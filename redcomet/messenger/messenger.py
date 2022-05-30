from contextlib import suppress
from typing import Dict, Callable, Any

from .packet import Packet
from .location import Location
from .address import Address
from .message import Message
from .port import Channel, AddressTranslator
from ..usecase.sending_to_unknown import LocationQueryRequest, LocationQueryResponse


class Messenger:
    def __init__(self, address: Address, handle: Callable[[Packet], Any], address_translator: AddressTranslator,
                 discovery_location: Location, channels: Dict[Location, Channel]):
        self._address = address
        self._handle = handle
        self._address_translator = address_translator
        self._discovery_location = discovery_location
        self._channels = channels

    def send(self, message: Message, sender: Address, receiver: Address):
        packet = Packet(message, sender, receiver)
        location = self._address_translator.query(receiver)

        if location is not None:
            with suppress(BaseException):
                self._channels[location].send(packet)
            return

        query_message = LocationQueryRequest(receiver, metadata={"pending_packet": packet})
        self._channels[self._discovery_location].send(Packet(query_message, self._address, Address("$.discovery")))

    def receive(self, packet: Packet):
        message = packet.message
        if isinstance(message, LocationQueryResponse):
            self._address_translator.register(message.address, message.location)
            pending_packet = message.metadata.get("pending_packet", None)
            if pending_packet is not None:
                self._channels[message.location].send(pending_packet)
        else:
            self._handle(packet)
