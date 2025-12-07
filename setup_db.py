import sys
from sqlalchemy.exc import SQLAlchemyError

try:
    from app import engine, Base
except Exception as exc:
    print(f"Failed to import app context: {exc}")
    sys.exit(1)


def main():
    try:
        # test connection
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        Base.metadata.create_all(bind=engine)
        print("Database tables created/ensured successfully.")
    except SQLAlchemyError as exc:
        print(f"SQLAlchemy error: {exc}")
        sys.exit(1)
    except Exception as exc:
        print(f"Unexpected error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()

