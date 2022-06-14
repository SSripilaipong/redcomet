from redcomet.message_handler.message_handler import MessageHandler
from tests.test_message_handler.mock import MockActorManager, DummyActorMessage


def test_should_pass_actor_message_to_actor_manager():
    my_message = DummyActorMessage()
    actor_manager = MockActorManager()
    handler = MessageHandler(actor_manager=actor_manager)

    handler.handle(my_message)

    assert actor_manager.handle_called_with_message == my_message
