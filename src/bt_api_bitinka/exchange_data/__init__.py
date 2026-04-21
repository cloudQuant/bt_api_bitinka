from __future__ import annotations

from bt_api_base.containers.exchanges.exchange_data import ExchangeData


_FALLBACK_REST_PATHS = {
    "get_exchange_info": "GET /markets",
    "get_tick": "GET /ticker",
    "get_depth": "GET /orderbook",
    "get_trades": "GET /trades",
    "get_account": "GET /account",
    "get_balance": "GET /balance",
    "make_order": "POST /order",
    "cancel_order": "POST /cancelOrder",
    "query_order": "GET /orderStatus",
    "get_open_orders": "GET /openOrders",
    "get_deals": "GET /trades",
}


class BitinkaExchangeData(ExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.exchange_name = "bitinka"
        self.rest_url = "https://www.bitinka.com/api"
        self.wss_url = ""
        self.rest_paths = dict(_FALLBACK_REST_PATHS)
        self.wss_paths = {}
        self.kline_periods = {
            "1m": "1m",
            "5m": "5m",
            "15m": "15m",
            "30m": "30m",
            "1h": "1h",
            "4h": "4h",
            "1d": "1d",
            "1w": "1w",
        }
        self.legal_currency = ["USDT", "USD", "EUR", "ARS", "BRL", "CLP", "COP", "PEN"]

    def get_symbol(self, symbol: str) -> str:
        if "-" in symbol:
            return symbol.replace("-", "/")
        if "_" in symbol:
            return symbol.replace("_", "/")
        return symbol

    def get_period(self, key: str) -> str:
        return self.kline_periods.get(key, key)

    def get_rest_path(self, key: str, **kwargs) -> str:
        if key not in self.rest_paths or self.rest_paths[key] == "":
            raise ValueError(f"[{self.exchange_name}] REST path not found: {key}")
        return self.rest_paths[key]


class BitinkaExchangeDataSpot(BitinkaExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.asset_type = "SPOT"
