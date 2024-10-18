from typing import List, Optional

from data import Connect
from models.person import PersonDB, Person
from models.user import UserInDB


def create_table():
    """
    Предворительное создание таблиц если их нет
    """
    with Connect() as cursor:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS persons (
                id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                second_name TEXT NOT NULL,
                third_name TEXT,
                age INTEGER NOT NULL,
                phone TEXT,
                nationality TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL UNIQUE,
                hashed_password TEXT NOT NULL
            )
        ''')
        cursor.fetchone()
    init_data_table()


def init_data_table():
    with Connect() as cursor:
        cursor.execute('''
                    INSERT OR IGNORE INTO users(username, hashed_password) VALUES('admin', '$2b$12$Zkf1ZNvWB/Zl3FRYw3PLIeC/kpq7shaw1NMLLyRRWplcfHlKoQb3C')''' # admin admin
                    )
        cursor.fetchone()


def get_person(id: int) -> Optional[PersonDB]:
    """
    Получить человека по id
    :param id: id человека
    :return: данные человека
    """
    with Connect() as cursor:
        cursor.execute('''
            SELECT 
                id,
                first_name, 
                second_name, 
                third_name, 
                age, 
                phone, 
                nationality
            FROM persons
            WHERE id = ?''', (
                str(id),
        ))
        result = dict(cursor.fetchone())

        return None if result is None else PersonDB.parse_obj(result)


def get_all_person() -> List[PersonDB]:
    """
    Получить всех людей из таблицы
    :return: список всех людей
    """
    with Connect() as cursor:
        cursor.execute('''
            SELECT 
                id,
                first_name, 
                second_name, 
                third_name, 
                age, 
                phone, 
                nationality
            FROM persons'''
        )
        result: List[PersonDB] = []
        for row in cursor.fetchall():
            person = dict(row)
            result.append(PersonDB.parse_obj(person))
        return [] if result is None else result


def add_person(person: Person):
    """
    Добавить человека в таблицу
    :param person: данные человека
    """
    with Connect() as cursor:
        cursor.execute('''
            INSERT INTO persons (
                first_name, 
                second_name, 
                third_name, 
                age, 
                phone, 
                nationality
            ) VALUES (?, ?, ?, ?, ?, ?)
            RETURNING id''', (
                person.first_name,
                person.second_name,
                person.third_name,
                person.age,
                person.phone,
                person.nationality,
        ))
        result = cursor.fetchone()
        return None if result is None else result


def create_user(user: UserInDB):
    """
    Создание пользователя
    :param user: данные пользователя
    :return: id добавленного пользователя
    """
    with Connect() as cursor:
        cursor.execute('''
            INSERT INTO users (
                username, 
                hashed_password
            ) VALUES (?, ?)
            RETURNING id''', (
                user.username,
                user.hashed_password,
        ))
        result = cursor.fetchone()
        return None if result is None else result


def get_user(username: str)-> Optional[UserInDB]:
    """
    Создание пользователя
    :param user: данные пользователя
    :return: id добавленного пользователя
    """
    with Connect() as cursor:
        cursor.execute('''
            SELECT username, hashed_password FROM users
                WHERE username = ?
            ''', (
                username,
        ))
        result = dict(cursor.fetchone())

        return None if result is None else UserInDB.parse_obj(result)


def delete_user(id: int):
    """
    Удаление пользователя
    :param id: id пользователя
    :return: id удаленного пользователя
    """
    with Connect() as cursor:
        cursor.execute('''
            DELETE FROM users
                WHERE id = ?
            RETURNING id''', (
                id,
        ))
        result = cursor.fetchone()
        return None if result is None else result
