from redcomet.messenger import Message, Address, Location


class Packet:
    def __init__(self, message: Message, sender: Address, receiver: Address, sender_location: Location = None):
        self._message = message
        self._sender = sender
        self._receiver = receiver
        self._sender_location = sender_location

    @property
    def message(self) -> Message:
        return self._message

    @property
    def sender(self) -> Address:
        return self._sender

    @property
    def receiver(self) -> Address:
        return self._receiver

    @property
    def sender_location(self) -> Location:
        return self._sender_location

    @sender_location.setter
    def sender_location(self, location: Location):
        self._sender_location = location

    def __eq__(self, other) -> bool:
        if not isinstance(other, Packet):
            return False
        return self._message == other._message and self._sender == other._sender and self._receiver == other._receiver

    def __repr__(self) -> str:
        return f"Packet({self._message!r}, sender={self._sender!r}, receiver={self._receiver!r}, " \
               f"sender_location={self._sender_location!r})"
