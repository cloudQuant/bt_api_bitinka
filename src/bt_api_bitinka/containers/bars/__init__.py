from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base.containers.bars.bar import BarData


class BitinkaBarData(BarData):
    def __init__(
        self,
        bar_info: str | list[Any] | dict[str, Any],
        symbol_name: str,
        asset_type: str,
        has_been_json_encoded: bool = False,
    ) -> None:
        super().__init__(bar_info, has_been_json_encoded)
        self.exchange_name = "BITINKA"
        self.local_update_time = time.time()
        self.symbol_name = symbol_name
        self.asset_type = asset_type
        self.bar_data = bar_info if has_been_json_encoded else None
        self.open_time: float | int = 0
        self.open_price: float | int = 0.0
        self.high_price: float | int = 0.0
        self.low_price: float | int = 0.0
        self.close_price: float | int = 0.0
        self.volume: float | int = 0.0

    def init_data(self) -> BitinkaBarData:
        if not self.has_been_json_encoded:
            self.bar_data = (
                json.loads(self.bar_info) if isinstance(self.bar_info, str) else self.bar_info
            )
            self.has_been_json_encoded = True

        payload = self.bar_data
        inner = payload.get("data", payload) if isinstance(payload, dict) else payload
        if isinstance(inner, list) and len(inner) >= 5:
            self.open_time = int(inner[0])
            self.open_price = float(inner[1])
            self.close_price = float(inner[2])
            self.high_price = float(inner[3])
            self.low_price = float(inner[4])
            if len(inner) > 5:
                self.volume = float(inner[5])

        return self

    def get_exchange_name(self) -> str:
        return self.exchange_name

    def get_symbol_name(self) -> str:
        return self.symbol_name

    def get_asset_type(self) -> str:
        return self.asset_type

    def get_server_time(self) -> float | int | None:
        return None

    def get_local_update_time(self) -> float | int | None:
        return self.local_update_time

    def get_open_time(self) -> float | int:
        self.init_data()
        return self.open_time

    def get_open_price(self) -> float | int:
        self.init_data()
        return self.open_price

    def get_high_price(self) -> float | int:
        self.init_data()
        return self.high_price

    def get_low_price(self) -> float | int:
        self.init_data()
        return self.low_price

    def get_close_price(self) -> float | int:
        self.init_data()
        return self.close_price

    def get_volume(self) -> float | int:
        self.init_data()
        return self.volume

    def get_amount(self) -> float | int:
        return 0.0

    def get_close_time(self) -> float | int:
        return self.get_open_time()

    def get_quote_asset_volume(self) -> float | int:
        return 0.0

    def get_base_asset_volume(self) -> float | int:
        return self.get_volume()

    def get_num_trades(self) -> int:
        return 0

    def get_taker_buy_base_asset_volume(self) -> float | int:
        return 0.0

    def get_taker_buy_quote_asset_volume(self) -> float | int:
        return 0.0

    def get_bar_status(self) -> bool | int:
        return True

    def get_all_data(self) -> dict[str, Any]:
        self.init_data()
        return {
            "exchange_name": self.exchange_name,
            "symbol_name": self.symbol_name,
            "asset_type": self.asset_type,
            "local_update_time": self.local_update_time,
            "open_time": self.open_time,
            "open_price": self.open_price,
            "high_price": self.high_price,
            "low_price": self.low_price,
            "close_price": self.close_price,
            "volume": self.volume,
        }

    def __str__(self) -> str:
        return json.dumps(self.get_all_data())

    def __repr__(self) -> str:
        return self.__str__()


class BitinkaRequestBarData(BitinkaBarData):
    pass


class BitinkaWssBarData(BitinkaBarData):
    pass


__all__ = ["BitinkaBarData", "BitinkaRequestBarData", "BitinkaWssBarData"]
