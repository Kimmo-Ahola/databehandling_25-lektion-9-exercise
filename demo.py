from dataclasses import dataclass
from typing import Any
from models.base import Base
from sqlalchemy.orm import Mapped, mapped_column, MappedAsDataclass
from sqlalchemy import String, Integer

class NormalClass():
    def __init__(self, id, name: str = "") -> None:
        self.id = id
        self.name = name

class SoftDeletionMixin:
    is_deleted: Mapped[bool] = mapped_column(default=False, init=False)

class Demo(MappedAsDataclass, SoftDeletionMixin, Base):
    __tablename__ = "demo"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, init=False)
    first_name: Mapped[str] = mapped_column(String(255))

x = NormalClass(id=1)

# test = Demo(first_name="Kimmo")

# y = NormalClass(id=1, name="Kimmo")
# y_2 = NormalClass(id=1, name="Kimmo")

# x = Test(id=1, name="Kimmo")
# x_2 = Test(id=1, name="Kimmo")

# x.name = "New Name"

# #print(y) # Reference based equality
# print(x) # Value based equality

demo = Demo(first_name="Kimmo")