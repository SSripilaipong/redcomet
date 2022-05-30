from typing import Dict, Any

from redcomet.messenger import Message, Address


class LocationQueryMessage(Message):
    def __init__(self, address: Address, metadata: Dict[Any, Any]):
        self._address = address
        self._metadata = metadata

    def __eq__(self, other):
        if not isinstance(other, LocationQueryMessage):
            return False
        return self._address == other._address and self._metadata == other._metadata
