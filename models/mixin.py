from sqlalchemy.orm import Mapped, mapped_column


class SoftDeletionMixin:
    is_deleted: Mapped[bool] = mapped_column(default=False)
