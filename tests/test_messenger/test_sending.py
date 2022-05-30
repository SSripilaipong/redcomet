from redcomet.messenger import Messenger, Address, Location, Packet
from tests.test_messenger.mock import MockAddressTranslator, MockChannel, MyMessage


def test_should_query_location_from_address_translator():
    translator = MockAddressTranslator(Location(""))
    messenger = Messenger(Address(""), Location(""),
                          handle=lambda _: ...,
                          address_translator=translator,
                          discovery_location=Location("discovery_node"),
                          channels={Location(""): MockChannel()})

    messenger.send(MyMessage(), Address("$.me"), Address("$.hello"))

    assert translator.query_called_with_address == Address("$.hello")


def test_should_send_message_to_corresponding_channel_when_the_location_is_known():
    channel = MockChannel()
    messenger = Messenger(Address(""), Location(""),
                          handle=lambda _: ...,
                          address_translator=MockAddressTranslator(query_return=Location("my_node")),
                          discovery_location=Location("discovery_node"),
                          channels={Location("my_node"): channel})
    message = MyMessage()

    messenger.send(message, Address("$.me"), Address("$.you"))

    assert channel.send_called_with_packet == Packet(message, Address("$.me"), Address("$.you"))


def test_should_suppress_any_exception_from_channel_send():
    messenger = Messenger(Address(""), Location(""),
                          handle=lambda _: ...,
                          address_translator=MockAddressTranslator(query_return=Location("my_node")),
                          discovery_location=Location("discovery_node"),
                          channels={Location("my_node"): MockChannel(send_error=BaseException())})

    messenger.send(MyMessage(), Address("$.me"), Address("$.hello"))


def test_should_attach_sender_location():
    channel = MockChannel()
    messenger = Messenger(Address(""), Location("my_node"),
                          handle=lambda _: ...,
                          address_translator=MockAddressTranslator(),
                          discovery_location=Location("your_node"),
                          channels={Location("your_node"): channel})

    messenger.send(MyMessage(), Address("$.me"), Address("$.you"))

    assert channel.send_called_with_packet.sender_location == Location("my_node")
