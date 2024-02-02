from pydantic import BaseModel
from typing import List, Optional
from ..models.profile import Profile


class User(BaseModel):
    id: Optional[str] = None
    email: str
    profiles: List[Profile] = []