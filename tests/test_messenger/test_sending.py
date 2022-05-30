from redcomet.messenger import Message, Messenger, Address, Location
from tests.test_messenger.mock import MockAddressTranslator, MockChannel


class MyMessage(Message):
    pass


def test_should_query_location_from_address_translator():
    translator = MockAddressTranslator()
    messenger = Messenger(address_translator=translator, channels={})

    messenger.send(Address("$.hello"), MyMessage())

    assert translator.query_called_with_address == Address("$.hello")


def test_should_send_message_to_corresponding_channel_when_the_location_is_known():
    channel = MockChannel()
    translator = MockAddressTranslator(query_return={(Address("$.hello"),): Location("my_node")})
    messenger = Messenger(address_translator=translator, channels={Location("my_node"): channel})
    message = MyMessage()

    messenger.send(Address("$.hello"), message)

    assert channel.send_called_with_message == message
