from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database.connection import get_db
from app.models.blog_model import Blog
from app.schemas.blog_schema import BlogResponse, BlogBase
from app.models.user_model import User
from app.security.oauth2 import get_current_user

router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)


@router.post("/", response_model=BlogResponse)
def create_post(blog: BlogBase, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    print(current_user)
    blog_dict = blog.model_dump()
    blog_dict["user_id"] = current_user.id
    print("Blog Data", blog_dict)
    blog_db = Blog(**blog_dict)
    db.add(blog_db)
    db.commit()
    db.refresh(blog_db)
    return blog_db

@router.get("/", response_model=List[BlogResponse])
def get_blogs(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Blog).where(Blog.user_id == current_user.id).all()


@router.put("/", response_model=BlogResponse)
def update_blog(blog: BlogResponse, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_blog = db.query(Blog).where(Blog.id == blog.id, Blog.user_id == current_user.id).first()
    if not db_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    for key, value in blog.model_dump(exclude_unset=True).items():
        setattr(db_blog, key, value)
    db.commit()
    db.refresh(db_blog)
    return db_blog


@router.delete("/{blog_id}", status_code=status.HTTP_202_ACCEPTED)
def delete_blog(blog_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_blog = db.query(Blog).where(Blog.id == blog_id, Blog.user_id == current_user.id).first()
    if not db_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    db.delete(db_blog)
    db.commit()
    return {"detail": "Blog deleted successfully"}
    