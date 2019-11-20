import datetime
from peewee import * 
from flask_login import UserMixin 

Database = SqliteDatabase('locations.sqlite')

class User(db.Model, UserMixin):
    __tableName__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    
    class meta: 
        database = DATABASE 
        
class Location(Model):
    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    loc_name: db.Column(db.CharField(), unique=True)
    street_num: db.Column(db.IntegerField(6))
    street_name: db.Column(db.CharField())
    apt_unit_num: db.Column(db.IntegerField())
    city: db.Column(db.CharField())
    State: db.Column(db.CharField(2))
    zipcode: db.Column(db.IntegerField(5))
    ada: db.Column(BooleanField())
    unisex: db.Column(BooleanField())
    open_time: db.Column(db.TimeField('Open time'))
    closing_time: db.Column(db.TimeField('Closing Time'))
    Directions: db.Column(db.CharField(255))

def initialize(): 
    DATABASE.connect()
    DATABASE.create_tables([User, Location], safe=True)
    print("Tables Created")
    DATABASE.close()
         

     