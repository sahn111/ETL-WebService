import os
from sqlalchemy import create_engine

connection_url = os.getenv("CONNECTION_URL")
sqlalchemy_engine = create_engine(connection_url)
