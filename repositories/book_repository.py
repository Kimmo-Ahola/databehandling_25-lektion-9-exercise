from repositories.base_repository import BaseRepository
from models.book import Book
from sqlalchemy.orm import Session
from typing import List


class BookRepository(BaseRepository[Book]):
    def get_by_id(self, id: int, session: Session) -> Book | None:
        try:
            return session.query(Book).where(Book.id == id).one()
        except:
            print(f"No book with id {id} was found!")

    def get_all(self, session: Session) -> List[Book]:
        return session.query(Book).all()
