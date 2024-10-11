from typing import List, Optional

from data import Connect
from models.person import Person, PersonCreate


def create_table():
    """
    Предворительное создание таблиц если их нет
    """

    with Connect() as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS person (
                id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                second_name TEXT NOT NULL,
                third_name TEXT,
                age INTEGER NOT NULL,
                phone TEXT,
                nationality TEXT
            )
        ''')


def get_person(id: int) -> Optional[Person]:
    with Connect() as cursor:
        cursor.execute('''
            SELECT 
                first_name, 
                second_name, 
                third_name, 
                age, 
                phone, 
                nationality
            FROM person
            WHERE id = ?''', (
                str(id)
        ))
        result = dict(cursor.fetchone())

        return None if result is None else Person.parse_obj(result)


def get_all_person() -> List[Person]:
    with Connect() as cursor:
        cursor.execute('''
            SELECT 
                first_name, 
                second_name, 
                third_name, 
                age, 
                phone, 
                nationality
            FROM person'''
        )
        result: List[Person] = []
        for row in cursor.fetchall():
            person = dict(row)
            result.append(Person.parse_obj(person))
        return [] if result is None else result


def add_person(person: Person):
    """
    Добавить человека в таблицу
    :param person: данные пользователя
    """
    with Connect() as cursor:
        cursor.execute('''
            INSERT INTO person (
                first_name, 
                second_name, 
                third_name, 
                age, 
                phone, 
                nationality
            ) VALUES (?, ?, ?, ?, ?, ?)''', (
                person.first_name,
                person.second_name,
                person.third_name,
                person.age,
                person.phone,
                person.nationality
        ))

