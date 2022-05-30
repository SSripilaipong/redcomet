from abc import ABC, abstractmethod

from redcomet.messenger import Message, Address


class Channel(ABC):

    @abstractmethod
    def send(self, address: Address, message: Message):
        pass
