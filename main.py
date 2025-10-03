import json
from database import engine, SessionLocal, Base
from models import User, Post, Comment
from crud import create_user, create_post, create_comment

def init_db():
    Base.metadata.create_all(bind=engine)

def load_demo(path="demo_data.json"):
    import os
    if not os.path.exists(path):
        return
    db = SessionLocal()
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for u in data.get("users", []):
        user = create_user(db, u.get("username"), u.get("email"))
        for p in u.get("posts", []):
            post = create_post(db, user.id, p.get("title"), p.get("body"))
            for c in p.get("comments", []):
                create_comment(db, u.get("id", user.id), post.id, c.get("text"))
    db.close()

if __name__ == '__main__':
    init_db()
    load_demo()
    print("DB initialized and demo loaded (if demo_data.json present).")