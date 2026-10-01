from pydantic import BaseModel
from models import ExpenseCategory
import datetime
import enum 

class UserCreate(BaseModel):
    username: str
    password: str
    
class UserOut(BaseModel):
    id: int
    username: str
    
    model_config = {"from_attributes": True}
    
class ExpenseCreate(BaseModel):
    amount: float
    category: ExpenseCategory
    description: str | None = None
    date: datetime.date

class ExpenseUpdate(BaseModel):
    amount: float | None = None
    category: ExpenseCategory | None = None
    description: str | None = None
    date: datetime.date | None = None
    
class ExpenseOut(BaseModel):
    id: int
    user_id: int
    amount: float
    category: ExpenseCategory
    description: str | None = None
    date: datetime.date
    
    model_config = {"from_attributes": True}

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    
class UserLogin(BaseModel):
    username: str
    password: str
    
class ExpensePeriod(str, enum.Enum):
    WEEK = "week"
    MONTH = "month"
    THREE_MONTHS = "3months"
    
