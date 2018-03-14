from queryDB import QueryDB
from datetime import datetime
from datetime import date
import MySQLdb


class ValidatorDB:
    def __init__(self, query_db: QueryDB):
        self.query_db = query_db

    def check_token(self, token):
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
        if not type_id.isdigit():
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

    def check_freezer_id(self, token, freezer_id):
        if not freezer_id.isdigit():
            return False

        query = """SELECT EXISTS
                     (SELECT *
                      FROM List_freezer
                      WHERE freezer_id = %s AND token = %s)"""
        res = self.query_db.get_query_db(query, (freezer_id, token,), one=True)

        if res[0] == 1:
            return True
        else:
            return False

    @staticmethod
    def check_date(date_prod):
        datetime_today = datetime.strptime(str(date.today()), '%Y-%m-%d')
        try:
            datetime_format = datetime.strptime(date_prod, '%Y-%m-%d')
            if datetime_format > datetime_today:
                return False
        except ValueError as e:
            print(e)
            return False

        return True

    def check_product_id(self, token, freezer_id, box_num, prod_num):
        if not freezer_id.isdigit() and box_num.isdigit() and prod_num.isdigit():
            return False

        query = """SELECT prod_num
                      FROM Product
                      WHERE freezer_id = %s AND token = %s AND box_num = %s AND prod_num = %s"""
        res = self.query_db.get_query_db(query, (freezer_id, token, box_num, prod_num, ))

        if res[0] == 1:
            return False
        else:
            return True

    def check_insert_product(self, token, header, product):
        product_formatted = {}
        if list(product.keys()) == header:

            if not self.check_product_id(token, product['freezer_id'], product['box_num'], product['prod_num']):
                return False, {}
            product_formatted['box_num'] = int(product['box_num'])
            product_formatted['prod_num'] = int(product['prod_num'])

            for idx, value in enumerate(header):

                if value == 'freezer_id' and not self.check_freezer_id(token, product[header[idx]]):
                    return False, {}
                elif value == 'freezer_id':
                    product_formatted[header[idx]] = int(product[header[idx]])
                    continue

                if value == 'type_id' and not self.check_type_id(product[header[idx]]):
                    return False, {}
                elif value == 'type_id':
                    product_formatted[header[idx]] = int(product[header[idx]])
                    continue

                if value == 'date_in' and not self.check_date(product[header[idx]]):
                    return False, {}
                elif value == 'date_in':
                    product_formatted[header[idx]] = datetime.strptime(product[header[idx]], '%Y-%m-%d')
                    continue

                if value == 'period' and not product[header[3]].isdigit():
                    return False, {}
                elif value == 'period':
                    product_formatted[header[idx]] = int(product[header[idx]])
                    continue

                if value == 'quantity' and not product[header[6]].isdigit():
                    return False, {}
                elif value == 'quantity':
                    product_formatted[header[idx]] = int(product[header[idx]])
                    continue

                if value == 'product_name':
                    product_formatted[header[idx]] = MySQLdb.escape_string(product[header[idx]])
                    continue

                if value == 'text_descr':
                    product_formatted[header[idx]] = MySQLdb.escape_string(product[header[idx]])
                    continue

            return True, product_formatted

        else:
            return False, {}
