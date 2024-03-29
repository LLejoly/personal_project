from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
from flask import json
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from flask_cors import CORS

import MySQLdb
import mysqlRequests
import responseMessage
import utils
from queryDB import QueryDB
from validatorDB import ValidatorDB

import os
import sys

if os.environ.get("DB_NAME"):
    db_identifier = os.environ.get("DB_NAME")
else:
    sys.exit("The environment DB_NAME is not set")

app = Flask(__name__)

# set up limiter on the number of requests that can be done for a user
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["24000 per day", "100 per minute"]
)

# One of the simplest configurations. Exposes all resources matching /* to
# CORS and allows the Content-Type header, which is necessary to POST JSON
# cross origin. All resources with this matching automatically has CORS headers set.
CORS(app, resources=r'/*')
# Try to connect to the database
try:
    connection = MySQLdb.connect(host="127.0.0.1",
                                 user="root",
                                 passwd="",
                                 db=db_identifier)
except MySQLdb.OperationalError as e:
    sys.exit(e)

query_db = QueryDB(connection)
validator_db = ValidatorDB(query_db)


def custom_response(status, details):
    """
    Generate a custom response that essentially send a JSON object with the status code returned.
    This JSON object follows the architecture:
    {
    "status": status code,
    "details": A text that explains the status code
    }
    :param status: An HTTP status code
    :param details: A text that explains this status code
    :return:
    """
    return app.response_class(status=status,
                              mimetype='application/json',
                              response=json.dumps({"status": status,
                                                   "details": details}))


@app.route("/", methods=['GET'])
def root():
    print("The documentation can be accessed in /documentation/api-documentation/site/index.html")
    return Response(status=200)


@app.route("/check_token/<string:token>", methods=['GET'])
def check_token(token):
    """
    Check the validity of a given token
    :param token: a user token to have access to the database
    :return: returns status code 200 if the request is a success
    otherwise a custom response that explains the problem
    """
    # Avoid SQL injection before doing requests
    # with the token and check the validity of it.
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
    # Avoid SQL injection before doing requests
    # with the token and check the validity of it.
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
    # Avoid SQL injection before doing requests
    # with the token and check the validity of it
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
        # Check if the JSON field is correct
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
        # Check if the JSON field is correct
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
        # Check if the JSON field is correct
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
    # Avoid SQL injection before doing requests
    # with the token and check the validity of it
    token = MySQLdb.escape_string(token)
    if not validator_db.valid_token(token):
        return custom_response(400, responseMessage.BAD_TOKEN)

    freezer = query_db.get_query_db(mysqlRequests.GET_SPECIFIC_FREERZER,
                                    (freezer_id,),
                                    one=True,
                                    header=True)

    # The freezer requested does not exist for the user specified
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
    # Avoid SQL injection before doing requests
    # with the token and check the validity of it
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


@app.route("/add_product/<string:token>", methods=['POST'])
def add_product(token):
    """
    Allow to add a new product to the database the JSON sent must be of type:
    {
      "product_name": "name",
      "text_descr": "description",
      "freezer_id": number,
      "type_id": number,
      "date_in" datetime YYY-MM-DD,
      "period":" number,
      "box_num": number,
      "prod_num": number,
      "quantity": number
    }
    :param token: a user token to have access to the database
    :return: a status code possible with a custom response
    """
    # Avoid SQL injection before doing requests
    # with the token and check the validity of it
    token = MySQLdb.escape_string(token)
    if not validator_db.valid_token(token):
        return custom_response(400, responseMessage.BAD_TOKEN)

    new_product = request.get_json()
    # data sent is not 'application/json' type
    if new_product is None:
        return custom_response(415, responseMessage.BAD_CONTENT_TYPE)
    # Check and returned the product correctly formatted (string escape, datetime,...)
    # if the new product was correctly sent. Otherwise, the element returned is simply a dictionary with
    # a error_type field that explain the reason of this error.
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


@app.route("/update_product/<int:freezer_id>/<int:box_num>/<int:prod_num>/<int:inside>/<string:token>",
           methods=['POST'])
