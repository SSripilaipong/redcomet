from abc import ABC, abstractmethod

from redcomet.messenger import Message


class Channel(ABC):

    @abstractmethod
    def send(self, message: Message):
        pass
