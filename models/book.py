from models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from typing import List


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))

    # Foreign Key to Author
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))

    # Add relationships
    # One book belongs to one author = No list
    author: Mapped["Author"] = relationship("Author", back_populates="books")  # type: ignore

    # One book can have many reviews = List
    reviews: Mapped[List["Review"]] = relationship("Review", back_populates="book")  # type: ignore

    def __repr__(self) -> str:
        return f"< Id: {self.id}, Title: {self.title}>"
