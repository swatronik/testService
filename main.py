import logging

import uvicorn
from fastapi import FastAPI

from config import SETTINGS
from data import database
from routers import person

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.WARNING)
logger = logging.getLogger(__name__)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    database.create_table()

    def create_app() -> FastAPI:
        current_app = FastAPI(title="Сервис", description="Сервис для проверки запросов", version="1.0.0")
        current_app.include_router(person.router, prefix="/api/person")
        return current_app

    app = create_app()

    webserver = uvicorn.Server(config=uvicorn.Config(app=app, port=SETTINGS.PORT, use_colors=False, host="0.0.0.0"))
    webserver.run()
