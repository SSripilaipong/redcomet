from abc import ABC, abstractmethod

from redcomet.messenger import Packet


class Channel(ABC):

    @abstractmethod
    def send(self, packet: Packet):
        pass
