from typing import Dict, Any

from redcomet.messenger import Message, Address


class LocationQueryRequest(Message):
    def __init__(self, address: Address, metadata: Dict[Any, Any]):
        self._address = address
        self._metadata = metadata

    def __eq__(self, other) -> bool:
        if not isinstance(other, LocationQueryRequest):
            return False
        return self._address == other._address and self._metadata == other._metadata

    def __repr__(self) -> str:
        return f"LocationQueryRequest({self._address!r}, metadata={self._metadata!r})"
