from redcomet.messenger import Message, Messenger, Address
from redcomet.messenger.location import Location
from redcomet.messenger.port import AddressTranslator


class MockAddressTranslator(AddressTranslator):
    def __init__(self):
        self.query_called_with_address = None

    def query(self, address: Address) -> Location:
        self.query_called_with_address = address


class MyMessage(Message):
    pass


def test_should_send_via_channel_when_the_address_is_known():
    translator = MockAddressTranslator()
    messenger = Messenger(address_translator=translator)
    message = MyMessage()

    messenger.send(Address("$.hello"), message)

    assert translator.query_called_with_address == Address("$.hello")
