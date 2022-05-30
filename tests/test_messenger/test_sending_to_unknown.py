from redcomet.messenger import Messenger, Address, Location, Packet
from redcomet.usecase.sending_to_unknown import LocationQueryRequest
from redcomet.usecase.sending_to_unknown.response import LocationQueryResponse
from tests.test_messenger.mock import MockChannel, MockAddressTranslator, MyMessage, MockMessageHandler


def test_should_send_query_message_to_discovery_service_when_address_is_unknown():
    channel = MockChannel()
    messenger = Messenger(Address("$.msg"),
                          handle=lambda _: ...,
                          address_translator=MockAddressTranslator(query_return=None),
                          discovery_location=Location("discovery_node"),
                          channels={Location("discovery_node"): channel})
    message = MyMessage()

    messenger.send(message, Address("$.me"), Address("$.you"))

    expected = LocationQueryRequest(Address("$.you"),
                                    metadata={"pending_packet": Packet(message, Address("$.me"), Address("$.you"))})
    assert channel.send_called_with_packet == Packet(expected, Address("$.msg"), Address("$.discovery"))


def test_should_register_location_when_receiving_query_message_response():
    translator = MockAddressTranslator()
    messenger = Messenger(Address(""),
                          handle=lambda _: ...,
                          address_translator=translator,
                          discovery_location=Location("discovery_node"),
                          channels={Location("your_node"): MockChannel()})

    response = LocationQueryResponse(Address("$.you"), Location("your_node"), metadata={})
    messenger.receive(Packet(response, Address("$.discovery"), Address("$.me")))

    assert translator.register_called_with_parameters == (Address("$.you"), Location("your_node"))


def test_should_not_call_message_handler_when_receiving_query_message_response():
    handler = MockMessageHandler()
    messenger = Messenger(Address(""),
                          handle=handler.handle,
                          address_translator=MockAddressTranslator(),
                          discovery_location=Location(""),
                          channels={})
    packet = Packet(LocationQueryResponse(Address("$.you"), Location("your_node"), metadata={}),
                    sender=Address("$.discovery"),
                    receiver=Address("$.me"))
    messenger.receive(packet)

    assert not handler.is_called


def test_should_send_pending_packet_if_attached_in_metadata():
    channel = MockChannel()
    messenger = Messenger(Address(""),
                          handle=lambda _: ...,
                          address_translator=MockAddressTranslator(),
                          discovery_location=Location("discovery_node"),
                          channels={Location("your_node"): channel})

    pending_packet = Packet(MyMessage(), sender=Address("$.me"), receiver=Address("$.you"))
    response = LocationQueryResponse(Address("$.you"), Location("your_node"),
                                     metadata={"pending_packet": pending_packet})
    messenger.receive(Packet(response, Address("$.discovery"), Address("$.me")))

    assert channel.send_called_with_packet == pending_packet
