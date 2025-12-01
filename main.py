from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker, Session
from sqlalchemy import String, Text, ForeignKey, create_engine
from typing import List
from seeding import Seeding
mysql_url = "mysql+pymysql://user:user123@localhost:3306/delete_me_2"

class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__ = 'authors'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    
    # Add relationship
    # One-to-many: One author can write many books

class Book(Base):
    __tablename__ = 'books'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    
    # Foreign Key to Author
    

    # Add relationships
    # Many-to-one: Many books belong to one author
    
    # One-to-many: One book can have many reviews
    

class Review(Base):
    __tablename__ = 'reviews'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    rating: Mapped[int] = mapped_column()
    comment: Mapped[str] = mapped_column(Text)

    # Foreign Key to book
    

    # Add relationship
    # Many-to-one: Many reviews belong to one book
    
def get_author(id: int, session: Session):
    pass

def get_author_and_books(id: int, session: Session):
    pass

def get_reviews_for_book(book_id: int, session: Session):
    pass

# Create tables
if __name__ == '__main__':
    engine = create_engine(url=mysql_url)

    My_Session = sessionmaker(engine)

    with My_Session() as session:
        Seeding.seed_database(session)


    """
    After the seeding is done:
        Write a query that fetches all books a specific author has written.
    """

    all_authors = session.query(Author).all()

    print("Här är alla författare i databasen: ")

    for author in all_authors:
        print(author)

    choice = input("Vilken författares information vill du se? Ange id: ")

    """
    i get_author_and_books() hämtar ni endast vald author via session.query och gör en explicit join för att få med böckerna

    i get_author hämtar ni endast vald author via session.query och sedan använder ni lazy loading med relation för att printa böckerna
    """

    author_and_books = get_author_and_books()

    author = get_author()


    """
    i reviews_for_book() hämtar ni recensionerna som tillhör en bok. Ni väljer själva om ni använder en explicit join eller inte.
    """

    reviews = reviews_for_book()