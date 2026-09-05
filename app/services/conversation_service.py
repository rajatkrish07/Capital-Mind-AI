import uuid
from app.models.models import Conversation
from app.repositories.conversation_repository import ConversationRepository
from app.exceptions import ConversationNotFoundError


class ConversationService:

    def __init__(self, conversation_repository: ConversationRepository):
        self.conversation_repository = conversation_repository

    # Fetches conversation by id
    def get_conversation_by_id(self, conversation_id: str) -> Conversation:
        conversation = self.conversation_repository.get_conversation_by_id(conversation_id)

        if conversation is None:
            raise ConversationNotFoundError(conversation_id)

        return conversation

    # Fetches conversation by title
    def get_conversation_by_title(self, user_id: str, title: str) -> Conversation:
        conversation = self.conversation_repository.get_conversation_by_title(user_id, title)

        if conversation is None:
            raise ConversationNotFoundError(title)

        return conversation

    # Fetches conversation by user
    def get_conversations_by_user(self, user_id: str) -> list[Conversation]:
        conversation = self.conversation_repository.get_conversations_by_user(user_id)

        return conversation

    # Creates conversation
    def create_conversation(self, conversation: Conversation) -> Conversation:

        conversation = Conversation(
            id=f"conv{str(uuid.uuid4())}",
            user_id=conversation.user_id,
            title=conversation.title
        )

        created_conversation = self.conversation_repository.create_conversation(conversation)

        return created_conversation

    # Updates Conversation
    def update_conversation(self, conversation: Conversation, new_title: str) -> Conversation:

        if conversation.title == new_title:
            return conversation

        conversation.title = new_title
        return self.conversation_repository.update_conversation(conversation)

    # Deletes Conversation
    def delete_conversation(self, conversation: Conversation) -> Conversation:
        return self.conversation_repository.delete_conversation(conversation)





