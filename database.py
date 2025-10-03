# engine, LocalSession, Base larni yarating
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import Config

engine = create_engine(Config().DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in Config().DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
