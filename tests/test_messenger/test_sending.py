from redcomet.messenger import Message, Messenger, Address
from tests.test_messenger.mock import MockAddressTranslator


class MyMessage(Message):
    pass


def test_should_query_location_from_address_translator():
    translator = MockAddressTranslator()
    messenger = Messenger(address_translator=translator)

    messenger.send(Address("$.hello"), MyMessage())

    assert translator.query_called_with_address == Address("$.hello")
