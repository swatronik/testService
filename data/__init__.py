import sqlite3

from config import SETTINGS


class Connect:
    def __init__(self):
        self.conn = sqlite3.connect(SETTINGS.USER_DB)

    def __enter__(self):
        self.conn.row_factory = sqlite3.Row
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()