from sqlalchemy import select, text
from sqlalchemy.exc import IntegrityError

from app.main import Base, SessionLocal, engine
from app.models.user import User

Base.metadata.create_all(bind=engine)


def ensure_user_id_sequence():
    with engine.begin() as conn:
        conn.execute(text("CREATE SEQUENCE IF NOT EXISTS users_user_id_seq"))
        conn.execute(text("ALTER TABLE users ALTER COLUMN user_id SET DEFAULT nextval('users_user_id_seq')"))
        conn.execute(text(
            "SELECT setval('users_user_id_seq', COALESCE((SELECT MAX(user_id)+1 FROM users), 1), false)"
        ))


ensure_user_id_sequence()


def create_test_user():
    db = SessionLocal()
    try:
        new_user = User(
            username="Anmol",
            email="abc@gmail.com",
            password="123"
        )
        db.add(new_user)
        db.commit()
        print("Created user:", new_user.username)
    except IntegrityError:
        db.rollback()
        print("User already exists or duplicate email/password.")
    finally:
        db.close()


def list_users():
    db = SessionLocal()
    try:
        users = db.execute(select(User)).scalars().all()
        print("Users in database:", len(users))
        for user in users:
            print(f"- {user.user_id}: {user.username} / {user.email}")
    finally:
        db.close()


if __name__ == "__main__":
    create_test_user()
    list_users()
