from redcomet.message_handler.actor_manager import ActorManager
from redcomet.message_handler.actor_message import ActorMessage


class MockActorManager(ActorManager):
    def __init__(self):
        self.handle_called_with_message = None

    def handle(self, message: ActorMessage) -> None:
        self.handle_called_with_message = message


class DummyActorMessage(ActorMessage):
    pass
