from sqlalchemy import Column, Integer, String, Text, DateTime
from .base import Base

class NewsArticle(Base):
    __tablename__ = 'news_articles'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    published_date = Column(DateTime)
    source = Column(String)
    url = Column(String, unique=True, index=True)
    image_url = Column(String)
    interactions = relationship("Interaction", back_populates="news_article")