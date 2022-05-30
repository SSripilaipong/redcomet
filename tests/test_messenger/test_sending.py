from redcomet.messenger import Messenger, Address, Location, Packet
from tests.test_messenger.mock import MockAddressTranslator, MockChannel, MyMessage


def test_should_query_location_from_address_translator():
    translator = MockAddressTranslator(Location(""))
    messenger = Messenger(Address(""),
                          handle=lambda _: ...,
                          address_translator=translator,
                          discovery_location=Location("discovery_node"),
                          channels={Location(""): MockChannel()})

    messenger.send(MyMessage(), None, Address("$.hello"))

    assert translator.query_called_with_address == Address("$.hello")


def test_should_send_message_to_corresponding_channel_when_the_location_is_known():
    channel = MockChannel()
    messenger = Messenger(Address("$.me"),
                          handle=lambda _: ...,
                          address_translator=MockAddressTranslator(query_return=Location("my_node")),
                          discovery_location=Location("discovery_node"),
                          channels={Location("my_node"): channel})
    message = MyMessage()

    messenger.send(message, None, Address("$.you"))

    assert channel.send_called_with_packet == Packet(message, Address("$.me"), Address("$.you"))


def test_should_suppress_any_exception_from_channel_send():
    messenger = Messenger(Address(""),
                          handle=lambda _: ...,
                          address_translator=MockAddressTranslator(query_return=Location("my_node")),
                          discovery_location=Location("discovery_node"),
                          channels={Location("my_node"): MockChannel(send_error=BaseException())})

    messenger.send(MyMessage(), None, Address("$.hello"))
