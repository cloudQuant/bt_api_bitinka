"""Module-level docstring."""
from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base.containers.accounts.account import AccountData


class BitinkaAccountData(AccountData):
    """Class BitinkaAccountData"""
    def __init__(
        self,
        account_info: dict[str, Any] | str,
        symbol_name: str,
        asset_type: str,
        has_been_json_encoded: bool = False,
    ) -> None:
        """__init__ method"""
        super().__init__(account_info, has_been_json_encoded)
        self.exchange_name = "BITINKA"
        self.local_update_time = time.time()
        self.symbol_name = symbol_name
        self.asset_type = asset_type

    def init_data(self) -> BitinkaAccountData:
        """init_data method"""
        if not self.has_been_json_encoded:
            self.account_data = (
                json.loads(self.account_info)
                if isinstance(self.account_info, str)
                else self.account_info
            )
            self.has_been_json_encoded = True

        payload = self.account_data if isinstance(self.account_data, dict) else {}
        inner = payload.get("data", payload)
        if isinstance(inner, dict):
            balances = inner.get("balance", [])
            self.balances = list(balances) if isinstance(balances, list) else []

        return self

    def get_exchange_name(self) -> str:
        """get_exchange_name method"""
        return str(self.exchange_name)

    def get_asset_type(self) -> str | None:
        """get_asset_type method"""
        return self.asset_type

    def get_server_time(self) -> int | float | None:
        """get_server_time method"""
        return self.server_time

    def get_local_update_time(self) -> int | float | None:
        """get_local_update_time method"""
        return self.local_update_time

    def get_account_id(self) -> str | None:
        """get_account_id method"""
        return self.account_id

    def get_account_type(self) -> str | None:
        """get_account_type method"""
        return self.account_type

    def get_can_deposit(self) -> bool | None:
        """get_can_deposit method"""
        return self.can_deposit

    def get_can_trade(self) -> bool | None:
        """get_can_trade method"""
        return self.can_trade

    def get_can_withdraw(self) -> bool | None:
        """get_can_withdraw method"""
        return self.can_withdraw

    def get_fee_tier(self) -> int | str | None:
        """get_fee_tier method"""
        return self.fee_tier

    def get_max_withdraw_amount(self) -> float | None:
        """get_max_withdraw_amount method"""
        return self.max_withdraw_amount

    def get_total_margin(self) -> float | None:
        """get_total_margin method"""
        return self.total_margin

    def get_total_used_margin(self) -> float | None:
        """get_total_used_margin method"""
        return self.total_used_margin

    def get_total_maintain_margin(self) -> float | None:
        """get_total_maintain_margin method"""
        return self.total_maintain_margin

    def get_total_available_margin(self) -> float | None:
        """get_total_available_margin method"""
        return self.total_available_margin

    def get_total_open_order_initial_margin(self) -> float | None:
        """get_total_open_order_initial_margin method"""
        return self.total_open_order_initial_margin

    def get_total_position_initial_margin(self) -> float | None:
        """get_total_position_initial_margin method"""
        return self.total_position_initial_margin

    def get_total_unrealized_profit(self) -> float | None:
        """get_total_unrealized_profit method"""
        return self.total_unrealized_profit

    def get_total_wallet_balance(self) -> float | None:
        """get_total_wallet_balance method"""
        return self.total_wallet_balance

    def get_balances(self) -> list[Any]:
        """get_balances method"""
        self.init_data()
        return list(self.balances)

    def get_positions(self) -> list[Any]:
        """get_positions method"""
        return list(self.positions)

    def get_spot_maker_commission_rate(self) -> float | None:
        """get_spot_maker_commission_rate method"""
        return self.spot_maker_commission_rate

    def get_spot_taker_commission_rate(self) -> float | None:
        """get_spot_taker_commission_rate method"""
        return self.spot_taker_commission_rate

    def get_future_maker_commission_rate(self) -> float | None:
        """get_future_maker_commission_rate method"""
        return self.future_maker_commission_rate

    def get_future_taker_commission_rate(self) -> float | None:
        """get_future_taker_commission_rate method"""
        return self.future_taker_commission_rate

    def get_option_maker_commission_rate(self) -> float | None:
        """get_option_maker_commission_rate method"""
        return self.option_maker_commission_rate

    def get_option_taker_commission_rate(self) -> float | None:
        """get_option_taker_commission_rate method"""
        return self.option_taker_commission_rate

    def __str__(self) -> str:
        self.init_data()
        return json.dumps(self.get_all_data())

    def __repr__(self) -> str:
        return self.__str__()


class BitinkaRequestAccountData(BitinkaAccountData):
    """Class BitinkaRequestAccountData"""
    pass


class BitinkaWssAccountData(BitinkaAccountData):
    """Class BitinkaWssAccountData"""
    pass


__all__ = [
    "BitinkaAccountData",
    "BitinkaRequestAccountData",
    "BitinkaWssAccountData",
]
