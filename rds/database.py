from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

ip=os.getenv("ip")
username=os.getenv("username")
pw=os.getenv("pw")
db=os.getenv("db")

SQLALCHEMY_DATABASE_URL = ("mysql+pymysql://{username}:{pw}@{ip}:3306/{db}?charset=utf8mb4"
                           .format(username='admin', pw='qweasdzxc7381?!', ip='inha-001-rds.ctgiwqznznut.us-east-2.rds.amazonaws.com', db='inha_001_portal'))

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
