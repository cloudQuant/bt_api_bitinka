"""Module-level docstring."""
from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base.containers.orders.order import OrderData
from bt_api_base.functions.utils import from_dict_get_float, from_dict_get_string


class BitinkaOrderData(OrderData):
    """Class BitinkaOrderData"""
    def __init__(
        self,
        order_info: str | dict[str, Any],
        symbol_name: str,
        asset_type: str,
        has_been_json_encoded: bool = False,
    ) -> None:
        """__init__ method"""
        super().__init__(order_info, has_been_json_encoded)
        self.exchange_name = "BITINKA"
        self.local_update_time = time.time()
        self.symbol_name = symbol_name
        self.asset_type = asset_type

    def init_data(self) -> BitinkaOrderData:
        """init_data method"""
        if not self.has_been_json_encoded:
            self.order_data = (
                json.loads(self.order_info) if isinstance(self.order_info, str) else self.order_info
            )
            self.has_been_json_encoded = True

        payload = self.order_data if isinstance(self.order_data, dict) else {}
        inner = payload.get("data", payload)
        if isinstance(inner, dict):
            self.order_id = from_dict_get_string(inner, "orderId")
            self.order_side = from_dict_get_string(inner, "side")
            self.order_type = from_dict_get_string(inner, "type")
            self.order_price = from_dict_get_float(inner, "price")
            self.order_size = from_dict_get_float(inner, "amount")
            self.order_status = from_dict_get_string(inner, "status")
            self.order_symbol_name = from_dict_get_string(inner, "market", self.symbol_name)

        return self

    def get_exchange_name(self) -> str:
        """get_exchange_name method"""
        return str(self.exchange_name)

    def get_asset_type(self) -> str | None:
        """get_asset_type method"""
        return self.asset_type

    def get_symbol_name(self) -> str | None:
        """get_symbol_name method"""
        return self.symbol_name

    def get_server_time(self) -> float | None:
        """get_server_time method"""
        return self.server_time

    def get_local_update_time(self) -> float | None:
        """get_local_update_time method"""
        return float(self.local_update_time) if self.local_update_time is not None else None

    def get_trade_id(self) -> str | None:
        """get_trade_id method"""
        return self.trade_id

    def get_client_order_id(self) -> str | None:
        """get_client_order_id method"""
        return self.client_order_id

    def get_cum_quote(self) -> float | None:
        """get_cum_quote method"""
        return self.cum_quote

    def get_executed_qty(self) -> float | None:
        """get_executed_qty method"""
        return self.executed_qty

    def get_order_id(self) -> str | None:
        """get_order_id method"""
        self.init_data()
        return self.order_id

    def get_order_size(self) -> float | None:
        """get_order_size method"""
        self.init_data()
        return self.order_size

    def get_order_price(self) -> float | None:
        """get_order_price method"""
        self.init_data()
        return self.order_price

    def get_reduce_only(self) -> bool | None:
        """get_reduce_only method"""
        return self.reduce_only

    def get_order_side(self) -> str | None:
        """get_order_side method"""
        self.init_data()
        return self.order_side

    def get_order_status(self) -> str | None:
        """get_order_status method"""
        self.init_data()
        return self.order_status if isinstance(self.order_status, str) else None

    def get_order_symbol_name(self) -> str | None:
        """get_order_symbol_name method"""
        self.init_data()
        return self.order_symbol_name

    def get_order_time_in_force(self) -> str | None:
        """get_order_time_in_force method"""
        return self.order_time_in_force

    def get_order_type(self) -> str | None:
        """get_order_type method"""
        self.init_data()
        return self.order_type

    def get_order_avg_price(self) -> float | None:
        """get_order_avg_price method"""
        return self.order_avg_price

    def get_origin_order_type(self) -> str | None:
        """get_origin_order_type method"""
        return self.origin_order_type

    def get_position_side(self) -> str | None:
        """get_position_side method"""
        return self.position_side

    def get_trailing_stop_price(self) -> float | None:
        """get_trailing_stop_price method"""
        return self.trailing_stop_price

    def get_trailing_stop_trigger_price(self) -> float | None:
        """get_trailing_stop_trigger_price method"""
        return self.trailing_stop_trigger_price

    def get_trailing_stop_callback_rate(self) -> float | None:
        """get_trailing_stop_callback_rate method"""
        return self.trailing_stop_callback_rate

    def get_trailing_stop_trigger_price_type(self) -> str | None:
        """get_trailing_stop_trigger_price_type method"""
        return self.trailing_stop_trigger_price_type

    def get_stop_loss_price(self) -> float | None:
        """get_stop_loss_price method"""
        return self.stop_loss_price

    def get_stop_loss_trigger_price(self) -> float | None:
        """get_stop_loss_trigger_price method"""
        return self.stop_loss_trigger_price

    def get_stop_loss_trigger_price_type(self) -> str | None:
        """get_stop_loss_trigger_price_type method"""
        return self.stop_loss_trigger_price_type

    def get_take_profit_price(self) -> float | None:
        """get_take_profit_price method"""
        return self.take_profit_price

    def get_take_profit_trigger_price(self) -> float | None:
        """get_take_profit_trigger_price method"""
        return self.take_profit_trigger_price

    def get_take_profit_trigger_price_type(self) -> str | None:
        """get_take_profit_trigger_price_type method"""
        return self.take_profit_trigger_price_type

    def get_close_position(self) -> bool | None:
        """get_close_position method"""
        return self.close_position

    def get_order_offset(self) -> str | None:
        """get_order_offset method"""
        return self.order_offset

    def get_order_exchange_id(self) -> str | None:
        """get_order_exchange_id method"""
        return self.order_exchange_id

    def __str__(self) -> str:
        self.init_data()
        return json.dumps(self.get_all_data())

    def __repr__(self) -> str:
        return self.__str__()


class BitinkaRequestOrderData(BitinkaOrderData):
    """Class BitinkaRequestOrderData"""
    pass


class BitinkaWssOrderData(BitinkaOrderData):
    """Class BitinkaWssOrderData"""
    pass


__all__ = ["BitinkaOrderData", "BitinkaRequestOrderData", "BitinkaWssOrderData"]
