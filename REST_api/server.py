from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
from flask import json

from flask_cors import CORS

import MySQLdb
import mysqlRequests
import responseMessage
import utils
from queryDB import QueryDB
from validatorDB import ValidatorDB

# TODO put flask limiter to limit the number of requests
app = Flask(__name__)
# One of the simplest configurations. Exposes all resources matching /* to
# CORS and allows the Content-Type header, which is necessary to POST JSON
# cross origin. All resources with this matching automatically has CORS headers set.
CORS(app, resources=r'/*')

connection = MySQLdb.connect(host="127.0.0.1",
                             user="root",
                             passwd="",
                             db="freezer.test")

query_db = QueryDB(connection)
validator_db = ValidatorDB(query_db)


def custom_response(status, details):
    return app.response_class(status=status,
                              mimetype='application/json',
                              response=json.dumps({"status": status,
                                                   "details": details}))


@app.route("/", methods=['GET'])
def root():
    # TODO return the documentation or a link to have access to it
    print("return the documentation")
    return Response(status=200)


@app.route("/check_token/<string:token>", methods=['GET'])
def check_token(token):
    """
    Check the validity of a given token
    :param token: a user token to have access to the database
    :return: returns status code 200 if the request is a success
    otherwise a custom response that explains the problem
    """
    token = MySQLdb.escape_string(token)
    if not validator_db.valid_token(token):
        return custom_response(400, responseMessage.BAD_TOKEN)

    return Response(status=200)


@app.route("/types/<string:token>", methods=["GET"])
def get_types(token):
    """
    Return the different possible types present in the database.
    :param token: a user token to have access to the database
    :return: A JSON containing the types of an error occurred
    """
    token = MySQLdb.escape_string(token)
    if not validator_db.valid_token(token):
        return custom_response(400, responseMessage.BAD_TOKEN)

    return jsonify(query_db.get_query_db(mysqlRequests.GET_TYPES,
                                         header=True))


