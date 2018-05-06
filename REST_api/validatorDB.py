from queryDB import QueryDB
from datetime import datetime
from datetime import date
import MySQLdb
import responseMessage
import utils


class ValidatorDB:
    def __init__(self, query_db: QueryDB):
        self.query_db = query_db

    def valid_token(self, token):
        """
        Check if the token given is valid or not
        :param token: a user token to have access to the database
        :return: A boolean (true if it is correct)
        """
        query = """SELECT EXISTS
                     (SELECT *
                      FROM User
                      WHERE token = %s)"""
        res = self.query_db.get_query_db(query, (token,), one=True)

        if res[0] == 1:
            return True
        else:
            return False

    def check_type_id(self, type_id):
        """
        Check if the type of the product given is correct
        :param type_id: An integer
        :return: A boolean (true if it is correct)
        """
        if not utils.is_valid_number(type_id):
            return False

        query = """SELECT EXISTS
                     (SELECT *
                      FROM Description_type
                      WHERE type_id = %s)"""
        res = self.query_db.get_query_db(query, (type_id,), one=True)

        if res[0] == 1:
            return True
        else:
            return False

    def check_freezer_id(self, token, freezer_id, available=True):
        """
        Check if the id of the freezer given is correct
        :param available:
        :param token: a user token to have access to the database
        :param freezer_id: An integer
        :return: A boolean (true if it is correct)
        """
        if not utils.is_valid_number(freezer_id):
            return False

        query = """SELECT EXISTS
                     (SELECT *
                      FROM List_freezer
                      WHERE freezer_id = %s AND token = %s)"""
        res = self.query_db.get_query_db(query, (freezer_id, token,), one=True)

        if res[0] == 1:
            val = True
        else:
            val = False

        if available:
            return val
        else:
            return not val

    @staticmethod
    def check_date(date_prod):
        """
        Check the date of the product
        :param date_prod: A date in an ISO format XXXX-XX-XX
        :return: A boolean (true if it is correct)
        """
        datetime_today = datetime.strptime(str(date.today()), '%Y-%m-%d')
        try:
            datetime_format = datetime.strptime(date_prod, '%Y-%m-%d')
            if datetime_format > datetime_today:
                return False
        except ValueError as e:
            print(e)
            return False

        return True

    def check_product_emplacement(self, token, freezer_id, box_num, prod_num):
        """
        Check if the emplacement given is valid. It checks the freezer identifier with the box number
        and the product number.
        :param token: a user token to have access to the database
        :param freezer_id: An integer that represents the id of the
        :param box_num: An integer that represents the box where the product is stored
        :param prod_num: An integer that represents the id of the product in the box
        :return: A boolean (true if it is correct)
        """
        if not utils.is_valid_number(freezer_id) \
                and utils.is_valid_number(box_num)\
                and utils.is_valid_number(prod_num):
            return False

        query = """SELECT *
                   FROM List_freezer
                   WHERE token = %s AND freezer_id = %s"""

        valid_freezer_id = self.query_db.get_query_db(query, (token,
                                                              freezer_id,))
        if not valid_freezer_id:
            return False

        query = """SELECT prod_num
                   FROM Product
                   WHERE token = %s AND freezer_id = %s AND box_num = %s AND prod_num = %s AND date_out IS NULL """
        res = self.query_db.get_query_db(query, (token,
                                                 freezer_id,
                                                 box_num,
                                                 prod_num,))

        for l in res:
            for e in l:
                if e == int(prod_num):
                    return False

        return True

    def check_insert_product(self, token, header, product):
        """
        Check if the product follows the rules to be inserted in the database
        :param token: a user token to have access to the database
        :param header: A list of that represents the keys that the json object need to have
        :param product: A json object that represent the product to check
        :return: a Tuple True with the formatted object or False with the {'error_type': 'explanation...'}
        """
        product_formatted = {}
        if list(product.keys()) == header:

            if not self.check_product_emplacement(token,
                                                  product['freezer_id'],
                                                  product['box_num'],
                                                  product['prod_num']):
                return False, {'error_type': responseMessage.BAD_PRODUCT_EMPLACEMENT}

            product_formatted['freezer_id'] = int(product['freezer_id'])
            product_formatted['box_num'] = int(product['box_num'])
            product_formatted['prod_num'] = int(product['prod_num'])

            for idx, value in enumerate(header):

                if value == 'type_id' and not self.check_type_id(product[header[idx]]):
                    return False, {'error_type': responseMessage.BAD_PRODUCT_TYPE}
                elif value == 'type_id':
                    product_formatted[header[idx]] = int(product[header[idx]])
                    continue

                if value == 'date_in' and not self.check_date(product[header[idx]]):
                    return False, {'error_type': responseMessage.BAD_PRODUCT_DATE}
                elif value == 'date_in':
                    product_formatted[header[idx]] = datetime.strptime(product[header[idx]], '%Y-%m-%d')
                    continue

                if value == 'period' and not utils.is_valid_number(product[header[3]]):
                    return False, {'error_type': responseMessage.BAD_PRODUCT_PERIOD}
                elif value == 'period':
                    product_formatted[header[idx]] = int(product[header[idx]])
                    continue

                if value == 'quantity' and not utils.is_valid_number(product[header[6]]):
                    return False, {'error_type': responseMessage.BAD_PRODUCT_QUANTITY}
                elif value == 'quantity':
                    product_formatted[header[idx]] = int(product[header[idx]])
                    continue

                if value == 'product_name':
                    product_formatted[header[idx]] = MySQLdb.escape_string(product[header[idx]]).decode('utf-8') #To have the characters in utf8 and not in unicode format
                    continue

                if value == 'text_descr':
                    product_formatted[header[idx]] = MySQLdb.escape_string(product[header[idx]]).decode('utf-8') #To have the  character in utf8 and not in unicode format
                    continue

            return True, product_formatted

        else:
            return False, {'error_type': responseMessage.BAD_FORMAT}

    # curl - d
    # '{"product_name":"Glace au citron","text_descr":"", "freezer_id":"","type_id":"","date_in":"", "date_out": "", "period":"","box_num":"","prod_num":"","quantity":""}' - H
    # "Content-Type: application/json" - X
    # POST
    # http: // localhost: 5000 / update_product / 1 / 5
    # b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92
    # TODO need to do more tests
    def check_update_product(self, product, update, token):
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

        if not can_be_updated == list(update.keys()):
            # TODO change the message sent
            return False, {'error_type': responseMessage.BAD_FORMAT}

        # set keys with None value
        format_prod = dict.fromkeys(can_be_updated)

        if update['box_num'] or update['freezer_id'] or update['prod_num']:

            if not update['freezer_id']:
                format_prod['freezer_id'] = product['freezer_id']
            elif utils.is_valid_number(update['freezer_id']):
                format_prod['freezer_id'] = update['freezer_id']
            else:
                return False, {'error_type': responseMessage.BAD_FORMAT}

            if not update['box_num']:
                format_prod['box_num'] = product['box_num']
            elif utils.is_valid_number(update['box_num']):
                format_prod['box_num'] = update['box_num']
            else:
                return False, {'error_type': responseMessage.BAD_FORMAT}

            if not update['prod_num']:
                format_prod['prod_num'] = product['prod_num']
            elif utils.is_valid_number(update['prod_num']):
                format_prod['prod_num'] = update['prod_num']
            else:
                return False, {'error_type': responseMessage.BAD_FORMAT}

            if not self.check_product_emplacement(token,
                                                  format_prod['freezer_id'],
                                                  format_prod['box_num'],
                                                  format_prod['prod_num']):
                return False, {'error_type': responseMessage.BAD_PRODUCT_EMPLACEMENT}

        if update['type_id']:
            if not self.check_type_id(update['type_id']):
                return False, {'error_type': responseMessage.BAD_PRODUCT_TYPE}

            format_prod['type_id'] = update['type_id']

        if update['date_in']:
            if not self.check_date(update['date_in']):
                return False, {'error_type': responseMessage.BAD_PRODUCT_DATE}

            format_prod['date_in'] = update['date_in']

        if update['date_out']:
            format_prod['date_remove'] = False
            if update['date_out'] == 'null':
                format_prod['date_remove'] = True
            elif not self.check_date(update['date_out']):
                return False, {'error_type': responseMessage.BAD_PRODUCT_DATE}

            format_prod['date_out'] = update['date_out']

        if update['period']:
            if not utils.is_valid_number(update['period']):
                return False, {'error_type': responseMessage.BAD_PRODUCT_PERIOD}

            format_prod['period'] = update['period']

        if update['quantity']:
            if not utils.is_valid_number(update['quantity']):
                return False, {'error_type': responseMessage.BAD_PRODUCT_QUANTITY}

            format_prod['quantity'] = update['quantity']

        if update['product_name']:
            format_prod['product_name'] = MySQLdb.escape_string(update['product_name']).decode("utf-8")

        if update['text_descr']:
            format_prod['text_descr'] = MySQLdb.escape_string(update['text_descr']).decode("utf-8")

        return True, format_prod
