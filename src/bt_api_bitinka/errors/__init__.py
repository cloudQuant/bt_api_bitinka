from __future__ import annotations

from typing import Any

from bt_api_base.error import ErrorCategory, ErrorTranslator, UnifiedError, UnifiedErrorCode


class BitinkaErrorTranslator(ErrorTranslator):
    @classmethod
    def translate(cls, raw_error: dict[str, Any], venue: str) -> UnifiedError | None:
        message = str(raw_error.get("message", raw_error.get("msg", ""))).lower()

        if "balance" in message or "insufficient" in message:
            return cls._build_error(
                code=UnifiedErrorCode.INSUFFICIENT_BALANCE,
                venue=venue,
                raw_error=raw_error,
            )
        if "order" in message and "not found" in message:
            return cls._build_error(
                code=UnifiedErrorCode.ORDER_NOT_FOUND,
                venue=venue,
                raw_error=raw_error,
            )
        if "order" in message and "duplicate" in message:
            return cls._build_error(
                code=UnifiedErrorCode.DUPLICATE_ORDER,
                venue=venue,
                raw_error=raw_error,
            )
        if "rate" in message or "limit" in message:
            return cls._build_error(
                code=UnifiedErrorCode.RATE_LIMIT_EXCEEDED,
                venue=venue,
                raw_error=raw_error,
            )
        if "auth" in message or "key" in message or "signature" in message:
            return cls._build_error(
                code=UnifiedErrorCode.INVALID_API_KEY,
                venue=venue,
                raw_error=raw_error,
            )

        return super().translate(raw_error, venue)

    @staticmethod
    def _build_error(
        *, code: UnifiedErrorCode, venue: str, raw_error: dict[str, Any],
    ) -> UnifiedError:
        message = str(raw_error.get("message", raw_error.get("msg", code.name)))
        return UnifiedError(
            code=code,
            category=ErrorCategory.BUSINESS,
            venue=venue,
            message=message,
            original_error=str(raw_error),
            context={"raw_response": raw_error},
        )
