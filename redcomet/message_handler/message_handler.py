from redcomet.message_handler.actor_manager import ActorManager
from redcomet.message_handler.actor_message import ActorMessage


class MessageHandler:
    def __init__(self, actor_manager: ActorManager):
        self._actor_manager = actor_manager

    def handle(self, message: ActorMessage) -> None:
        self._actor_manager.handle(message)
