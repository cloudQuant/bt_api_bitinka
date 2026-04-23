from __future__ import annotations

from typing import Any, Optional

from bt_api_base.containers.requestdatas.request_data import RequestData
from bt_api_base.feeds.capability import Capability
from bt_api_base.feeds.feed import Feed
from bt_api_base.feeds.http_client import HttpClient
from bt_api_base.logging_factory import get_logger

from bt_api_bitinka.exchange_data import BitinkaExchangeDataSpot

RequestParams = dict[str, Any]
RequestExtraData = dict[str, Any]
RequestSpec = tuple[str, Optional[RequestParams], RequestExtraData]


class BitinkaRequestData(Feed):
    @classmethod
    def _capabilities(cls) -> set[Capability]:
        return {
            Capability.GET_TICK,
            Capability.GET_DEPTH,
            Capability.GET_EXCHANGE_INFO,
            Capability.GET_BALANCE,
            Capability.GET_ACCOUNT,
            Capability.MAKE_ORDER,
            Capability.CANCEL_ORDER,
        }

    def __init__(self, data_queue: Any = None, **kwargs: Any) -> None:
        super().__init__(data_queue, **kwargs)
        self.data_queue = data_queue
        self.exchange_name = kwargs.get("exchange_name", "BITINKA___SPOT")
        self.asset_type = kwargs.get("asset_type", "SPOT")
        self._params = BitinkaExchangeDataSpot()
        api_key = kwargs.get("public_key") or kwargs.get("api_key") or ""
        api_secret = (
            kwargs.get("private_key") or kwargs.get("secret_key") or kwargs.get("api_secret") or ""
        )
        self._params.api_key = str(api_key)
        self._params.api_secret = str(api_secret)
        self.request_logger = get_logger("bitinka_feed")
        self.async_logger = get_logger("bitinka_feed")
        self._http_client = HttpClient(venue=self.exchange_name, timeout=10)

    def _get_headers(
        self,
        method: str,
        request_path: str,
        params: RequestParams | None = None,
        body: Any = "",
    ) -> dict[str, str]:
        headers = {"Content-Type": "application/json"}
        if self._params.api_key:
            headers["X-API-KEY"] = self._params.api_key
        return headers

    def request(
        self,
        path: str,
        params: RequestParams | None = None,
        body: Any | None = None,
        extra_data: RequestExtraData | None = None,
        timeout: int = 10,
    ) -> RequestData:
        method = path.split()[0] if " " in path else "GET"
        request_path = "/" + path.split()[1] if " " in path else path
        headers = self._get_headers(method, request_path, params, body)
        try:
            response = self._http_client.request(
                method=method,
                url=self._params.rest_url + request_path,
                headers=headers,
                json_data=body if method == "POST" else None,
                params=params,
            )
            return self._process_response(response, extra_data)
        except Exception as e:
            self.request_logger.error(f"Request failed: {e}")
            raise

    async def async_request(
        self,
        path: str,
        params: RequestParams | None = None,
        body: Any | None = None,
        extra_data: RequestExtraData | None = None,
        timeout: int = 5,
    ) -> RequestData:
        method = path.split()[0] if " " in path else "GET"
        request_path = "/" + path.split()[1] if " " in path else path
        headers = self._get_headers(method, request_path, params, body)
        try:
            response = await self._http_client.async_request(
                method=method,
                url=self._params.rest_url + request_path,
                headers=headers,
                json_data=body if method == "POST" else None,
                params=params,
            )
            return self._process_response(response, extra_data)
        except Exception as e:
            self.async_logger.error(f"Async request failed: {e}")
            raise

    def async_callback(self, future: Any) -> None:
        try:
            result = future.result()
            if result is not None:
                self.push_data_to_queue(result)
        except Exception as e:
            self.async_logger.error(f"Async callback error: {e}")

    def _process_response(
        self,
        response: dict[str, Any] | list[Any],
        extra_data: RequestExtraData | None = None,
    ) -> RequestData:
        if extra_data is None:
            extra_data = {}
        return RequestData(response, extra_data)

    def _get_server_time(
        self,
        extra_data: RequestExtraData | None = None,
        **kwargs: Any,
    ) -> RequestSpec:
        if extra_data is None:
            extra_data = {}
        extra_data.update(
            {
                "exchange_name": self.exchange_name,
                "symbol_name": "",
                "asset_type": self.asset_type,
                "request_type": "get_server_time",
            },
        )
        return "GET /serverTime", {}, extra_data

    def get_server_time(
        self,
        extra_data: RequestExtraData | None = None,
        **kwargs: Any,
    ) -> RequestData:
        path, params, extra_data = self._get_server_time(extra_data, **kwargs)
        return self.request(path, params=params, extra_data=extra_data)

    def push_data_to_queue(self, data: Any) -> None:
        if self.data_queue is not None:
            self.data_queue.put(data)

    def connect(self) -> None:
        pass

    def disconnect(self) -> None:
        super().disconnect()

    def is_connected(self) -> bool:
        return True
