# 로컬
from database import database


# db연결
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()