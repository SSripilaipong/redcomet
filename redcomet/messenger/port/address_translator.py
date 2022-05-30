from abc import ABC, abstractmethod

from redcomet.messenger.address import Address
from redcomet.messenger.location import Location


class AddressTranslator(ABC):

    @abstractmethod
    def query(self, address: Address) -> Location:
        pass

    @abstractmethod
    def register(self, address: Address, location: Location):
        pass
