import datetime
from peewee import * 
from flask_login import UserMixin 

DATABASE = SqliteDatabase('locations.sqlite')

class User(UserMixin, Model):
    __tableName__ = "users"
    id = IntegerField(primary_key=True)
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    user_pic = CharField()
    
    class meta: 
        database = DATABASE 
        
class Location(Model):
    __tablename__ = "locations"
    id = IntegerField(primary_key=True)
    user_id = ForeignKeyField(User)
    created_at = DateTimeField(default=datetime.datetime.now)
    loc_name = CharField(unique=True)
    street_num = IntegerField(6)
    street_name = CharField()
    apt_unit_num = IntegerField()
    city = CharField()
    State = CharField(2)
    zipcode = IntegerField(5)
    ada = BooleanField()
    unisex = BooleanField()
    open_time = CharField()
    closing_time = CharField()
    Directions = CharField(255)




def initialize(): 
    DATABASE.connect()
    DATABASE.create_tables([User, Location], safe=True)
    print("Tables Created")
    DATABASE.close()
    
    # blah

     