# Packages
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect
from faker import Faker
import random

# Load env
load_dotenv()

# Credentials
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Database engine
db_engine = create_engine(conn_string, echo=False)
fake = Faker()

# Testing Table Names
def get_tables(engine):
    """Get list of tables."""
    inspector = inspect(engine)
    return inspector.get_table_names()

get_tables(db_engine)


