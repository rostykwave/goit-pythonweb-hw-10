from sqlalchemy import String, Date, Text
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from datetime import date
from typing import Optional

class Base(DeclarativeBase):
    pass

class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(50), index=True)
    last_name: Mapped[str] = mapped_column(String(50), index=True)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    phone_number: Mapped[str] = mapped_column(String(20))
    birth_date: Mapped[date] = mapped_column(Date)
    additional_data: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
