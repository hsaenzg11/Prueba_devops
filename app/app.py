from flask import Flask, request, jsonify

app = Flask(__name__)

# define the API key for authentication
API_KEY = "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"

# define the endpoint 
@app.route('/DevOps', methods=['POST'])
def devops():
    # check API key
    if 'X-Parse-REST-API-Key' not in request.headers or request.headers['X-Parse-REST-API-Key'] != API_KEY:
        return 'ERROR', 401
    
    # check if the JSON payload is valid
    json_data = request.get_json()
    if not json_data or 'message' not in json_data or 'to' not in json_data or 'from' not in json_data or 'timeToLifeSec' not in json_data:
        return 'ERROR', 400
    
    # process the request and return the response
    response_data = {
        'message': f'Hello {json_data["to"]} your message will be sent'
    }
    return jsonify(response_data)
if __name__ == '__main__':
    app.run()

