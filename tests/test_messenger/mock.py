from redcomet.messenger import Address
from redcomet.messenger.location import Location
from redcomet.messenger.port import AddressTranslator


class MockAddressTranslator(AddressTranslator):
    def __init__(self):
        self.query_called_with_address = None

    def query(self, address: Address) -> Location:
        self.query_called_with_address = address
