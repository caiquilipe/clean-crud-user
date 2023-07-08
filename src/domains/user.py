from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserModel:
    id: str = None
    first_name: str
    last_name: str
    created_at: datetime
    updated_at: datetime
