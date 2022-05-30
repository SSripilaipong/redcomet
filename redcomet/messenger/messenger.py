from contextlib import suppress
from typing import Dict

from .location import Location
from .address import Address
from .message import Message
from .port import Channel, AddressTranslator
from ..usecase.discovery import LocationQueryMessage


class Messenger:
    def __init__(self, address_translator: AddressTranslator, discovery_location: Location,
                 channels: Dict[Location, Channel]):
        self._address_translator = address_translator
        self._discovery_location = discovery_location
        self._channels = channels

    def send(self, address: Address, message: Message):
        location = self._address_translator.query(address)
        if location is not None:
            with suppress(BaseException):
                self._channels[location].send(address, message)
            return

        query_message = LocationQueryMessage(address, metadata={"pending_message": message})
        self._channels[self._discovery_location].send(Address("$.discovery"), query_message)