# gerer les response code example curl -H "Content-Type: application/json" -X POST -d '{"num_boxes":"4",
# "name":"xyz"}' http://localhost:5000/freezers/93896fbc55089bbf31d7a4c5db8fc992/
@app.route("/freezers/<string:token>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def freezers(token):
    """
    This functions has a different behavior depending on the request Type:
    - GET method will return a json object containing the different freezers owned by the user
    - POST method will add a freezer to the freezers' list of the user.
     The POST request takes a JSON of the following form: {"num_boxes":"4","name":"xyz"}
    :param token: a user token to have access to the database
    :return: - GET method returns a JSON object or a custom error in case of bad request
             - POST method returns a status code with possible a custom response if it was not a success
    """
    token = MySQLdb.escape_string(token)
    if not validator_db.valid_token(token):
        return custom_response(400, responseMessage.BAD_TOKEN)

    if request.method == 'GET':
        return jsonify(query_db.get_query_db(mysqlRequests.GET_FREEZERS,
                                             (token,),
                                             header=True))

    if request.method == 'POST':
        freezer = request.get_json()

        # data sent is not 'application/json' type
        if freezer is None:
            return custom_response(415, responseMessage.BAD_CONTENT_TYPE)

        if set(freezer.keys()) == {'num_boxes', 'name'}:
            if not utils.is_valid_number(freezer['num_boxes']):
                return custom_response(400, responseMessage.BAD_FORMAT)

            freezer['name'] = MySQLdb.escape_string(freezer['name']).decode("utf-8")

            if not query_db.insert_query_db(mysqlRequests.INSERT_FREEZER,
                                            (freezer['num_boxes'],
                                             freezer['name'],
                                             token,)):
                return custom_response(500, responseMessage.SERVER_ERROR)
        else:
            return custom_response(400, responseMessage.BAD_FORMAT)

        return Response(status=200)
    # Update an existing freezer
    if request.method == 'PUT':
        freezer = request.get_json()
        # data sent is not 'application/json' type
        if freezer is None:
            return custom_response(415, responseMessage.BAD_CONTENT_TYPE)

        if set(freezer.keys()) == {'freezer_id', 'num_boxes', 'name'}:
            if not validator_db.valid_freezer_id(token, freezer['freezer_id'], available=False):
                return custom_response(400, responseMessage.BAD_FORMAT)

            curr_freezer = query_db.get_query_db(mysqlRequests.GET_SPECIFIC_FREERZER,
                                                 (freezer['freezer_id'],),
                                                 one=True,
                                                 header=True)
            if not freezer['num_boxes']:
                freezer['num_boxes'] = curr_freezer['number_boxes']
            else:
                if not utils.is_valid_number(freezer['number_boxes']):
                    return custom_response(400, responseMessage.BAD_FORMAT)

            if not freezer['name']:
                freezer['name'] = curr_freezer['freezer_name']
            else:
                freezer['name'] = MySQLdb.escape_string(freezer['name']).decode("utf-8")

            query_db.insert_query_db(mysqlRequests.UPDATE_FREEZER_NAME_AND_BOXES,
                                     (freezer['name'],
                                      freezer['num_boxes'],
                                      freezer['freezer_id'],))

        else:
            return custom_response(400, responseMessage.BAD_FORMAT)

        return Response(status=200)

    if request.method == 'DELETE':
        freezer = request.get_json()
        # data sent is not 'application/json' type
        if freezer is None:
            return custom_response(415, responseMessage.BAD_CONTENT_TYPE)

        if set(freezer.keys()) == {'freezer_id'}:
            if not validator_db.valid_freezer_id(token, freezer['freezer_id'], available=False):
                return custom_response(400, responseMessage.BAD_FORMAT)

            res = query_db.get_query_db(mysqlRequests.GET_PROD_NUM_LIST,
                                        (token,
                                         freezer['freezer_id'],),
                                        one=True,
                                        header=True)

            if res:
                return custom_response(400, responseMessage.DELETE_FREEZER)

            query_db.insert_query_db(mysqlRequests.DELETE_FREEZER,
                                     (freezer['freezer_id'],))
            return Response(status=200)

    return custom_response(400, responseMessage.BAD_REQUEST)


@app.route("/freezer_next_id/<int:freezer_id>/<string:token>", methods=['GET'])
def freezer_next_id(freezer_id, token):
    """
    Returns the next available product id for all boxes in a freezer
    :param freezer_id: the id of the freezer concerned
    :param token: a user token to have access to the database
    :return:
    """
    token = MySQLdb.escape_string(token)
    if not validator_db.valid_token(token):
        return custom_response(400, responseMessage.BAD_TOKEN)

    freezer = query_db.get_query_db(mysqlRequests.GET_SPECIFIC_FREERZER,
                                    (freezer_id,),
                                    one=True,
                                    header=True)

    if not freezer:
        return custom_response(400, responseMessage.BAD_FORMAT)

    next_idxs = {}
    for i in range(1, freezer['number_boxes'] + 1):
        next_idxs[str(i)] = 1

    products = query_db.get_query_db(mysqlRequests.GET_PROD_NUM_LIST,
                                     (token,
                                      freezer_id,))

    for idx, box in products:
        if next_idxs[str(box)] == idx:
            next_idxs[str(box)] = idx + 1

    return jsonify(next_idxs)


# curl -H "Content-Type: application/json" -X POST -d '{"product_name":"Soupe de Noël","text_descr":"Soupe à base
# de tomate, poivrons et petits pois", "freezer_id":"1","type_id":"1","date_in":"2017-12-26","period":"6",
# "box_num":"1","prod_num":"3","quantity":"4"}'
# http://localhost:5000/add_product/5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92
@app.route("/add_product/<string:token>", methods=['POST'])
def add_product(token):
    """
    Allow to add a new product to the database
    :param token: a user token to have access to the database
    :return: a status code possible with a custom response
    """
    token = MySQLdb.escape_string(token)
    if not validator_db.valid_token(token):
        return custom_response(400, responseMessage.BAD_TOKEN)

    new_product = request.get_json()
    # data sent is not 'application/json' type
    if new_product is None:
        return custom_response(415, responseMessage.BAD_CONTENT_TYPE)

    correct, new_product = validator_db.check_insert_product(token,
                                                             mysqlRequests.PRODUCT_HEADER,
                                                             new_product)
    if not correct:
        return custom_response(400, new_product['error_type'])

    query_db.insert_query_db(mysqlRequests.INSERT_PRODUCT,
                             (new_product['product_name'],
                              new_product['text_descr'],
                              new_product['type_id'],
                              token,
                              new_product['freezer_id'],
                              new_product['type_id'],
                              new_product['date_in'],
                              new_product['period'],
                              new_product['box_num'],
                              new_product['prod_num'],
                              new_product['quantity'],))

    return Response(status=200)


@app.route("/get_product/<string:params>/<int:freezer_id>/<string:token>", methods=['GET'])
def get_product(params, freezer_id, token):
    """
    Returns the list of products following certain restrictions for a user
    :param params: The parameters that we want to apply of the products
                - 'all': selects all products
                - 'inside': selects only products that are in the freezer
                - 'outside': select products that are outside
    :param freezer_id: select the freezer if 0 all freezers will be selected
    :param token: a user token to have access to the database
    :return:
    """
    token = MySQLdb.escape_string(token)
    if not validator_db.valid_token(token):
        return custom_response(400, responseMessage.BAD_TOKEN)

    if params == 'all':
        if freezer_id == 0:
            return jsonify(query_db.get_query_db(mysqlRequests.generate_product_query('all'),
                                                 (token,),
                                                 header=True))
        else:
            return jsonify(query_db.get_query_db(mysqlRequests.generate_product_query('all-one'),
                                                 (token,
                                                  freezer_id,),
                                                 header=True))

    if params == 'inside':
        if freezer_id == 0:
            return jsonify(query_db.get_query_db(mysqlRequests.generate_product_query('inside'),
                                                 (token,),
                                                 header=True))
        else:
            return jsonify(query_db.get_query_db(mysqlRequests.generate_product_query('inside-one'),
                                                 (token,
                                                  freezer_id,),
                                                 header=True))

    if params == 'outside':
        if validator_db.valid_token(token):
            if freezer_id == 0:
                return jsonify(query_db.get_query_db(mysqlRequests.generate_product_query('outside'),
                                                     (token,),
                                                     header=True))
            else:
                return jsonify(query_db.get_query_db(mysqlRequests.generate_product_query('outside-one'),
                                                     (token,
                                                      freezer_id,),
                                                     header=True))

    return custom_response(400, responseMessage.BAD_PARAMETER)


@app.route("/update_product/<int:freezer_id>/<int:box_num>/<int:prod_num>/<int:inside>/<string:token>",
           methods=['POST'])
def update_product(freezer_id, box_num, prod_num, inside, token):
    """
    Update an existing product by giving its id and sending a json object of the form
    {
     "product_name":"",
     "text_descr":"",
     "freezer_id":"",
     "type_id":"",
     "date_in":"",
     "date_out": "",
     "period":"",
     "box_num":"",
     "prod_num":"",
     "quantity":""
     }
       Where the fields to update need to be non empty. To remove the date out simply put null
    :param inside:
    :param prod_num:
    :param box_num:
    :param freezer_id:
    :param token: a user token to have access to the database
    :return:
    """
    token = MySQLdb.escape_string(token)
    if not validator_db.valid_token(token):
        return custom_response(400, responseMessage.BAD_TOKEN)
    if inside > 0:
        curr_product = query_db.get_query_db(mysqlRequests.GET_A_PRODUCT_INSIDE,
                                             (token,
                                              freezer_id,
                                              box_num,
                                              prod_num,),
                                             one=True,
                                             header=True)
    else:
        curr_product = query_db.get_query_db(mysqlRequests.GET_A_PRODUCT_OUTSIDE,
                                             (token,
                                              freezer_id,
                                              box_num,
                                              prod_num,),
                                             one=True,
                                             header=True)

    if not curr_product:
        return custom_response(400, responseMessage.BAD_PARAMETER)

    print(curr_product)
    updt_product = request.get_json()
    # data sent is not 'application/json' type
    if updt_product is None:
        return custom_response(415, responseMessage.BAD_CONTENT_TYPE)

    validity, update_prod = validator_db.check_update_product(curr_product,
                                                              updt_product,
                                                              token)

    if not validity:
        return custom_response(400, responseMessage.BAD_REQUEST)

    print(update_prod)
    # UPDATE SEQUENTIALLY
    if update_prod['freezer_id']:
        query_db.insert_query_db(mysqlRequests.UPDATE_QUANTITY,
                                 (update_prod['freezer_id'],
                                  update_prod['box_num'],
                                  update_prod['prod_num'],
                                  curr_product['prod_id'],))

    if update_prod['product_name']:
        query_db.insert_query_db(mysqlRequests.UPDATE_PRODUCT_NAME,
                                 (update_prod['product_name'], curr_product['descr_id'],))
    if update_prod['text_descr']:
        query_db.insert_query_db(mysqlRequests.UPDATE_TEXT_DESCR,
                                 (update_prod['text_descr'], curr_product['descr_id'],))
    if update_prod['freezer_id']:
        query_db.insert_query_db(mysqlRequests.UPDATE_FREEZER_ID,
                                 (update_prod['freezer_id'], curr_product['prod_id'],))
    if update_prod['type_id']:
        query_db.insert_query_db(mysqlRequests.UPDATE_TYPE_ID,
                                 (update_prod['type_id'], curr_product['prod_id'], curr_product['descr_id'],))
    if update_prod['date_in']:
        query_db.insert_query_db(mysqlRequests.UPDATE_DATE_IN,
                                 (update_prod['date_in'], curr_product['prod_id'],))
    if update_prod['date_out']:
        if update_prod['remove']:
            query_db.insert_query_db(mysqlRequests.REMOVE_DATE_OUT,
                                     (curr_product['prod_id'],))
        else:
            query_db.insert_query_db(mysqlRequests.UPDATE_DATE_OUT,
                                     (update_prod['date_out'], curr_product['prod_id'],))
    if update_prod['period']:
        query_db.insert_query_db(mysqlRequests.UPDATE_PERIOD,
                                 (update_prod['period'], curr_product['prod_id'],))
    if update_prod['quantity']:
        query_db.insert_query_db(mysqlRequests.UPDATE_QUANTITY,
                                 (update_prod['quantity'], curr_product['prod_id'],))
    return Response(status=200)


# TODO TAKE product is just a modification of update product
# get_product("5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92", 2, 3)

@app.route("/get_general_tendency/<string:token>", methods=['GET'])
def get_general_tendency(token):
    token = MySQLdb.escape_string(token)
    if not validator_db.valid_token(token):
        return custom_response(400, responseMessage.BAD_TOKEN)

    return jsonify(query_db.get_query_db(mysqlRequests.GET_GLOBAL_TENDENCY,
                                         header=True))


@app.route("/get_custom_tendency/<string:token>", methods=['GET'])
def get_custom_tendency(token):
    token = MySQLdb.escape_string(token)
    if not validator_db.valid_token(token):
        return custom_response(400, responseMessage.BAD_TOKEN)

    return jsonify(query_db.get_query_db(mysqlRequests.GET_PERSONALIZED_TENDENCY,
                                         (token,),
                                         header=True))


if __name__ == '__main__':
    app.config['TESTING'] = True
    app.run()
