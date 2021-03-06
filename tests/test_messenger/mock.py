from typing import Optional

from redcomet.messenger import Address, Location, Message, Packet
from redcomet.messenger.port import AddressTranslator, Channel


class MockAddressTranslator(AddressTranslator):
    def __init__(self, query_return=None):
        self._query_return = query_return
        self.query_called_with_address = None
        self.register_called_with_parameters = None
        self.register_is_called = False

    def query(self, address: Address) -> Optional[Location]:
        self.query_called_with_address = address
        return self._query_return

    def register(self, address: Address, location: Location):
        self.register_called_with_parameters = address, location
        self.register_is_called = True


class MockChannel(Channel):
    def __init__(self, send_error=None):
        self._send_error = send_error
        self.send_called_with_packet: Optional[Packet] = None

    def send(self, packet: Packet):
        self.send_called_with_packet = packet
        if self._send_error is not None:
            raise self._send_error


class MockMessageHandler:
    def __init__(self):
        self.called_with_packet = None
        self.is_called = False

    def handle(self, packet: Packet):
        self.called_with_packet = packet
        self.is_called = True


class MyMessage(Message):
    pass
