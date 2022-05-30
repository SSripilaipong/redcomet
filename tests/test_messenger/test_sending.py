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
    messenger = Messenger(address_translator=MockAddressTranslator(query_return=Location("my_node")),
                          channels={Location("my_node"): channel})
    message = MyMessage()

    messenger.send(Address("$.hello"), message)

    assert channel.send_called_with_message == message


def test_should_send_address_to_corresponding_channel_when_the_location_is_known():
    channel = MockChannel()
    messenger = Messenger(address_translator=MockAddressTranslator(query_return=Location("my_node")),
                          channels={Location("my_node"): channel})
    message = MyMessage()

    messenger.send(Address("$.hello"), message)

    assert channel.send_called_with_address == Address("$.hello")


def test_should_suppress_any_exception_from_channel_send():
    messenger = Messenger(address_translator=MockAddressTranslator(query_return=Location("my_node")),
                          channels={Location("my_node"): MockChannel(send_error=BaseException())})

    messenger.send(Address("$.hello"), MyMessage())
