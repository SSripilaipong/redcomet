from redcomet.message_handler import ActorMessage
from redcomet.message_handler.actor_manager import ActorManager
from redcomet.messenger import Message


class MessageHandler:
    def __init__(self, actor_manager: ActorManager):
        self._actor_manager = actor_manager

    def handle(self, message: Message) -> None:
        if isinstance(message, ActorMessage):
            self._actor_manager.handle(message)
