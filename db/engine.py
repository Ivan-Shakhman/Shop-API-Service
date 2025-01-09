from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


DATABASE_URL = "postgresql://username:password@localhost/shop_db"

engine = create_async_engine(DATABASE_URL)
SessionLocal = async_sessionmaker(bind=engine, autoflush=False, autocommit=False)
