from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey, create_engine
from typing import List

mysql_url = "mysql+pymysql://user:user123@localhost:3306/delete_me_2"

class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__ = 'authors'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    
    # One-to-many: One author can write many books
    books: Mapped[List["Book"]] = relationship(back_populates='author')

class Book(Base):
    __tablename__ = 'books'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    author_id: Mapped[int] = mapped_column(ForeignKey('authors.id'))
    
    # Many-to-one: Many books belong to one author
    author: Mapped["Author"] = relationship(back_populates='books')
    
    # One-to-many: One book can have many reviews
    reviews: Mapped[List["Review"]] = relationship(back_populates='book')

class Review(Base):
    __tablename__ = 'reviews'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    rating: Mapped[int] = mapped_column()
    comment: Mapped[str] = mapped_column(Text)
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id'))
    
    # Many-to-one: Many reviews belong to one book
    book: Mapped["Book"] = relationship(back_populates='reviews')

# Create tables
if __name__ == '__main__':
    engine = create_engine(url=mysql_url)