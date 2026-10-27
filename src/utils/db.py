from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
from src.utils.settings import settings

# 1. Engine setup (Aapne shayad aisi hi line likhi hogi)
engine = create_engine(settings.DB_CONNECTION)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# 2. Yeh naya function jodiye jo database se query karke check karega
def check_db_connection():
    try:
        # Ek choti si raw SQL query run karke test karte hain
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("🎉 SUCCESS: Database connected successfully!")
    except Exception as e:
        print(f"❌ ERROR: Database connection failed! Details: {e}")