def update_product(freezer_id, box_num, prod_num, inside, token):
    """
    Update an existing product by giving the freezer identifier, the box number inside of this freezer,
    the product number inside this pox, and specifiying if the product is still present in the freezer or if
    it is an old product previously stored at that place. With these four parameter a JSON object of the following form
    need to be sent:
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
    Where the fields to update need to be non empty.
    To remove the output date out, the field date_out simply be set to null

    :param freezer_id: A number that refer to a user with the token given
    :param box_num: The box number where the product is located
    :param prod_num: The identifier of the product inside of that box
    :param inside: An integer that specify if the product is still in the freezer or no.
    A number which is higher or equal to one will be interpreted as inside otherwise it
    will be interpreted as outside.
    :param token: a user token to have access to the database
    :return:
    """
    # Avoid SQL injection before doing requests
    # with the token and check the validity of it.
    token = MySQLdb.escape_string(token)
    if not validator_db.valid_token(token):
        return custom_response(400, responseMessage.BAD_TOKEN)

    # Check if the product is inside the freezers
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
    # Check a product with the different parameters given for the requests
    # lead to an actual product or not.
    if not curr_product:
        return custom_response(400, responseMessage.BAD_PARAMETER)

    updt_product = request.get_json()
    # data sent is not 'application/json' type
    if updt_product is None:
        return custom_response(415, responseMessage.BAD_CONTENT_TYPE)
    # Check and returned the product correctly formatted (string escape, datetime,...)
    # if the product was correctly sent. Otherwise, the element returned is simply a dictionary with
    # a error_type field that explain the reason of this error.
    validity, update_prod = validator_db.check_update_product(token,
                                                              curr_product,
                                                              updt_product)
    if not validity:
        return custom_response(400, update_prod['error_type'])

    # UPDATE sequentially each element
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
        # Check if the update is to remove the output date
        if update_prod['date_remove']:
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


@app.route("/general_tendency/<string:token>", methods=['GET'])
def general_tendency(token):
    """
    This function is used to give the global view of products stored and consumed by all people
    using the API. It simply list the occurrence of each product type in the database and are sorted
    following the descending order on the frequency.
    [
        {
        "freq": 12,
        "type_id": 1,
        "type_name_en": "soup",
        "type_name_fr": "soupe"
        },
        {
        "freq": 6,
        "type_id": 24,
        "type_name_en": "ice-cream",
        "type_name_fr": "glace"
        },
        ...
    ]
    :param token: a user token to have access to the database
    :return:
    """
    # Avoid SQL injection before doing requests
    # with the token and check the validity of it.
    token = MySQLdb.escape_string(token)
    if not validator_db.valid_token(token):
        return custom_response(400, responseMessage.BAD_TOKEN)

    return jsonify(query_db.get_query_db(mysqlRequests.GET_GLOBAL_TENDENCY,
                                         header=True))


@app.route("/custom_tendency/<string:token>", methods=['GET'])
def custom_tendency(token):
    """
    This function is used to give the personalized tendency of a specific user based on his previous consumptions.
    And are sorted following the latest date and the Descending order on the frequency.
    The response returned is a Json object of the form.
    [
        {
        "freq": 12,
        "latest": "2018-02-05",
        "type_id": 1,
        "type_name_en": "soup",
        "type_name_fr": "soupe"
        },
        {
        "freq": 6,
        "latest": "2017-05-02",
        "type_id": 24,
        "type_name_en": "ice-cream",
        "type_name_fr": "glace"
        },
        ...
    ]

    :param token: a user token to have access to the database
    :return: A JSON object similar to the example given above
    """
    # Avoid SQL injection before doing requests
    # with the token and check the validity of it.
    token = MySQLdb.escape_string(token)
    if not validator_db.valid_token(token):
        return custom_response(400, responseMessage.BAD_TOKEN)

    tendency = query_db.get_query_db(mysqlRequests.GET_PERSONALIZED_TENDENCY,
                                     (token,),
                                     header=True)

    types_in_freezers = query_db.get_query_db(mysqlRequests.GET_TYPES_USED,
                                              (token,),
                                              header=True)
    list_tendency = []
    # Check if it is still possible to retrieve products
    # of types referred inside the tendency variable that simply
    # links the tendency of a user without checking if products of
    # that type are still present in freezers.
    for elem in tendency:
        res = map(lambda x: x['type_id'] == elem['type_id'], types_in_freezers)
        if res:
            list_tendency.append(elem)

    return jsonify(list_tendency)


if __name__ == '__main__':
    app.config['TESTING'] = True
    app.run()
