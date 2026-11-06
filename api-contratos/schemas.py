from datetime import date
from enum import Enum

from pydantic import BaseModel, Field, model_validator

class ContractStatus(str, Enum):

    ACTIVE = "active"
    EXPIRED = "expired"
    CANCELED = "canceled"

class CreateContract (BaseModel):
    number: str = Field(min_length=1, max_length=50)
    supplier: str = Field(min_length=1, max_length=100)
    value: float = Field(gt=0)
    start_date: date
    expiration_date: date
    status: ContractStatus = ContractStatus.ACTIVE

    @model_validator(mode="after")
    def dates_validator(self):
        if self.expiration_date < self.start_date:
            raise ValueError("Expiration date cannot be earlier than start date")
        return self