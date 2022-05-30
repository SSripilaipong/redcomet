from redcomet.messenger import Message, Messenger, Address, Location, Packet
from redcomet.usecase.discovery import LocationQueryMessage
from tests.test_messenger.mock import MockAddressTranslator, MockChannel


class MyMessage(Message):
    pass


def test_should_query_location_from_address_translator():
    translator = MockAddressTranslator(Location(""))
    messenger = Messenger(Address(""),
                          address_translator=translator,
                          discovery_location=Location("discovery_node"),
                          channels={Location(""): MockChannel()})

    messenger.send(Address("$.hello"), MyMessage())

    assert translator.query_called_with_address == Address("$.hello")


def test_should_send_message_to_corresponding_channel_when_the_location_is_known():
    channel = MockChannel()
    messenger = Messenger(Address("$.me"),
                          address_translator=MockAddressTranslator(query_return=Location("my_node")),
                          discovery_location=Location("discovery_node"),
                          channels={Location("my_node"): channel})
    message = MyMessage()

    messenger.send(Address("$.you"), message)

    assert channel.send_called_with_packet == Packet(message, Address("$.me"), Address("$.you"))


def test_should_suppress_any_exception_from_channel_send():
    messenger = Messenger(Address(""),
                          address_translator=MockAddressTranslator(query_return=Location("my_node")),
                          discovery_location=Location("discovery_node"),
                          channels={Location("my_node"): MockChannel(send_error=BaseException())})

    messenger.send(Address("$.hello"), MyMessage())


def test_should_send_query_message_to_discovery_service_when_address_is_unknown():
    channel = MockChannel()
    messenger = Messenger(Address("$.me"),
                          address_translator=MockAddressTranslator(query_return=None),
                          discovery_location=Location("discovery_node"),
                          channels={Location("discovery_node"): channel})
    message = MyMessage()

    messenger.send(Address("$.hello"), message)

    expected = LocationQueryMessage(Address("$.hello"), metadata={"pending_message": message})
    assert channel.send_called_with_packet == Packet(expected, Address("$.me"), Address("$.discovery"))
