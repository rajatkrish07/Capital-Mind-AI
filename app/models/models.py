from __future__ import annotations
from datetime import datetime, timezone
from app.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import DateTime, String, ForeignKey, Text

# User ORM
class User(Base):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(
        String(50),
        primary_key=True
    )
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda:datetime.now(timezone.utc)
    )
    conversations: Mapped[list[Conversation]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

# Conversations ORM
class Conversation(Base):
    __tablename__ = "conversations"
    id: Mapped[str] = mapped_column(
        String(50),
        primary_key=True
    )
    user_id: Mapped[str] = mapped_column(
        String(50),
        ForeignKey("users.id"),
        nullable=False
    )
    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda:datetime.now(timezone.utc)
    )

    user: Mapped[User] = relationship(
        back_populates="conversations"
    )

    messages: Mapped[list[Message]] = relationship(
        back_populates="conversation",
        cascade = "all, delete-orphan"
    )

# Message ORM
class Message(Base):
    __tablename__ = "messages"
    id: Mapped[str] = mapped_column(
        String(50),
        primary_key=True
    )
    conversation_id: Mapped[str] = mapped_column(
        String(50),
        ForeignKey("conversations.id"),
        nullable=False
    )
    role: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda:datetime.now(timezone.utc)
    )
    conversation: Mapped[Conversation] = relationship(
        back_populates="messages"
    )
