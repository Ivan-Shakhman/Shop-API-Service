from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db.engine import get_db
from db.engine import SessionLocal
from app.routers import categories_router


app = FastAPI()
app.include_router(
    categories_router.router,
    prefix="/categories",
    tags=["categories"]
)


@app.get("/")
async def title(db: Session = Depends(get_db)):
    return {"message": "Welcome in my shop"}
