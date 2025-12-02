from typing import List
from repositories.base_repository import BaseRepository
from models.author import Author
from sqlalchemy.orm import Session, joinedload


class AuthorRepository(BaseRepository[Author]):
    def get_by_id(
        self, id: int, session: Session, include_deleted: bool = False
    ) -> Author | None:
        try:
            if include_deleted:
                session.query(Author).where(Author.id == id).one()
            else:
                return (
                    session.query(Author)
                    .where(Author.id == id, Author.is_deleted == False)
                    .one()
                )
        except:
            print(f"No author with id {id} was found!")

    def get_all(self, session: Session, include_deleted: bool = False) -> List[Author]:
        if include_deleted:
            return session.query(Author).all()
        else:
            return session.query(Author).where(Author.is_deleted == False).all()

    def get_authors_and_books(self, session: Session) -> List[Author]:
        return (
            session.query(Author)
            .where(Author.is_deleted == False)
            .options(joinedload(Author.books))
            .all()
        )

    def delete(self, entity: Author, session: Session) -> bool:
        try:
            session.delete(entity)
            session.commit()
            return True
        except:
            print("")
            return False
