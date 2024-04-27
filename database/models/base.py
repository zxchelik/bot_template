from datetime import datetime
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(AsyncAttrs, DeclarativeBase):
    created: Mapped[Optional[datetime]] = mapped_column(default=datetime.now)
    updated: Mapped[Optional[datetime]] = mapped_column(default=datetime.now, onupdate=datetime.now)
