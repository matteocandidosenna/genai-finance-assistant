from datetime import date, datetime
from decimal import Decimal

#SQLAlchemy ORM allows us to model and interact with relational databases using Python
from sqlalchemy import CheckConstraint, Date, DateTime, Numeric, String, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key = True)

    name: Mapped[str] = mapped_column(
        String(100),
        nullable = False
    )

    account_type: Mapped[str] = mapped_column(
        String(30),
        nullable = False
    )

    opening_balance: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable = False,
        server_default = "0.00"
    )

class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(
        primary_key = True
    )

    account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id"),
        nullable = False
    )

    description: Mapped[String] = mapped_column(
        String(300),
        nullable = False
    )