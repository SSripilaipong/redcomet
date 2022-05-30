from contextlib import suppress
from typing import Dict, Callable, Any

from .packet import Packet
from .location import Location
from .address import Address
from .message import Message
from .port import Channel, AddressTranslator
from ..usecase.discovery import LocationQueryMessage


class Messenger:
    def __init__(self, address: Address, handle: Callable[[Packet], Any], address_translator: AddressTranslator,
                 discovery_location: Location, channels: Dict[Location, Channel]):
        self._address = address
        self._handle = handle
        self._address_translator = address_translator
        self._discovery_location = discovery_location
        self._channels = channels

    def send(self, address: Address, message: Message):
        location = self._address_translator.query(address)
        if location is not None:
            with suppress(BaseException):
                self._channels[location].send(Packet(message, self._address, address))
            return

        query_message = LocationQueryMessage(address, metadata={"pending_message": message})
        self._channels[self._discovery_location].send(Packet(query_message, self._address, Address("$.discovery")))

    def receive(self, packet: Packet):
        self._handle(packet)
