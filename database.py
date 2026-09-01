from sqlalchemy import create_engine, text

DATABASE_URL = ("postgresql+psycopg://"
"finance_user:finance_password@localhost:5433/finance_db")

engine = create_engine(DATABASE_URL)

def test_connection():
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_database(), current_user"))
        database_name, user_name = result.one()

        print("Well Succeeded Connection!")
        print(f"Databse: {database_name}")
        print(f"User: {user_name}")


if __name__ == "__main__":
    test_connection()