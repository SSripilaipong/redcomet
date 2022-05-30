from redcomet.messenger import Location, Messenger, Address, Packet
from tests.test_messenger.mock import MockAddressTranslator, MyMessage, MockMessageHandler


def test_should_call_handler_function_with_received_packet():
    handler = MockMessageHandler()
    messenger = Messenger(Address(""), Location(""),
                          handle=handler.handle,
                          address_translator=MockAddressTranslator(),
                          discovery_location=Location(""),
                          channels={})
    packet = Packet(MyMessage(), Address("$.you"), Address(""))

    messenger.receive(packet)

    assert handler.called_with_packet == packet
