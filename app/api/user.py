from fastapi import APIRouter
from app.models.user import *
from database import get_session
from sqlmodel import select,Session
from fastapi import Depends
from typing import Optional
import logging
from fastapi import HTTPException,Query

router = APIRouter(tags=["user"],prefix="/user")

@router.get("/", response_model=list[UserRead])
def read_users(session: Session = Depends(get_session),user_id:Optional[int]=Query(None)):
    """
    Get all users
    """
    try:
        if user_id:
            users = session.get(User, user_id)
            if not users:
                raise HTTPException(status_code=404, detail="User not found")
            return [users]
        else:
            return session.exec(select(User)).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    

@router.post("/",response_model=UserRead)
def create_user(user:UserCreate,session:Session=Depends(get_session)):    
    try:
        db_user = User.model_validate(user)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user
    except Exception as e:
        session.rollback()
        print(e,"Error*********************")
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/{user_id}",response_model=UserRead)
def update_user(user_id:int,user:UserCreate,session:Session=Depends(get_session)):
    try:
        db_user=session.get(User,user_id)
        if not db_user:
            raise HTTPException(status_code=404,detail="User not found")    
        db_user.model_dump(exclude_unset=True)
        session.commit()
        session.refresh(db_user)
        return db_user
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{user_id}")
def delete_user(user_id:int,session:Session=Depends(get_session)):
    user=session.get(User,user_id)
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    session.delete(user)
    session.commit()
    return {"message":"User deleted successfully"}
    
