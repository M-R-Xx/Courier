from pydantic import BaseModel
from typing import Optional
import datetime

class ModifyBaseModel(BaseModel):
    id: Optional[int] = 0


class ChangePassword(BaseModel):
    password: str


class LoginData(BaseModel):
    login: str
    password: str

class User(ModifyBaseModel):
    position: str = ''
    login: str = ''
    password: str = ''
    power_level: int = 0

class Order(ModifyBaseModel):
    user: int = 0
    order_date: str = ''
    status: str = ''

class Customer(BaseModel):
    name: str = ''
    address: str = ''
    phone: str = ''

class Courier(BaseModel):
    name: str = ''
    vehicle: str = ''
    availability: bool = True