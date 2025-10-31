from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database.db import Base, engine, SessionLocal
from database.models import Expense
from schema import ExpenseCreate

app = FastAPI()

# Create DB
Base.metadata.create_all(bind=engine)

# Dependency: Open DB connection for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "Backend is running ✅"}


@app.post("/add-expense")
def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    new_expense = Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        payment_mode=expense.payment_mode,
        date=expense.date
    )
    
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    
    return {"message": "Expense added ✅", "data": new_expense}
