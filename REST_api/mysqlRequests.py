GET_TYPES = """SELECT *
               FROM Description_type"""


GET_ALL_PRODUCTS_ALL_FREEZERS = """SELECT box_num, DATE_FORMAT(date_in, '%%Y-%%m-%%d') AS date_formatted_in,
                                   DATE_FORMAT(date_out, '%%Y-%%m-%%d') AS date_formatted_out, descr_id,
                                   freezer_id, period, prod_id, prod_num, quantity, type_id
                                   FROM Product
                                   WHERE token = %s"""

GET_ALL_PRODUCTS_ONE_FREEZER = """SELECT box_num, DATE_FORMAT(date_in, '%%Y-%%m-%%d') AS date_formatted_in,
                                   DATE_FORMAT(date_out, '%%Y-%%m-%%d') AS date_formatted_out, descr_id,
                                   freezer_id, period, prod_id, prod_num, quantity, type_id
                                   FROM Product
                                   WHERE token = %s AND freezer_id = %s"""

GET_ALL_PRODUCTS_INSIDE_ALL_FREEZERS = """SELECT box_num, DATE_FORMAT(date_in, '%%Y-%%m-%%d') AS date_formatted_in,
                                          DATE_FORMAT(date_out, '%%Y-%%m-%%d') AS date_formatted_out, descr_id,
                                          freezer_id, period, prod_id, prod_num, quantity, type_id
                                          FROM Product
                                          WHERE token = %s AND date_out IS NULL """

GET_ALL_PRODUCTS_INSIDE_ONE_FREEZER = """SELECT box_num, DATE_FORMAT(date_in, '%%Y-%%m-%%d') AS date_formatted_in,
                                         DATE_FORMAT(date_out, '%%Y-%%m-%%d') AS date_formatted_out, descr_id,
                                         freezer_id, period, prod_id, prod_num, quantity, type_id
                                         FROM Product
                                         WHERE token = %s AND freezer_id = %s AND date_out IS NULL """

GET_ALL_PRODUCTS_OUTSIDE_ALL_FREEZERS = """SELECT box_num, DATE_FORMAT(date_in, '%%Y-%%m-%%d') AS date_formatted_in,
                                          DATE_FORMAT(date_out, '%%Y-%%m-%%d') AS date_formatted_out, descr_id,
                                          freezer_id, period, prod_id, prod_num, quantity, type_id
                                          FROM Product
                                          WHERE token = %s AND date_out IS NOT NULL """

GET_ALL_PRODUCTS_OUTSIDE_ONE_FREEZER = """SELECT box_num, DATE_FORMAT(date_in, '%%Y-%%m-%%d') AS date_formatted_in,
                                         DATE_FORMAT(date_out, '%%Y-%%m-%%d') AS date_formatted_out, descr_id,
                                         freezer_id, period, prod_id, prod_num, quantity, type_id
                                         FROM Product
                                         WHERE token = %s AND freezer_id = %s AND date_out IS NOT NULL """






INSERT_FREEZER = """BEGIN;
                    INSERT INTO Description_freezer (number_boxes, freezer_name) VALUES(%s, %s);
                    INSERT INTO List_freezer (freezer_id, token) VALUES(LAST_INSERT_ID(),%s);
                    COMMIT;"""

INSERT_PRODUCT = """BEGIN;
                    INSERT INTO Description_product (product_name, text_descr)  VALUES (%s, %s);
                    INSERT INTO Product_to_type (descr_id, type_id)  VALUES (LAST_INSERT_ID(), %s);
                    INSERT INTO Product (token, descr_id, freezer_id, type_id, date_in,
                    period, box_num, prod_num, quantity) VALUES(%s,LAST_INSERT_ID(),%s,%s,%s,%s,%s,%s,%s) ;
                    COMMIT;"""

UPDATE_PRODUCT_NAME = """BEGIN;
                         UPDATE Description_product
                         SET product_name =%s
                         WHERE descr_id =%s;
                         COMMIT;"""

UPDATE_TEXT_DESCR = """BEGIN;
                       UPDATE Description_product
                       SET text_descr =%s
                       WHERE descr_id =%s;
                       COMMIT;"""

UPDATE_FREEZER_ID = """BEGIN;
                       UPDATE Product
                       SET freezer_id =%s
                       WHERE prod_id =%s;
                       COMMIT;"""

UPDATE_TYPE_ID = """BEGIN;
                    UPDATE Product
                    SET type_id =%s
                    WHERE prod_id =%s;
                    COMMIT;"""

UPDATE_DATE_IN = """BEGIN;
                    UPDATE Product
                    SET date_in = NULL
                    WHERE prod_id = %s;
                    COMMIT;"""

REMOVE_DATE_OUT = """BEGIN;
                     UPDATE Product
                     SET date_out = NULL
                     WHERE prod_id = %s;
                     COMMIT;"""

UPDATE_DATE_OUT = """BEGIN;
                     SET @mydate = %s;
                     UPDATE Product
                     SET date_out = CASE
                         WHEN @mydate > date_in THEN @mydate
                         ELSE date_out
                         END
                     WHERE prod_id = %s;
                     COMMIT;"""

UPDATE_PERIOD = """BEGIN;
                   UPDATE Product
                   SET period = %s
                   WHERE prod_id = %s;
                   COMMIT;"""

UPDATE_QUANTITY = """BEGIN;
                     UPDATE Product
                     SET quantity = %s
                     WHERE prod_id = %s;
                     COMMIT;"""
