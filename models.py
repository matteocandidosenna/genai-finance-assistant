from datetime import date, datetime
from decimal import Decimal

#SQLAlchemy ORM allows us to model and interact with relational databases using Python
from sqlalchemy import CheckConstraint, Date, DateTime, Numeric, String, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(
        primary_key = True
        )

    name: Mapped[str] = mapped_column(
        str(100),
        nullable = False
    )

    account_type: Mapped[str] = mapped_column(
        str(30),
        nullable = False
    )

    opening_balance: Mapped[Decimal] = mapped_column(
        Decimal(12, 2),
        nullable = False,
        server_default = "0.00"
    )

class Transaction(Base):
    __tablename__ = "transactions"

    __table_args__ = ( #we dont want values diferent from income or expense
        CheckConstraint(
            "transaction_type IN ('income', 'expense')",
            name = "ck_transactions_type"
        ),

        CheckConstraint( #no negative values allowed
            "amount > 0",
            name = "ck_transaction_amount_positive"
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key = True
    )

    account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id"),
        nullable = False
    )

    description: Mapped[str] = mapped_column(
        str(300),
        nullable = False
    )

    amount: Mapped[Decimal] = mapped_column(
        Decimal(15,2),
        nullable = False
    )

    transaction_type: Mapped[str] = mapped_column(
        str(50),
        nullable = False
    )

    category: Mapped[str] = mapped_column( #like food, housing, salary, etc...   
        str(100),
        nullable = False
    )

    transaction_date: Mapped[date] = mapped_column(
        Date,
        nullable = False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone = True),
        server_default = func.now(),
        nullable = False
    ) 

