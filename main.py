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
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))

    # Add relationships
    # Many-to-one: Many books belong to one author
    
    # One-to-many: One book can have many reviews
    

class Review(Base):
    __tablename__ = 'reviews'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    rating: Mapped[int] = mapped_column()
    comment: Mapped[str] = mapped_column(Text)

    # Foreign Key to book look at author_id to find a hint

    # Add relationship
    # Many-to-one: Many reviews belong to one book
    
def get_author(id: int, session: Session):
    """
    Fetch the author.
    Display the books using lazy loading with a relation
    """
    pass

def get_books_for_author(author_id: int, session: Session):
    """
    Fetch the author and all books for the author.
    Use joinedload or an explicit .join() query
    """
    pass

def get_reviews_for_book(book_id: int, session: Session):
    """
    Fetch all reviews for a book.
    Use lazy loading, joinedload or explicit join() query
    """
    pass

# Create tables
if __name__ == '__main__':
    engine = create_engine(url=mysql_url)

    My_Session = sessionmaker(engine)

    with My_Session() as session:
        Seeding.seed_database(session)

    all_authors = session.query(Author).all()

    print("Här är alla författare i databasen: ")

    for author in all_authors:
        print(author)

    user_choice = int(input("Vilken författares information vill du se? Ange id: "))

    """
    Implementera metoderna nedan.
    Använd user_choice eller liknande metod för att få ett id.
    Läs i metoderna vad som ska finnas i dem.
    """

    # author_and_books = get_author_and_books()

    # author = get_author()

    # reviews = reviews_for_book()