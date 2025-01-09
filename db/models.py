from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Category(DeclarativeBase):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    name: Mapped[str]
    age_limit: Mapped[int]

