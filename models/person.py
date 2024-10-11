from typing import List, Union

from fastapi import UploadFile
from pydantic import BaseModel, json


class PersonCreate(BaseModel):
    first_name: Union[str, None]
    second_name: Union[str, None]
    third_name: Union[str, None]
    age: Union[int, None]
    phone: Union[str, None]
    nationality: Union[str, None]

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value


class Person(PersonCreate):
    pass
