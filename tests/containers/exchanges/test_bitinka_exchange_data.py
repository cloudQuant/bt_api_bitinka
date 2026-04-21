"""Tests for BitinkaExchangeData container."""

from __future__ import annotations

from bt_api_bitinka.exchange_data import BitinkaExchangeData


class TestBitinkaExchangeData:
    """Tests for BitinkaExchangeData."""

    def test_init(self):
        """Test initialization."""
        exchange = BitinkaExchangeData()

        assert exchange.exchange_name == "bitinka"
