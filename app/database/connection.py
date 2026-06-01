from app.database.database import SessionLocal,Base,engine

def db_init():
    Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()