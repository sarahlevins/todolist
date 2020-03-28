import helper
import json
from flask import Flask, request, Response
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/item/new', methods=['POST'])
def add_item():
    # get item from the post body
    req_data = request.get_json()
    item = req_data['item']

    # add item to list
    res_data = helper.add_to_list(item)

    # return error if item not added
    if res_data is None:
        response = Response(f"{{'error': 'Item not added - {item} }}",
                            status=400, mimetype='application/json')
        return response

    response = Response(json.dumps(res_data), mimetype='application/json')

    return response


@app.route('/item/all', methods=['GET'])
def get_all_items():
    res_data = helper.get_all_items()

    return Response(json.dumps(res_data), mimetype='application/json')
    return response


@app.route('/item/status', methods=['GET'])
def get_item():
    item_name = request.args.get('name')
    status = helper.get_item(item_name)

    if status is None:
        response = Response(f"{{'error': 'Item Not Found - {item_name}'}}",
                            status=404, mimetype='application/json')
        return response

    # Return status
    res_data = {
        'status': status
    }

    response = Response(json.dumps(res_data), status=200,
                        mimetype='application/json')
    return response


@app.route('/item/update', methods=['PUT'])
def update_status():
    # get item from POST body
    req_data = request.get_json()
    item = req_data['item']
    status = req_data['status']

    # update item in list
    res_data = helper.update_status(item, status)

    if res_data is None:
        response = Response(f"{{'error': 'Error updating item - {item } {status} }}",
                            status=400, mimetype='application/json')
        return response

    response = Response(json.dumps(res_data), mimetype='application/json')
    return response


@app.route('/item/remove', methods=['DELETE'])
def delete_item():
    req_data = request.get_json()
    item = req_data['item']

    res_data = helper.delete_item(item)

    if res_data is None:
        response = Response(f"{{'error': 'Error deleting item - {item} }}",
                            status=400, mimetype='application/json')
        return response

    response = Response(json.dumps(res_data), mimetype='application/json')

    return response
