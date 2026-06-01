from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.response import APIResponse
from app.database.connection import get_db
from app.models.user import User
from app.schemas.user import CreateUser, LoginUser
from app.services.auth import hash_password, verify_password, create_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup")
def signup(user: CreateUser, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == user.username).first()

    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(
        username=user.username,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()

    return APIResponse(
        success=True,
        message="user created"
        
    )

@router.post("/login")
def login(user: LoginUser, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()

    if not db_user :
        raise HTTPException(status_code=401, detail="Invalid username")
    elif  not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid password")
    

    token = create_token({"sub": db_user.username})
    
    return {"access_token": token}