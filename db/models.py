from decimal import Decimal
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey


class Category(DeclarativeBase):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    name: Mapped[str]
    age_limit: Mapped[int]


class Distributor(DeclarativeBase):
    __tablename__ = "distributor"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    name: Mapped[str]
    country: Mapped[str]


class Product(DeclarativeBase):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    name: Mapped[str]
    price: Mapped[Decimal]
    rel_category_id: Mapped[int] = mapped_column(Integer, ForeignKey("category.id"))
    rel_distributor_id: Mapped[int] = mapped_column(Integer, ForeignKey("distributor.id"))

    rel_category = relationship("category")
    rel_distributor = relationship("distributor")
