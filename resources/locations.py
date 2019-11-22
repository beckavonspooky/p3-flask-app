import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict

location = Blueprint('locations', 'location')

## get the list of locations
@location.route('/', methods=['GET'])
def get_all_locations():
    try:
        locations = [model_to_dict(location) for location in models.Location.select()]
        return jsonify(data=locations, status={'code': 200, 'message': 'Success'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'Error getting the resources'})

#create (add) a location 
@location.route('/<id>', methods=['POST'])
def create_locations(id):
    payload = request.get_json()
    payload['user_id'] = id
    print(payload, '<<---- payload is printing')
    location = models.Location.create(**payload)
    location_dict = model_to_dict(location)
    return jsonify(data=location_dict, status={'code': 201, 'message': 'Success'})

##show route: show location
@location.route('/<id>', methods=['GET'])
def get_location(id):
    try:
       location = model_to_dict(models.Location.get_by_id(id))
       print(location)
       return jsonify(data=location, status={'code': 201, 'message': 'Success'})

    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'Error location not found'})

##update the location
@location.route('/<id>', methods=['PUT'])
def update_location(id):
    try:
        payload = request.get_json()
        query = models.Location.update(**payload).where(models.Location.id == id)
        query.execute()
        return jsonify(data=model_to_dict(model.Location.get_by_id(id)), status={'code': 201, 'message': 'Location Updated'})
    
    except:
        return jsonify(data={}, status={'code': 401, 'message': 'Location does not exist'})

##delete a location from the db
@location.route('/<id>', methods=['DELETE'])
def delete_location(id):
    query = models.Location.delete().where(models.Location.id==id)
    query.execute()
    return jsonify(data='Location deleted', status={'code': 200, 'message': 'Location delated'})

