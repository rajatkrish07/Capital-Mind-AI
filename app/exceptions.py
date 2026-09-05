class UserNotFoundError(Exception):
    def __init__(self,identifier: str):
        super().__init__(f"User not found: {identifier}")

class ConversationNotFoundError(Exception):
    def __init__(self, identifier: str):
        super().__init__(f"Conversation not found: {identifier}")