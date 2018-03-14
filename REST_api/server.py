from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
from flask import json

from flask_cors import CORS, cross_origin

import MySQLdb
import mysqlRequests
import response_message
from queryDB import QueryDB
from validatorDB import ValidatorDB

# utiliser  mysqlclient-python
app = Flask(__name__)
CORS(app, support_credentials=True)
connection = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="freezer")

query_db = QueryDB(connection)
validator_db = ValidatorDB(query_db)


def generate_response(status, details):
    return app.response_class(status=status,
                              mimetype='application/json',
                              response=json.dumps({"status": status, "details": details}))


@app.route("/", methods=['GET'])
@cross_origin(supports_credentials=True)
def ttest():
    print("return the documentation")


@app.route("/types/<string:token>", methods=["GET"])
def get_types(token):
    token = MySQLdb.escape_string(token)
    if validator_db.check_token(token):
        return jsonify(query_db.get_query_db(mysqlRequests.GET_TYPES,
                                             header=True))

    return generate_response(400, response_message.BAD_TOKEN)


# gerer les response code
# example
# curl -H "Content-Type: application/json" -X POST -d '{"num_boxes":"4","name":"xyz"}' http://localhost:5000/freezers/93896fbc55089bbf31d7a4c5db8fc992/
@app.route("/freezers/<string:token>", methods=['GET', 'POST'])
def freezers(token):
    token = MySQLdb.escape_string(token)
    if request.method == 'GET':
        if validator_db.check_token(token):
            query = """SELECT *
                       FROM Description_freezer"""
            return jsonify(query_db.get_query_db(query, header=True))

        return generate_response(400, response_message.BAD_TOKEN)

    if request.method == 'POST':
        freezer = request.get_json()
        if validator_db.check_token(token):
            if list(freezer.keys()) == ['num_boxes', 'name']:
                if not freezer['num_boxes'].isdigit():
                    return generate_response(400, response_message.BAD_FORMAT)
                num = int(freezer['num_boxes'])
                name = MySQLdb.escape_string(freezer['name'])

                ## catch the error server if case of fails
                query_db.insert_query_db(mysqlRequests.INSERT_FREEZER,
                                         (num, name, token,))
            else:
                return generate_response(400, response_message.BAD_TOKEN)

        return Response(status=200)

    return generate_response(400, response_message.BAD_TOKEN)


# # curl -H "Content-Type: application/json" -X POST -d '{"product_name":"Soupe de Noël","text_descr":"Soupe à base de tomate, poivrons et petits pois", "freezer_id":"1","type_id":"1","date_in":"2017-12-26","period":"6","box_num":"1","prod_num":"3","quantity":"4"}' http://localhost:5000/add_product/5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92
@app.route("/add_product/<string:token>", methods=['POST'])
def add_product(token):
    token = MySQLdb.escape_string(token)
    header = ['product_name',
              'text_descr',
              'freezer_id',
              'type_id',
              'date_in',
              'period',
              'box_num',
              'prod_num',
              'quantity']

    new_product = request.get_json()

    if validator_db.check_token(token):
        correct, new_product = validator_db.check_insert_product(token, header, new_product)

        if not correct:
            return generate_response(400, response_message.BAD_FORMAT)

        query_db.insert_query_db(mysqlRequests.INSERT_PRODUCT,
                                 (new_product['product_name'], new_product['text_descr'], new_product['type_id'],
                                  token, new_product['freezer_id'], new_product['type_id'],
                                  new_product['date_in'], new_product['period'], new_product['box_num'],
                                  new_product['prod_num'], new_product['quantity'],))
    else:
        return generate_response(400, response_message.BAD_TOKEN)

    return Response(status=200)


