from pydantic import BaseModel

class PostPayload(BaseModel):
    title: str
    body: str
    userId: int

VALID_POST_PAYLOAD = PostPayload(title="Test Post", body="This is a test post", userId=1)
ANOTHER_VALID_POST_PAYLOAD = PostPayload(title="Another Test Post", body="Another body", userId=2)
UPDATE_POST_PAYLOAD = {"title": "Updated Post", "body": "Updated body", "userId": 1}
