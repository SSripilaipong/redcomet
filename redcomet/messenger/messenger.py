from .address import Address
from .message import Message
from .port import AddressTranslator


class Messenger:
    def __init__(self, address_translator: AddressTranslator):
        self._address_translator = address_translator

    def send(self, address: Address, message: Message):
        self._address_translator.query(address)
