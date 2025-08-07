from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Trail, Comment, User

router = APIRouter()


# ----- TRAILS -----
@router.get("/trails", tags=["Trails"])
def get_trails(db: Session = Depends(get_db)):
    return db.query(Trail).all()


@router.get("/trails/{trail_id}", tags=["Trails"])
def get_trail(trail_id: int, db: Session = Depends(get_db)):
    trail = db.query(Trail).filter(Trail.trail_id == trail_id).first()
    if not trail:
        raise HTTPException(status_code=404, detail="Trail not found")
    return trail


# ----- COMMENTS -----
@router.get("/comments", tags=["Comments"])
def get_comments(db: Session = Depends(get_db)):
    return db.query(Comment).all()


@router.get("/comments/{comment_id}", tags=["Comments"])
def get_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = db.query(Comment).filter(Comment.comment_id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment


@router.post("/comments", tags=["Comments"])
def create_comment(trail_id: int, user_id: int, comment_text: str, db: Session = Depends(get_db)):
    new_comment = Comment(
        trail_id=trail_id,
        user_id=user_id,
        comment_text=comment_text
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


@router.put("/comments/{comment_id}", tags=["Comments"])
def update_comment(comment_id: int, comment_text: str, db: Session = Depends(get_db)):
    comment = db.query(Comment).filter(Comment.comment_id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    
    comment.comment_text = comment_text
    db.commit()
    db.refresh(comment)
    return comment


@router.delete("/comments/{comment_id}", tags=["Comments"])
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = db.query(Comment).filter(Comment.comment_id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    
    db.delete(comment)
    db.commit()
    return {"message": "Comment deleted"}


# ----- USERS -----
@router.get("/users", tags=["Users"])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.get("/users/{user_id}", tags=["Users"])
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
