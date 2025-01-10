import datetime
from decimal import Decimal
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, DateTime


class CategoryDB(DeclarativeBase):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    name: Mapped[str]
    age_limit: Mapped[int]


class DistributorDB(DeclarativeBase):
    __tablename__ = "distributor"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    name: Mapped[str]
    country: Mapped[str]


class ProductDB(DeclarativeBase):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    name: Mapped[str]
    price: Mapped[Decimal]
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("category.id"))
    distributor_id: Mapped[int] = mapped_column(Integer, ForeignKey("distributor.id"))

    category = relationship("CategoryDB")
    distributor = relationship("DistributorDB")


class PositionDB(DeclarativeBase):
    __tablename__ = "position"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    name: Mapped[str]
    salary: Mapped[Decimal]


class PersonalDB(DeclarativeBase):
    __tablename__ = "personal"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False, index=True)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    position_id: Mapped[int] = mapped_column(Integer, ForeignKey("position.id"), nullable=False)

    position = relationship("PositionDB")


class UserDB(DeclarativeBase):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str]
    last_name: Mapped[str]


class OrderDB(DeclarativeBase):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    created_at: Mapped[str] = mapped_column(DateTime, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    user = relationship("UserDB")


class BasketDB(DeclarativeBase):
    __tablename__ = "basket"
    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    user = relationship("UserDB")


class BasketItemDB(DeclarativeBase):
    __tablename__ = "basket_item"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    basket_id: Mapped[int] = mapped_column(ForeignKey("basket.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    quantity: Mapped[int] = mapped_column(nullable=False)

    basket = relationship("BasketDB")
    product = relationship("ProductDB")


class OrderItemDB(DeclarativeBase):
    __tablename__ = "order_item"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    quantity: Mapped[int] = mapped_column(nullable=False)

    basket = relationship("OrderDB")
    product = relationship("ProductDB")
