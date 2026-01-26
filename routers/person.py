from typing import List

from fastapi import APIRouter, HTTPException

import models
from data import database
from models.person import Person, PersonDB

router = APIRouter()


@router.get("/get", response_model=PersonDB)
async def get_person(id: int):
    person = database.get_person(id)
    if person is None:
        raise HTTPException(status_code=404, detail="Не удалось найти person по id")
    return person


@router.get("/get-all", response_model=List[PersonDB])
async def get_all_person():
    return database.get_all_person()


@router.post("/add")
async def add_person(new_person: Person):
    return database.add_person(new_person)


@router.delete("/delete")
async def delete_person(id: int):
    return database.delete_person(id)


@router.put("/update")
async def update_person(id: int, person: Person):
    return database.update_person(id, person)
