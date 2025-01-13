from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime


class CategoryBase(BaseModel):
    name: str
    age_limit: int


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class DistributorBase(BaseModel):
    name: str
    country: str


class Distributor(DistributorBase):
    id: int

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str
    price: Decimal
    category_id: int
    distributor_id: int


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class PositionBase(BaseModel):
    name: str
    salary: Decimal


class Position(PositionBase):
    id: int

    class Config:
        orm_mode = True


class PersonalBase(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    position_id: int


class Personal(PersonalBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    created_at: datetime
    user_id: int


class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True


class BasketBase(BaseModel):
    user_id: int


class Basket(BasketBase):
    id: int

    class Config:
        orm_mode = True


class BasketItemBase(BaseModel):
    basket_id: int
    product_id: int
    quantity: int


class BasketItem(BasketItemBase):
    id: int

    class Config:
        orm_mode = True


class OrderItemBase(BaseModel):
    order_id: int
    product_id: int
    quantity: int


class OrderItem(OrderItemBase):
    id: int

    class Config:
        orm_mode = True
