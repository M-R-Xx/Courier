from peewee import Model, CharField, IntegerField, FloatField, ForeignKeyField
from peewee import *  
import datetime
import settings


db = SqliteDatabase(database=f'{settings.DATABASE_PATH}/{settings.DATABASE_NAME}')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    position = CharField(default='')
    login = CharField(default='')
    password = CharField(default='')
    power_level = IntegerField(default=0)

class Order(BaseModel):
    user = ForeignKeyField(User, backref='orders', default=0)
    order_date = DateField(default=datetime.date.today())
    status = CharField(default='')

class Customer(BaseModel):
    name = CharField(default='')
    address = CharField(default='')
    phone = CharField(default='')

class Courier(BaseModel):
    name = CharField(default='')
    vehicle = CharField(default='')
    availability = BooleanField(default=True)

db.create_tables([User, Order, Customer, Courier])