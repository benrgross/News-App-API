from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base

class Interaction(Base):
    __tablename__ = 'interactions'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    news_article_id = Column(Integer, ForeignKey('news_articles.id'))
    interaction_type = Column(String)  # e.g., 'click', 'like'
    interaction_time = Column(DateTime)

    user = relationship("User", back_populates="interactions")
    news_article = relationship("NewsArticle", back_populates="interactions")