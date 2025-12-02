from models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text


class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True)
    rating: Mapped[int] = mapped_column()
    comment: Mapped[str] = mapped_column(Text)

    # Foreign Key to book look at author_id to find a hint
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"))
    # Add relationship
    # One Review belongs to one book = No List
    book: Mapped["Book"] = relationship("Book", back_populates="reviews")  # type: ignore

    def __repr__(self) -> str:
        return f"<Id: {self.id}, Rating: {self.rating}, Comment: {self.comment}>"
