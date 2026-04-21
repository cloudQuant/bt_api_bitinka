# bt_api_bitinka

[![PyPI Version](https://img.shields.io/pypi/v/bt_api_bitinka.svg)](https://pypi.org/project/bt_api_bitinka/)
[![Python Versions](https://img.shields.io/pypi/pyversions/bt_api_bitinka.svg)](https://pypi.org/project/bt_api_bitinka/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/cloudQuant/bt_api_bitinka/actions/workflows/ci.yml/badge.svg)](https://github.com/cloudQuant/bt_api_bitinka/actions)
[![Docs](https://readthedocs.org/projects/bt-api-bitinka/badge/?version=latest)](https://bt-api-bitinka.readthedocs.io/)

---

<!-- English -->
# bt_api_bitinka

> **Bitinka exchange plugin for bt_api** — Unified REST API for **Spot** trading with support for **USD**, **USDT**, **EUR**, and **Latin American currencies** (ARS, BRL, CLP, COP, PEN).

`bt_api_bitinka` is a runtime plugin for [bt_api](https://github.com/cloudQuant/bt_api_py) that connects to **Bitinka** exchange. It depends on [bt_api_base](https://github.com/cloudQuant/bt_api_base) for core infrastructure.

Bitinka is a **Latin American cryptocurrency exchange** headquartered in Argentina, offering trading in USD, USDT, EUR, and several Latin American fiat currencies.

| Resource | Link |
|----------|------|
| English Docs | https://bt-api-bitinka.readthedocs.io/ |
| Chinese Docs | https://bt-api-bitinka.readthedocs.io/zh/latest/ |
| GitHub | https://github.com/cloudQuant/bt_api_bitinka |
| PyPI | https://pypi.org/project/bt_api_bitinka/ |
| Issues | https://github.com/cloudQuant/bt_api_bitinka/issues |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| Main Project | https://github.com/cloudQuant/bt_api_py |

---

## Features

### 1 Asset Type

| Asset Type | Code | REST | Description |
|---|---|---|---|
| Spot | `BITINKA___SPOT` | ✅ | Spot trading with USD, USDT, EUR, ARS, BRL, CLP, COP, PEN pairs |

### REST API

- **Market Data** — Ticker, order book depth, trades, exchange info
- **Account** — Balance, account info
- **Trading** — Place orders, cancel orders, query order status, open orders

### Plugin Architecture

Auto-registers at import time via `ExchangeRegistry`. Works seamlessly with `BtApi`:

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BITINKA___SPOT": {
        "api_key": "your_key",
        "secret": "your_secret",
    }
})

ticker = api.get_tick("BITINKA___SPOT", "BTCUSDT")
balance = api.get_balance("BITINKA___SPOT")
order = api.make_order(exchange_name="BITINKA___SPOT", symbol="BTCUSDT", volume=0.001, price=50000, order_type="limit")
```

### Unified Data Containers

All exchange responses normalized to bt_api_base container types:

- `TickContainer` — 24hr rolling ticker
- `OrderBookContainer` — Order book depth
- `TradeContainer` — Individual trades
- `OrderContainer` — Order status and fills
- `AccountBalanceContainer` — Asset balances

---

## Installation

### From PyPI (Recommended)

```bash
pip install bt_api_bitinka
```

### From Source

```bash
git clone https://github.com/cloudQuant/bt_api_bitinka
cd bt_api_bitinka
pip install -e .
```

### Requirements

- Python `3.9` – `3.14`
- `bt_api_base >= 0.15`
- `httpx` for HTTP client

---

## Quick Start

### 1. Install

```bash
pip install bt_api_bitinka
```

### 2. Get ticker (public — no API key needed)

```python
from bt_api_py import BtApi

api = BtApi()
ticker = api.get_tick("BITINKA___SPOT", "BTCUSDT")
print(f"BTCUSDT price: {ticker}")
```

### 3. Place an order (requires API key)

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BITINKA___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

order = api.make_order(
    exchange_name="BITINKA___SPOT",
    symbol="BTCUSDT",
    volume=0.001,
    price=50000,
    order_type="limit",
)
print(f"Order placed: {order}")
```

### 4. bt_api Plugin Integration

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BITINKA___SPOT": {"api_key": "key", "secret": "secret"}
})

# REST calls
ticker = api.get_tick("BITINKA___SPOT", "BTCUSDT")
balance = api.get_balance("BITINKA___SPOT")
order = api.make_order(exchange_name="BITINKA___SPOT", symbol="BTCUSDT", volume=0.001, price=50000, order_type="limit")
```

---

## Architecture

```
bt_api_bitinka/
├── plugin.py                     # register_plugin() — bt_api plugin entry point
├── registry_registration.py      # register_bitinka() — feeds / exchange_data registration
├── exchange_data/
│   └── __init__.py             # BitinkaExchangeData (base) + BitinkaExchangeDataSpot
├── feeds/
│   ├── live_bitinka/
│   │   ├── spot.py             # BitinkaRequestDataSpot — SPOT feed
│   │   └── request_base.py    # BitinkaRequestData — base request class
│   └── __init__.py
├── containers/                   # Normalized data containers
├── errors/
│   └── __init__.py
└── __init__.py
```

---

## Supported Operations

| Category | Operation | Notes |
|---|---|---|
| **Market Data** | `get_tick` | 24hr rolling ticker |
| | `get_depth` | Order book depth |
| | `get_exchange_info` | Exchange configuration |
| | `get_deals` | Recent trades |
| **Account** | `get_balance` | Asset balances |
| | `get_account` | Full account info |
| **Trading** | `make_order` | LIMIT orders |
| | `cancel_order` | Cancel order by ID |
| | `query_order` | Query order status |
| | `get_open_orders` | All open orders |

---

## Supported Bitinka Symbols

Bitinka trading pairs are supported across multiple quote currencies:

- **USDT pairs**: `BTCUSDT`, `ETHUSDT`, `SOLUSDT` ...
- **USD pairs**: `BTCUSD`, `ETHUSD` ...
- **EUR pairs**: `BTCEUR`, `ETHEUR` ...
- **Latin American fiat**: `BTCARS`, `ETHBRL`, `BTCCLP`, `ETHCOP`, `ETHPEN` ...

---

## Error Handling

All Bitinka API errors are translated to bt_api_base `ApiError` subclasses.

---

## Documentation

| Doc | Link |
|-----|------|
| **English** | https://bt-api-bitinka.readthedocs.io/ |
| **中文** | https://bt-api-bitinka.readthedocs.io/zh/latest/ |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| Main Project | https://cloudquant.github.io/bt_api_py/ |

---

## License

MIT — see [LICENSE](LICENSE).

---

## Support

- [GitHub Issues](https://github.com/cloudQuant/bt_api_bitinka/issues) — bug reports, feature requests
- Email: yunjinqi@gmail.com

---

---

## 中文

> **bt_api 的 Bitinka 交易所插件** — 为**现货**交易提供统一的 REST API，支持 **USD**、**USDT**、**EUR** 以及 **拉丁美洲法币**（ARS、BRL、CLP、COP、PEN）。

`bt_api_bitinka` 是 [bt_api](https://github.com/cloudQuant/bt_api_py) 的运行时插件，连接 **Bitinka** 交易所。依赖 [bt_api_base](https://github.com/cloudQuant/bt_api_base) 提供核心基础设施。

Bitinka 是 **拉丁美洲加密货币交易所**，总部位于阿根廷，提供 USD、USDT、EUR 及多种拉丁美洲法币的交易对。

| 资源 | 链接 |
|------|------|
| 英文文档 | https://bt-api-bitinka.readthedocs.io/ |
| 中文文档 | https://bt-api-bitinka.readthedocs.io/zh/latest/ |
| GitHub | https://github.com/cloudQuant/bt_api_bitinka |
| PyPI | https://pypi.org/project/bt_api_bitinka/ |
| 问题反馈 | https://github.com/cloudQuant/bt_api_bitinka/issues |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| 主项目 | https://github.com/cloudQuant/bt_api_py |

---

## 功能特点

### 1 种资产类型

| 资产类型 | 代码 | REST | 说明 |
|---|---|---|---|
| 现货 | `BITINKA___SPOT` | ✅ | 现货交易，支持 USD、USDT、EUR、ARS、BRL、CLP、COP、PEN 交易对 |

### REST API

- **行情数据** — 行情、订单簿深度、成交、交易所信息
- **账户** — 余额、账户信息
- **交易** — 下单、撤单、查询订单状态、挂单列表

### 插件架构

通过 `ExchangeRegistry` 在导入时自动注册，与 `BtApi` 无缝协作：

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BITINKA___SPOT": {
        "api_key": "your_key",
        "secret": "your_secret",
    }
})

ticker = api.get_tick("BITINKA___SPOT", "BTCUSDT")
balance = api.get_balance("BITINKA___SPOT")
order = api.make_order(exchange_name="BITINKA___SPOT", symbol="BTCUSDT", volume=0.001, price=50000, order_type="limit")
```

### 统一数据容器

所有交易所响应规范化为 bt_api_base 容器类型：

- `TickContainer` — 24小时滚动行情
- `OrderBookContainer` — 订单簿深度
- `TradeContainer` — 逐笔成交
- `OrderContainer` — 订单状态和成交
- `AccountBalanceContainer` — 资产余额

---

## 安装

### 从 PyPI 安装（推荐）

```bash
pip install bt_api_bitinka
```

### 从源码安装

```bash
git clone https://github.com/cloudQuant/bt_api_bitinka
cd bt_api_bitinka
pip install -e .
```

### 系统要求

- Python `3.9` – `3.14`
- `bt_api_base >= 0.15`
- `httpx` HTTP 客户端

---

## 快速开始

### 1. 安装

```bash
pip install bt_api_bitinka
```

### 2. 获取行情（公开接口，无需 API key）

```python
from bt_api_py import BtApi

api = BtApi()
ticker = api.get_tick("BITINKA___SPOT", "BTCUSDT")
print(f"BTCUSDT 价格: {ticker}")
```

### 3. 下单交易（需要 API key）

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BITINKA___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

order = api.make_order(
    exchange_name="BITINKA___SPOT",
    symbol="BTCUSDT",
    volume=0.001,
    price=50000,
    order_type="limit",
)
print(f"订单已下单: {order}")
```

### 4. bt_api 插件集成

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "BITINKA___SPOT": {"api_key": "key", "secret": "secret"}
})

# REST 调用
ticker = api.get_tick("BITINKA___SPOT", "BTCUSDT")
balance = api.get_balance("BITINKA___SPOT")
order = api.make_order(exchange_name="BITINKA___SPOT", symbol="BTCUSDT", volume=0.001, price=50000, order_type="limit")
```

---

## 架构

```
bt_api_bitinka/
├── plugin.py                     # register_plugin() — bt_api 插件入口
├── registry_registration.py     # register_bitinka() — feeds / exchange_data 注册
├── exchange_data/
│   └── __init__.py            # BitinkaExchangeData（基类）+ BitinkaExchangeDataSpot
├── feeds/
│   ├── live_bitinka/
│   │   ├── spot.py            # BitinkaRequestDataSpot — SPOT feed
│   │   └── request_base.py   # BitinkaRequestData — 请求基类
│   └── __init__.py
├── containers/                   # 规范化数据容器
├── errors/
│   └── __init__.py
└── __init__.py
```

---

## 支持的操作

| 类别 | 操作 | 说明 |
|---|---|---|
| **行情数据** | `get_tick` | 24小时滚动行情 |
| | `get_depth` | 订单簿深度 |
| | `get_exchange_info` | 交易所配置 |
| | `get_deals` | 近期成交 |
| **账户** | `get_balance` | 资产余额 |
| | `get_account` | 完整账户信息 |
| **交易** | `make_order` | 限价单 |
| | `cancel_order` | 按 ID 撤单 |
| | `query_order` | 查询订单状态 |
| | `get_open_orders` | 所有挂单 |

---

## 支持的 Bitinka 交易对

支持多种计价货币的 Bitinka 交易对：

- **USDT 交易对**: `BTCUSDT`, `ETHUSDT`, `SOLUSDT` ...
- **USD 交易对**: `BTCUSD`, `ETHUSD` ...
- **EUR 交易对**: `BTCEUR`, `ETHEUR` ...
- **拉丁美洲法币交易对**: `BTCARS`, `ETHBRL`, `BTCCLP`, `ETHCOP`, `ETHPEN` ...

---

## 错误处理

所有 Bitinka API 错误均翻译为 bt_api_base `ApiError` 子类。

---

## 文档

| 文档 | 链接 |
|-----|------|
| **英文文档** | https://bt-api-bitinka.readthedocs.io/ |
| **中文文档** | https://bt-api-bitinka.readthedocs.io/zh/latest/ |
| bt_api_base | https://bt-api-base.readthedocs.io/ |
| 主项目 | https://cloudquant.github.io/bt_api_py/ |

---

## 许可证

MIT — 详见 [LICENSE](LICENSE)。

---

## 技术支持

- [GitHub Issues](https://github.com/cloudQuant/bt_api_bitinka/issues) — bug 报告、功能请求
- 邮箱: yunjinqi@gmail.com
