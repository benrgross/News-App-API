from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .core.config import settings
from .models.base import Base

engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)