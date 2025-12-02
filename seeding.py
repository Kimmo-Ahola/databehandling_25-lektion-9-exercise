from sqlalchemy.orm import Session
from models.author import Author
from models.book import Book
from models.review import Review


class Seeding:

    @staticmethod
    def seed_database(session: Session):
        count = session.query(Author).count()

        if count == 0:
            author = Author(name="JRR Tolkien")
            author_2 = Author(name="JK Rowling")

            author.books = [
                Book(
                    title="The hobbit", reviews=[Review(rating=2, comment="Good book!")]
                ),
                Book(title="Lord of the Rings"),
            ]
            author_2.books = [Book(title="Harry Potter")]

            session.add(author)
            session.add(author_2)
            session.commit()
