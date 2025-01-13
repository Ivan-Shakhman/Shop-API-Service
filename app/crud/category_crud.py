from fastapi import HTTPException, Body

import schemas
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


def update_category(
        db: Session,
        category_id: int,
        update_data: schemas.CategoryUpdate = Body(default={})
):
    category = db.query(models.CategoryDB).filter(models.CategoryDB.id == category_id).first()
    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found"
        )

    updated_category = update_data.dict(exclude_unset=True)
    for key, value in updated_category.items():
        setattr(category, key, value)
    db.commit()
    db.refresh(category)
    return category
