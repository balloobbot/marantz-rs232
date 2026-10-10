"""Exceptions shared by all Marantz protocols."""

from __future__ import annotations


class MarantzConnectionError(ConnectionError):
    """Raised when the serial connection is not open or is lost."""
