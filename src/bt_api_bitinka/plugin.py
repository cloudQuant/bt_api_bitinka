from __future__ import annotations

from typing import Any

from bt_api_base.plugins.protocol import PluginInfo
from bt_api_base.registry import ExchangeRegistry

from bt_api_bitinka import __version__
from bt_api_bitinka.registry_registration import register_bitinka


def get_plugin_info() -> PluginInfo:
    return PluginInfo(
        name="bt_api_bitinka",
        version=__version__,
        core_requires=">=0.15,<1.0",
        supported_exchanges=("BITINKA___SPOT",),
        supported_asset_types=("SPOT",),
        plugin_module="bt_api_bitinka.plugin",
    )


def register_plugin(registry: ExchangeRegistry, runtime_factory: Any) -> PluginInfo:
    register_bitinka(registry)
    return get_plugin_info()
