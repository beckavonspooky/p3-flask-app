import models

from flask import request, jsonify, Blueprint
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user
from playhouse.shortcuts import model_to_dict

##setting up the user & login

user = Blueprint("users", "user")

@user.route('/register', methods= ["POST"])
def register():
    payload = request.get_json()
    payload['email'] = payload['email'].lower()
    try:
        #does user exist in db? 
        models.User.get(models.User.email == payload ['email']) 
        #finding user by email
        return jsonify(data={}, status={"code": 401, "message": "User with that Email and name already exits"})
    except models.DoesNotExist: 
        payload["password"] = generate_password_hash(payload["password"])
        
        #bcrypt for hash
        user = models.User.create(**payload)

        #login portion
        login_user(user)

        user_dict = model_to_dict(user)
        print(user_dict)
        del user_dict['password']
        print(type(user_dict["password"]))
        return jsonify(data=user_dict, status= {"code": 201, "message": "It worked"})

@user.route('/login', methods=["POST"])
def login():
    payload = request.get_json()
    print(payload)
    try: 
        user = models.User.get(models.User.email == payload ["email"])
        user_dict = model_to_dict(user)
        if(check_password_hash(user_dict["password"], payload['password'])):
            del user_dict['password']
            login_user(user)
            print('Welcome back ' + user)
            return jsonify(data=user_dict, status={"code": 200, "message": "Success"})
        else:
            return jsonify(data={}, status={"code": 401, "message": "Email or Password is incorrect"})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'Email or Password is incorrect'})

# @user.route('/<id>', methods=["PUT"])
# def update_user(id):
#     try:
#         payload = request.get_json()
#         query = models.User.edit().where(edit.User.userid==id)query.execute()
#         return jsonify (data=model_to_dict(models.User.get_by_id(id)), status={"code": 200, "message": "resource successfully edited"})
#     except:
#         return jsonify(data={}, status={'code': 401, 'message': 'User not found.'})

# @user.route('/id', methods=["DELETE"])
# def delete_user(id):
#     query = models.user.delete().where(models.User.id==id)
#     query.execute()
#     return jsonify(data='resource successfully deleted', status={"code": 200, "message": "resource deleted successfully"})