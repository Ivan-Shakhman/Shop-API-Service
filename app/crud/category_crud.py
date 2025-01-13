from db import models
from sqlalchemy.orm import Session
from schemas import CategoryCreate


def get_all_categories(db: Session):
    return db.query(models.CategoryDB).all()


def create_category(db: Session, category: CategoryCreate):
    db_category = models.CategoryDB(
        name=category.name,
        age_limit=category.age_limit
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_category(db: Session, category_id: int):
    return (
        db
        .query(models.CategoryDB)
        .filter(models.CategoryDB.id == category_id)
        .first()
        )
