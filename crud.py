from sqlalchemy.orm import Session
from models import User, Post, Comment
from datetime import datetime

def create_user(db: Session, username: str, email: str = None):
    user = User(username=username, email=email, created_at=datetime.utcnow())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_post(db: Session, user_id: int, title: str, body: str = None):
    post = Post(user_id=user_id, title=title, body=body, created_at=datetime.utcnow())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def create_comment(db: Session, user_id: int, post_id: int, text: str):
    comment = Comment(user_id=user_id, post_id=post_id, text=text, created_at=datetime.utcnow())
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

def update_post(db: Session, post_id: int, title: str = None, body: str = None):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        return None
    if title is not None:
        post.title = title
    if body is not None:
        post.body = body
    db.commit()
    db.refresh(post)
    return post

def get_user_posts(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()

def get_post_comments(db: Session, post_id: int):
    return db.query(Comment).filter(Comment.post_id == post_id).all()

def delete_post(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        return False
    db.delete(post)
    db.commit()
    return True

