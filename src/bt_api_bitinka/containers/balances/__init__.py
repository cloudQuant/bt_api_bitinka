from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base.containers.balances.balance import BalanceData
from bt_api_base.functions.utils import from_dict_get_float, from_dict_get_string


class BitinkaBalanceData(BalanceData):
    def __init__(
        self,
        balance_info: Any,
        asset_type: str = "SPOT",
        has_been_json_encoded: bool = False,
    ) -> None:
        super().__init__(balance_info, has_been_json_encoded)
        self.exchange_name = "BITINKA"
        self.asset_type = asset_type
        self.balance_data: dict[str, Any] | None = balance_info if has_been_json_encoded else None
        self.currency: str | None = None
        self.available: float | None = None
        self.locked: float | None = None
        self.local_update_time = time.time()

    def init_data(self) -> BitinkaBalanceData:
        if not self.has_been_json_encoded:
            self.balance_data = (
                json.loads(self.balance_info)
                if isinstance(self.balance_info, str)
                else self.balance_info
            )
            self.has_been_json_encoded = True

        payload = self.balance_data if isinstance(self.balance_data, dict) else {}
        inner = payload.get("data", payload)
        if isinstance(inner, dict):
            self.currency = from_dict_get_string(inner, "currency")
            self.available = from_dict_get_float(inner, "available")
            self.locked = from_dict_get_float(inner, "locked")

        return self

    def get_all_data(self) -> dict[str, Any]:
        self.init_data()
        return {
            "exchange_name": self.exchange_name,
            "asset_type": self.asset_type,
            "local_update_time": self.local_update_time,
            "currency": self.currency,
            "available": self.available,
            "locked": self.locked,
            "total": self.get_total(),
        }

    def get_exchange_name(self) -> str:
        return self.exchange_name

    def get_asset_type(self) -> str | None:
        return self.asset_type

    def get_server_time(self) -> float | None:
        return None

    def get_local_update_time(self) -> float | None:
        return float(self.local_update_time)

    def get_account_id(self) -> str | None:
        return None

    def get_account_type(self) -> str | None:
        return None

    def get_fee_tier(self) -> int | str | None:
        return None

    def get_max_withdraw_amount(self) -> float | None:
        return None

    def get_margin(self) -> float | None:
        return None

    def get_used_margin(self) -> float | None:
        return None

    def get_available_margin(self) -> float | None:
        return self.available

    def get_cash(self) -> float | None:
        return self.available

    def get_total(self) -> float:
        return float((self.available or 0.0) + (self.locked or 0.0))

    def get_currency(self) -> str | None:
        self.init_data()
        return self.currency

    def get_available(self) -> float | None:
        self.init_data()
        return self.available

    def get_locked(self) -> float | None:
        self.init_data()
        return self.locked

    def __str__(self) -> str:
        return json.dumps(self.get_all_data())

    def __repr__(self) -> str:
        return self.__str__()


class BitinkaRequestBalanceData(BitinkaBalanceData):
    pass


class BitinkaWssBalanceData(BitinkaBalanceData):
    pass


__all__ = [
    "BitinkaBalanceData",
    "BitinkaRequestBalanceData",
    "BitinkaWssBalanceData",
]
