from typing import Optional

from redcomet.messenger import Address, Location, Message
from redcomet.messenger.port import AddressTranslator, Channel


class MockAddressTranslator(AddressTranslator):
    def __init__(self, query_return=None):
        self._query_return = query_return or {}
        self.query_called_with_address = None

    def query(self, address: Address) -> Optional[Location]:
        self.query_called_with_address = address
        return self._query_return.get((address,))


class MockChannel(Channel):
    def __init__(self):
        self.send_called_with_message = None

    def send(self, message: Message):
        self.send_called_with_message = message
