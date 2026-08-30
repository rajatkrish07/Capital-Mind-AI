import uuid
from app.repositories.user_repository import UserRepository
from app.models.models import User
from app.exceptions import UserNotFoundError

class UserService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    # Get user by id
    def get_user_by_id(self, user_id: str) -> User:
        user = self.user_repository.get_user_by_id(user_id)

        if user is None:
            raise UserNotFoundError(user_id)

        return user

    # Get user by email
    def get_user_by_email(self, email: str) -> User:
        user = self.user_repository.get_user_by_email(email)

        if user is None:
            raise UserNotFoundError(email)

        return user

    # Creates user with email
    def create_user(self, email: str) -> User:

        user = User(
            id=f"usr_{str(uuid.uuid4())}",
            email=email
        )

        return self.user_repository.create_user(user)
