from __future__ import annotations

from bt_api_base.balance_utils import simple_balance_handler as _bitinka_balance_handler
from bt_api_base.registry import ExchangeRegistry

from bt_api_bitinka.exchange_data import BitinkaExchangeDataSpot
from bt_api_bitinka.feeds.live_bitinka.spot import BitinkaRequestDataSpot


def register_bitinka(registry: ExchangeRegistry | type[ExchangeRegistry]) -> None:
    registry.register_feed("BITINKA___SPOT", BitinkaRequestDataSpot)
    registry.register_exchange_data("BITINKA___SPOT", BitinkaExchangeDataSpot)
    registry.register_balance_handler("BITINKA___SPOT", _bitinka_balance_handler)


def register(registry: ExchangeRegistry | None = None) -> None:
    if registry is None:
        register_bitinka(ExchangeRegistry)
        return
    register_bitinka(registry)
