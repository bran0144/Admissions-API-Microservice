from flask import Flask, request, jsonify
from pymongo import MongoClient
import certifi
from bson import json_util
import json


app = Flask(__name__)
uri=""

app.secret_key = "your_secret_key"  # Replace with a strong secret key

client = MongoClient(uri, tlsCAFile=certifi.where())
application_db = client['applications']  
applications_collection = application_db['applications']


@app.route('/applications', methods=['POST'])
def create_application():

    data = request.get_json()
    email = data.get('email')
    college_name = data.get('college_name')
    location = data.get('location')
    date_submitted = data.get('date_submitted')
    status = data.get('status')
    ranking = data.get('ranking')
    decision = data.get('decision')
    

    # Check if the application already exists
    if applications_collection.find_one({'college_name': college_name}):
        return jsonify({'message': f'Application already exists.'}), 401
     

    else:
        applications_collection.insert_one({'email': email, 'college_name': college_name, 'location':location, 'date_submitted': date_submitted, 'status': status, 'ranking': ranking, 'decision': decision})
        return jsonify({'message': f'New college added.'}), 201

   

@app.route('/applications', methods=['GET'])
def get_applications():

    data = request.get_json()
    email = data.get('email')

    applications = applications_collection.find({'email': email})

    documents = list(applications)

    json_string= json.dumps(documents, default=json_util.default)

    return json_string, 200
            
@app.route('/update', method=['PUT'])
def update_application():

    data = request.get_json()
    email = data.get('email')
    college_name = data.get('college_name')
    location = data.get('location')
    date_submitted = data.get('date_submitted')
    status = data.get('status')
    ranking = data.get('ranking')
    decision = data.get('decision')

    filter = ({'email': email, 'college_name': college_name}) 

    new_values = {"$set":{'location':location, 'date_submitted': date_submitted, 'status': status, 'ranking': ranking, 'decision': decision }}

    application = applications_collection.update_one(filter, new_values)

    if application.modified_count == 1:
        return jsonify({'message': f'Application updated.'}), 200
    
    else:
        return jsonify({'message': f'Application not found.'}), 404
    

@app.route('/delete', method=['DELETE'])
def delete_application():

    data = request.get_json()
    email = data.get('email')
    college_name = data.get('college_name')

    result = applications_collection.delete_one({'email': email, 'college_name': college_name})

    if result.deleted_count == 1:
        return jsonify({'message': f'Application deleted.'}), 204
    
    else:
        return jsonify({'message': f'Application not found.'}), 404

if __name__ == "__main__":

    app.run(port=9003, debug=True)