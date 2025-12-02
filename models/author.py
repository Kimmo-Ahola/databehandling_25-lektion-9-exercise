from models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import List


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    is_deleted: Mapped[bool] = mapped_column(default=False)
    # Add relationship
    # One-to-many: One author can write many books
    books: Mapped[List["Book"]] = relationship("Book", back_populates="author")  # type: ignore

    def __repr__(self) -> str:
        return f"<Id: {self.id}, Name: {self.name}, Is Deleted: {self.is_deleted}>"
