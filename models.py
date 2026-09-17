from datetime import datetime, timezone
import enum
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, DateTime, Enum as SQLAlchemyEnum
from database import Base
from sqlalchemy.orm import relationship

class ExpenseCategory(str, enum.Enum):
    GROCERIES = "Groceries"
    LEISURE = "Leisure"
    ELECTRONICS = "Electronics"
    UTILITIES = "Utilities"
    CLOTHING = "Clothing"
    HEALTH = "Health"
    OTHERS = "Others"
    


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    
    expenses = relationship("Expense", back_populates="owner")
    
class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable = False)
    amount = Column(Float, nullable = False)
    category = Column(SQLAlchemyEnum(ExpenseCategory), nullable=False)
    description = Column(String, nullable=True)
    date = Column(Date, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    owner = relationship("User", back_populates="expenses")