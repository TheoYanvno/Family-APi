"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import random
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")
jackson_family.add_member({"first_name": "John", "age": "33","lucky_number": [7,13,22]})
jackson_family.add_member({"first_name": "Jane", "age": "35","lucky_number": [10,14,3]})
jackson_family.add_member({"first_name": "Jimmy", "age": "5","lucky_number": [1]})

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_get_all_members():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()



    return jsonify(members), 200

@app.route('/member', methods=['POST'])
def handle_add_member():
    data = request.get_json()
    # data['id'] = random.randint(10000, 1000000)
    jackson_family.add_member(data)
    return jsonify(data), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def handle_delete_member(member_id):
    jackson_family.delete_member(member_id)
    return jsonify({'done': True}), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def handle_get_member(member_id):
    member = jackson_family.get_member(member_id)
    if len(member) > 0:
        return jsonify(member[0]), 200
    else:
        return jsonify({}), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
