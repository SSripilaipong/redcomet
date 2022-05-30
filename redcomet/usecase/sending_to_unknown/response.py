from typing import Dict, Any, Optional

from redcomet.messenger import Message, Address, Location


class LocationQueryResponse(Message):
    def __init__(self, address: Address, location: Optional[Location], metadata: Dict[Any, Any]):
        self._address = address
        self._location = location
        self._metadata = metadata

    @property
    def address(self) -> Address:
        return self._address

    @property
    def location(self) -> Location:
        return self._location

    @property
    def metadata(self) -> Dict[Any, Any]:
        return self._metadata

    def __eq__(self, other):
        if not isinstance(other, LocationQueryResponse):
            return False
        return (self._address == other._address and self._location == other._location
                and self._metadata == other._metadata)

    def __repr__(self) -> str:
        return f"LocationQueryResponse({self._address!r}, {self._location!r}, metadata={self._metadata!r})"
