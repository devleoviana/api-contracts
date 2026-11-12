from datetime import date

from sqlalchemy import Date, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class Contract(Base):
    __tablename__ = "contracts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    numero: Mapped[str] = mapped_column(String(50), unique=True)
    fornecedor: Mapped[str] = mapped_column(String(100))
    valor: Mapped[float] = mapped_column(Float)
    data_inicio: Mapped[date] = mapped_column(Date)
    data_vencimento: Mapped[date] = mapped_column(Date)
    status: Mapped[str] = mapped_column(String(20), default="active")