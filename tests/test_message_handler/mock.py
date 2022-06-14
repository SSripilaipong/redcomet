from redcomet.message_handler import ActorManager, ActorMessage, SystemMessage


class MockActorManager(ActorManager):
    def __init__(self):
        self.handle_is_called = False
        self.handle_called_with_message = None

    def handle(self, message: ActorMessage) -> None:
        self.handle_is_called = True
        self.handle_called_with_message = message


class DummyActorMessage(ActorMessage):
    pass


class DummySystemMessage(SystemMessage):
    pass
