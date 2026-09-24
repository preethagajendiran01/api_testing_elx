from pydantic import BaseModel, RootModel

class PostResponse(BaseModel):
    id: int
    title: str
    body: str
    userId: int

class DeleteResponse(RootModel[dict]):
    pass
