from app.crud import category_crud
import schemas
from fastapi import HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from db.engine import get_db

router = APIRouter()


@router.get("/", response_model=list[schemas.Category])
async def read_all_categories(db: Session = Depends(get_db)):
    return category_crud.get_all_categories(db)


@router.post("/", response_model=schemas.Category)
async def create_category(
    category: schemas.CategoryCreate,
    db: Session = Depends(get_db)
):
    return category_crud.create_category(db=db, category=category)


@router.get("/{category_id}")
async def get_category_by_id(
        category_id: int,
        db: Session = Depends(get_db)
):
    db_category = category_crud.get_category(category_id=category_id, db=db)
    if not db_category:
        raise HTTPException(status_code=404, detail="category not found!")
    return db_category
