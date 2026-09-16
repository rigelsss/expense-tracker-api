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
    
class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable = False)
    amount = Column(Float,nullable = False)