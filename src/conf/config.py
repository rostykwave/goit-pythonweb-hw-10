import os

class Config:
    DB_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql+asyncpg://username:password@localhost/contacts_db"
)

config = Config