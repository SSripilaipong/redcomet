from redcomet.messenger import Messenger, Address, Location, Packet
from redcomet.usecase.discovery import LocationQueryMessage
from tests.test_messenger.mock import MockChannel, MockAddressTranslator, MyMessage


def test_should_send_query_message_to_discovery_service_when_address_is_unknown():
    channel = MockChannel()
    messenger = Messenger(Address("$.me"),
                          handle=lambda _: ...,
                          address_translator=MockAddressTranslator(query_return=None),
                          discovery_location=Location("discovery_node"),
                          channels={Location("discovery_node"): channel})
    message = MyMessage()

    messenger.send(Address("$.hello"), message)

    expected = LocationQueryMessage(Address("$.hello"), metadata={"pending_message": message})
    assert channel.send_called_with_packet == Packet(expected, Address("$.me"), Address("$.discovery"))
