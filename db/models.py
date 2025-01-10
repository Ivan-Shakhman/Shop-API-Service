import datetime
from decimal import Decimal
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, DateTime


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
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("category.id"))
    distributor_id: Mapped[int] = mapped_column(Integer, ForeignKey("distributor.id"))

    category = relationship("Category")
    distributor = relationship("Distributor")


class Position(DeclarativeBase):
    __tablename__ = "position"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    name: Mapped[str]
    salary: Mapped[Decimal]


class Personal(DeclarativeBase):
    __tablename__ = "personal"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False, index=True)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    position_id: Mapped[int] = mapped_column(Integer, ForeignKey("position.id"), nullable=False)

    position = relationship("Position")


class User(DeclarativeBase):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str]
    last_name: Mapped[str]


class Order(DeclarativeBase):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    created_at: Mapped[str] = mapped_column(DateTime, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    user = relationship("User")


class Basket(DeclarativeBase):
    __tablename__ = "basket"
    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    user = relationship("User")


class BasketItem(DeclarativeBase):
    __tablename__ = "basket_item"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    basket_id: Mapped[int] = mapped_column(ForeignKey("basket.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    quantity: Mapped[int] = mapped_column(nullable=False)

    basket = relationship("Basket")
    product = relationship("Product")


class OrderItem(DeclarativeBase):
    __tablename__ = "order_item"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    quantity: Mapped[int] = mapped_column(nullable=False)

    basket = relationship("Order")
    product = relationship("Product")
