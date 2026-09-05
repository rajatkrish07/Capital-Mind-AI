from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import and_, select
from app.models.models import Conversation
from collections.abc import Sequence

class ConversationRepository:
    def __init__(self, db: Session):
        self.db = db

    # Creates new conversation
    def create_conversation(self, conversation: Conversation) -> Conversation:
        try:
            self.db.add(conversation)
            self.db.commit()
            self.db.refresh(conversation)

            return conversation

        except IntegrityError:
            self.db.rollback()
            raise

    # Fetch conversations by id
    def get_conversation_by_id(self, conversation_id: str) -> Conversation | None:
        stmt = select(Conversation).where(Conversation.id == conversation_id)
        execute = self.db.execute(stmt)
        result = execute.scalars().first()
        return result

    # Fetch conversations by title
    def get_conversation_by_title(self, user_id: str, title: str) -> Conversation | None:
        stmt = select(Conversation).where(
            and_(
                Conversation.user_id == user_id,
        Conversation.title == title
            )
        )
        execute = self.db.execute(stmt)
        result = execute.scalars().first()
        return result

    # Fetch conversations by user
    def get_conversations_by_user(self, user_id: str) -> Sequence[Conversation]:
        stmt = select(Conversation).where(
            Conversation.user_id == user_id
        ).order_by(
            Conversation.created_at.desc()
        )
        execute = self.db.execute(stmt)
        result = execute.scalars().all()
        return result

    # Update conversation
    def update_conversation(self, conversation: Conversation) -> Conversation:
        try:
            self.db.add(conversation)
            self.db.commit()
            self.db.refresh(conversation)

            return conversation

        except IntegrityError:
            self.db.rollback()
            raise

    # Deletes Conversation
    def delete_conversation(self, conversation: Conversation) -> Conversation:
        try:
            self.db.delete(conversation)
            self.db.commit()
            return conversation

        except IntegrityError:
            self.db.rollback()
            raise

