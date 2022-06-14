from abc import ABC, abstractmethod

from redcomet.message_handler.actor_message import ActorMessage


class ActorManager(ABC):

    @abstractmethod
    def handle(self, message: ActorMessage) -> None:
        pass
