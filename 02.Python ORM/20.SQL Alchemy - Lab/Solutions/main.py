import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
load_dotenv()

from sqlalchemy import create_engine

DATABASE_URL = f'postgresql+psycopg2://{os.environ["DB_USER_"]}:{os.environ["DB_PASSWORD_"]}@{os.environ["DB_HOST"]}/{os.environ["DB_NAME"]}'
engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)

Session = sessionmaker(bind=engine)







