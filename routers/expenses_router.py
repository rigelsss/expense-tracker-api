from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import ExpenseCreate, ExpenseOut, ExpenseUpdate
from models import Expense, User
from database import get_db
from auth import get_current_user
from datetime import date

router = APIRouter(prefix="/expenses", tags=["expenses"])

@router.post("/create", response_model=ExpenseOut)
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_expense = Expense(
        user_id = current_user.id,
        amount = expense.amount,
        category = expense.category,
        description = expense.description,
        date = expense.date
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    
    return new_expense


@router.get("/list", response_model=list[ExpenseOut])
def list_expenses(
    start_date: date | None = None,
    end_date: date | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),    
):
    query = db.query(Expense).filter(Expense.user_id == current_user.id)
    
    if start_date:
        query = query.filter(Expense.date >= start_date)
    if end_date:
        query = query.filter(Expense.date <= end_date)
        
    return query.all()


@router.put("/update/{expense_id}", response_model=ExpenseOut)
def update_expense(
    expense_id: int,
    expense_update: ExpenseUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Despesa não encontrada")
    
    if expense.user_id != current_user.id:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail="Não autorizado a atualizar esta despesa")
    
    update_data = expense_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(expense, field, value)
    
    db.commit()
    db.refresh(expense)

    return expense

@router.delete("/delete/{expense_id}", response_model=dict)
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Despesa não encontrada")
    
    if expense.user_id != current_user.id:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail="Não autorizado a deletar esta despesa")
    
    db.delete(expense)
    db.commit()
    return {"message": "Despesa deletada com sucesso"}