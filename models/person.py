from typing import List, Union

from fastapi import UploadFile
from pydantic import BaseModel, json


class Person(BaseModel):
    first_name: Union[str, None] = None
    second_name: Union[str, None] = None
    third_name: Union[str, None] = None
    age: Union[int, None] = None
    phone: Union[str, None] = None
    nationality: Union[str, None] = None

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class PersonDB(Person):
    id: Union[int, None]
