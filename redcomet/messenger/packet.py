from redcomet.messenger import Message, Address


class Packet:
    def __init__(self, message: Message, sender: Address, receiver: Address):
        self._message = message
        self._sender = sender
        self._receiver = receiver

    @property
    def message(self) -> Message:
        return self._message

    @property
    def sender(self) -> Address:
        return self._sender

    @property
    def receiver(self) -> Address:
        return self._receiver

    def __eq__(self, other):
        if not isinstance(other, Packet):
            return False
        return self._message == other._message and self._sender == other._sender and self._receiver == other._receiver
