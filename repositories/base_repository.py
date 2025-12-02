from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from models.base import Base
from typing import List, Generic, TypeVar

T = TypeVar("T", bound=Base) # This means that we can only use the repository on classes that inherit from Base, ie our database table classes


class BaseRepository(ABC, Generic[T]):
    @abstractmethod
    def get_by_id(self, id: int, session: Session) -> T | None:
        pass

    @abstractmethod
    def get_all(self, session: Session) -> List[T]:
        pass

    @abstractmethod
    def delete(self, entity: T, session: Session) -> bool:
        pass
