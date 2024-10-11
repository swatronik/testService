from typing import List

from fastapi import APIRouter, HTTPException

import models
from data import database
from models.person import Person

router = APIRouter()


@router.get("/get", response_model=Person)
async def get_person(id: int):
    person = database.get_person(id)
    if person is None:
        raise HTTPException(status_code=404, detail="Не удалось найти person по id")
    return person


@router.get("/get-all", response_model=List[Person])
async def get_all_person():
    return database.get_all_person()


@router.post("/add")
async def add_person(new_person: Person):
    database.add_person(new_person)
