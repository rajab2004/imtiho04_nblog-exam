from database import SessionLocal
from main import init_db, load_demo
import crud

def run_tests():
    init_db()
    db = SessionLocal()
    # Create user
    u = crud.create_user(db, "test_user", "test@example.com")
    print("Created user:", u.username, u.id)
    # Create post
    p = crud.create_post(db, u.id, "Hello", "This is a test post")
    print("Created post:", p.title, p.id)
    # Create comment
    c = crud.create_comment(db, u.id, p.id, "Nice post!")
    print("Created comment id:", c.id, "text:", c.text)
    # Get posts
    posts = crud.get_user_posts(db, u.id)
    print("User posts count:", len(posts))
    # Update post
    updated = crud.update_post(db, p.id, title="Updated title")
    print("Updated post title:", updated.title)
    # Delete post
    ok = crud.delete_post(db, p.id)
    print("Deleted post:", ok)
    db.close()

if __name__ == '__main__':
    run_tests()