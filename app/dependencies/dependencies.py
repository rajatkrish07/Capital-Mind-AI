from collections.abc import Generator
from sqlalchemy.orm import Session
from app.core.database import SessionLocal

# Yields DB session
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

# Resolving user
def get_current_user() -> str:
    return "dev-user-001"