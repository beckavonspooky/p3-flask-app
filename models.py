from peewee import * 
from flask_login import UserMixin 
import os

from playhouse.db_url import connect

DATABASE= connect(os.environ.get('DATABASE_URL'))

# DATABASE = SqliteDatabase('locations.sqlite')

class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    
    class Meta: 
        database = DATABASE 
        
class Location(Model):
    user_id = ForeignKeyField(User)
    loc_name = CharField(unique=True)
    address = CharField(null=False)
    
    # street_name = CharField(Null=True)
    # apt_unit_num = IntegerField(Null=True)
    # city = CharField(Null=True)
    # state = CharField(2, Null=True)
    # zipcode = IntegerField(5, Null=True)
    # ada = BooleanField(Null=True)
    # unisex = BooleanField(Null=True)
    # open_time = CharField(Null=True)
    # closing_time = CharField(Null=True)
    # directions = CharField(255, Null=True)
    
    class Meta: 
        database = DATABASE 

def initialize(): 
    DATABASE.connect()
    DATABASE.create_tables([User, Location], safe=True)
    print("Tables Created")
    DATABASE.close()
    


     