@app.route("/get_product/<string:params>/<int:freezer_id>/<string:token>", methods=['GET'])
def get_product(token, params, freezer_id):
    token = MySQLdb.escape_string(token)
    if validator_db.check_token(token):
        if params == 'all':
            if freezer_id == 0:
                return jsonify(query_db.get_query_db(mysqlRequests.GET_ALL_PRODUCTS_ALL_FREEZERS,
                                                     (token,),
                                                     header=True))
            else:
                return jsonify(query_db.get_query_db(mysqlRequests.GET_ALL_PRODUCTS_ONE_FREEZER,
                                                     (token, freezer_id,),
                                                     header=True))

        if params == 'inside':
            if freezer_id == 0:
                return jsonify(query_db.get_query_db(mysqlRequests.GET_ALL_PRODUCTS_INSIDE_ALL_FREEZERS,
                                                     (token,),
                                                     header=True))
            else:
                return jsonify(query_db.get_query_db(mysqlRequests.GET_ALL_PRODUCTS_INSIDE_ONE_FREEZER,
                                                     (token, freezer_id,),
                                                     header=True))

        if params == 'outside':
            if validator_db.check_token(token):
                if freezer_id == 0:
                    return jsonify(query_db.get_query_db(mysqlRequests.GET_ALL_PRODUCTS_OUTSIDE_ALL_FREEZERS,
                                                         (token,),
                                                         header=True))
                else:
                    return jsonify(query_db.get_query_db(mysqlRequests.GET_ALL_PRODUCTS_OUTSIDE_ONE_FREEZER,
                                                         (token, freezer_id,),
                                                         header=True))

        return generate_response(400, response_message.BAD_PARAMETER)

    return generate_response(400, response_message.BAD_TOKEN)


@app.route("/update_product/<int:product_id>/<string:object>/<string:token>", methods=['POST'])
def update_product(token, product_id, object):
    token = MySQLdb.escape_string(token)
    can_be_updated = ['product_name',
                      'text_descr',
                      'freezer_id',
                      'type_id',
                      'date_in',
                      'date_out',
                      'period',
                      'box_num',
                      'prod_num',
                      'quantity']
    if object not in can_be_updated:
        return generate_response(400, response_message.BAD_FORMAT)

    query = """SELECT *
               FROM Product
               WHERE token = %s AND prod_id =%s"""
    query_result = query_db.get_query_db(query, (token, product_id,), header=True)
    if query_result:
        product = query_result[0]
    else:
        return

    if validator_db.check_token(token):
        new_product = request.get_json()
        if list(new_product.keys()) == [object]:
            value_formatted = MySQLdb.escape_string(new_product[object])

            if object == 'product_name':
                query_db.insert_query_db(mysqlRequests.UPDATE_PRODUCT_NAME,
                                         (value_formatted, product['descr_id'],))

            if object == 'text_descr':
                query_db.insert_query_db(mysqlRequests.UPDATE_TEXT_DESCR,
                                         (value_formatted, product['descr_id'],))

            if object == 'freezer_id':
                if not validator_db.check_freezer_id(token, value_formatted):
                    return generate_response(400, response_message.BAD_FORMAT)
                query_db.insert_query_db(mysqlRequests.UPDATE_FREEZER_ID,
                                         (int(value_formatted), product['prod_id'],))

            if object == 'type_id':
                if not validator_db.check_type_id(value_formatted):
                    return generate_response(400, response_message.BAD_FORMAT)
                query_db.insert_query_db(mysqlRequests.UPDATE_TYPE_ID,
                                         (int(value_formatted), product['prod_id'],))

            if object == 'date_in':
                if not validator_db.check_date(value_formatted.decode("utf-8")):
                    return generate_response(400, response_message.BAD_FORMAT)

                query_db.insert_query_db(mysqlRequests.UPDATE_DATE_IN,
                                         (value_formatted, product['prod_id'],))

            if object == 'date_out':
                remove = False
                if value_formatted.decode("utf-8") == 'null':
                    remove = True
                elif not validator_db.check_date(value_formatted.decode("utf-8")):
                    return generate_response(400, response_message.BAD_FORMAT)

                if remove:
                    query_db.insert_query_db(mysqlRequests.REMOVE_DATE_OUT,
                                             (product['prod_id'],))
                else:
                    query_db.insert_query_db(mysqlRequests.UPDATE_DATE_OUT,
                                             (value_formatted, product['prod_id'],))

            if object == 'period':
                if not value_formatted.isdigit():
                    return generate_response(400, response_message.BAD_FORMAT)

                query_db.insert_query_db(mysqlRequests.UPDATE_PERIOD,
                                         (value_formatted, product['prod_id'],))
            ## box et prod num à faire
            if object == 'quantity':
                if not value_formatted.isdigit():
                    return generate_response(400, response_message.BAD_FORMAT)

                query_db.insert_query_db(mysqlRequests.UPDATE_QUANTITY,
                                         (value_formatted, product['prod_id'],))

            return Response(status=200)

    return generate_response(400, response_message.BAD_TOKEN)

# get_product("5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92", 2, 3)
