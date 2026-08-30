from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.models import User
from sqlalchemy.exc import IntegrityError

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    # Fetches user by id
    def get_user_by_id(self, user_id) -> User | None:
        stmt = select(User).where(User.id == user_id)
        execute = self.db.execute(stmt)
        result = execute.scalars().first()
        return result

    # Fetches user by email
    def get_user_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        execute = self.db.execute(stmt)
        result = execute.scalars().first()
        return result

    # Creates user
    def create_user(self, user: User) -> User:
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user

        except IntegrityError:
            self.db.rollback()
            raise

    # Updates user
    def update_user(self, user: User) -> User:
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user

        except IntegrityError:
            self.db.rollback()
            raise

    # Deletes user
    def delete_user(self, user: User) -> User:
        try:
            self.db.delete(user)
            self.db.commit()
            return user

        except IntegrityError:
            self.db.rollback()
            raise