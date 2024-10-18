import json
from typing import Union

from pydantic import BaseModel


class User(BaseModel):
    username: Union[str, None]

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class UserInDB(User):
    hashed_password: Union[str, None]
