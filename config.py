from functools import lru_cache


class Config:
    USER_DB: str = 'data\\database.db'
    PORT: int = 8093


@lru_cache()
def get_config():
    return Config()


SETTINGS = get_config()