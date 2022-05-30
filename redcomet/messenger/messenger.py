from typing import Dict

from .location import Location
from .address import Address
from .message import Message
from .port import Channel, AddressTranslator


class Messenger:
    def __init__(self, address_translator: AddressTranslator, channels: Dict[Location, Channel]):
        self._address_translator = address_translator
        self._channels = channels

    def send(self, address: Address, message: Message):
        location = self._address_translator.query(address)
        if location is not None:
            self._channels[location].send(message)
