from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import Base

class User(Base):
    __tablename__ = "Users"
    __table_args__ = {"schema": "CW2"}

    user_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    comments = relationship("Comment", back_populates="user")

class Trail(Base):
    __tablename__ = "Trails"
    __table_args__ = {"schema": "CW2"}

    trail_id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    location = Column(String(200), nullable=False)

    comments = relationship("Comment", back_populates="trail")

class Comment(Base):
    __tablename__ = "Comments"
    __table_args__ = {"schema": "CW2"}

    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    trail_id = Column(Integer, ForeignKey("CW2.Trails.trail_id"))
    user_id = Column(Integer, ForeignKey("CW2.Users.user_id"))
    comment_text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime)
    is_archived = Column(Boolean, default=False)

    user = relationship("User", back_populates="comments")
    trail = relationship("Trail", back_populates="comments")
