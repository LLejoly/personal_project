PRODUCT_HEADER = ['product_name',
                  'text_descr',
                  'freezer_id',
                  'type_id',
                  'date_in',
                  'period',
                  'box_num',
                  'prod_num',
                  'quantity']
"""
SQL request to return the possible types of products 
that are present in the database.
"""
GET_TYPES = """SELECT *
               FROM Description_type"""

"""
SQL request to return all information about a product given.
Parameters passed to the request in that order:
- the user token
- the freezer id
- the box number
- the product number
"""
GET_A_PRODUCT = """SELECT *
                   FROM Product
                   WHERE token = %s 
                   AND freezer_id = %s 
                   AND box_num = %s 
                   AND prod_num = %s"""

"""
SQL request to return all information about a product which is inside a freezer.
Parameters passed to the request in that order:
- the user token
- the freezer id
- the box number
- the product number
"""
GET_A_PRODUCT_INSIDE = """SELECT *
                   FROM Product
                   WHERE token = %s 
                   AND freezer_id = %s 
                   AND box_num = %s 
                   AND prod_num = %s 
                   AND date_out IS NULL"""

"""
SQL request to return all information about a product which is outside a freezer.
Parameters passed to the request in that order:
- the user token
- the freezer id
- the box number
- the product number
"""
GET_A_PRODUCT_OUTSIDE = """SELECT *
                           FROM Product
                           WHERE token = %s 
                           AND freezer_id = %s 
                           AND box_num = %s 
                           AND prod_num = %s 
                           AND date_out IS NOT NULL"""

"""
SQL request to return information about a specific freezer given the freezer id.
Parameters passed to the request in that order:
- a freezer id
"""
GET_SPECIFIC_FREERZER = """SELECT freezer_id,
                                  number_boxes,
                                  freezer_name 
                           FROM Description_freezer WHERE freezer_id = %s"""
"""
Returns a list of freezers associated to a specific token.
Parameters passed to the request in that order:
- a user token
"""
GET_FREEZERS = """SELECT Description_freezer.freezer_id,
                         Description_freezer.number_boxes,
                         Description_freezer.freezer_name 
                  FROM Description_freezer INNER JOIN List_freezer
                  WHERE token = %s AND Description_freezer.freezer_id = List_freezer.freezer_id"""
"""
Returns a list of [[prod_num, box_num]] for a given freezer and token.
Parameters passed to the request in that order:
- a user token
- freezer id
"""
GET_PROD_NUM_LIST = """SELECT prod_num, box_num
                       FROM Product
                       WHERE token = %s AND freezer_id = %s AND date_out IS NULL 
                       ORDER BY box_num, prod_num"""

"""
Return a list of products inserted into the database and sorted by
frequency in the descending order
"""
GET_GLOBAL_TENDENCY = """SELECT Product_to_type.type_id,
                                Description_type.type_name_en,
                                Description_type.type_name_fr,
                                COUNT(*) AS freq
                         FROM (Product_to_type
                         INNER JOIN Description_type ON  Product_to_type.type_id = Description_type.type_id)
                         GROUP BY Product_to_type.type_id 
                         ORDER BY freq DESC;"""

"""
Return a personalized list of products present in the freezer of a user.
These products are sorted by frequency, by type, and by the latest product of that type taken from the freezers.
If all products of a certain type have never been taken then the result of the last type of product taken will be null.
Parameters passed to the request in that order:
-a user token
"""
GET_PERSONALIZED_TENDENCY = """SELECT Product.type_id,
                                      Description_type.type_name_en,
                                      Description_type.type_name_fr,
                                      DATE_FORMAT(max(Product.date_out), '%%Y-%%m-%%d') AS latest,
                                      COUNT(*) AS freq 
                               FROM (Product INNER JOIN Description_type ON Product.type_id = Description_type.type_id)
                               WHERE Product.token = %s
                               GROUP BY Product.type_id
                               ORDER BY latest DESC, freq DESC;"""
"""
GET the types used by a user.
Parameters passed to the request in that order:
-a user token
"""
GET_TYPES_USED = """SELECT  DISTINCT type_id
                    FROM Product 
                    WHERE token = %s
                    AND date_out IS NULL 
                    ORDER BY type_id ASC;"""

param_all = """FROM ((Product
                      INNER JOIN Description_product
                        ON Product.descr_id = Description_product.descr_id
                          AND Product.token = %s)
                            INNER JOIN Description_freezer
                              ON Product.freezer_id = Description_freezer.freezer_id)"""

param_all_inside = """FROM ((Product
                      INNER JOIN Description_product
                        ON Product.descr_id = Description_product.descr_id
                          AND Product.token = %s
                          AND Product.date_out IS NULL)
                            INNER JOIN Description_freezer
                              ON Product.freezer_id = Description_freezer.freezer_id)"""

param_all_outside = """FROM ((Product
                      INNER JOIN Description_product
                        ON Product.descr_id = Description_product.descr_id
                          AND Product.token = %s
                          AND Product.date_out IS NOT NULL)
                            INNER JOIN Description_freezer
                              ON Product.freezer_id = Description_freezer.freezer_id)"""

param_one = """FROM ((Product
                      INNER JOIN Description_product
                        ON Product.descr_id = Description_product.descr_id
                          AND Product.token = %s
                          AND Product.freezer_id = %s)
                            INNER JOIN Description_freezer
                              ON Product.freezer_id = Description_freezer.freezer_id)"""

param_one_inside = """FROM ((Product
                      INNER JOIN Description_product
                        ON Product.descr_id = Description_product.descr_id
                          AND Product.token = %s
                          AND Product.freezer_id = %s
                          AND Product.date_out IS NULL)
                            INNER JOIN Description_freezer
                              ON Product.freezer_id = Description_freezer.freezer_id)"""

param_one_outside = """FROM ((Product
                      INNER JOIN Description_product
                        ON Product.descr_id = Description_product.descr_id
                          AND Product.token = %s
                          AND Product.freezer_id = %s
                          AND Product.date_out IS NOT NULL)
                            INNER JOIN Description_freezer
                              ON Product.freezer_id = Description_freezer.freezer_id)"""


def generate_product_query(param):
    select_col = """SELECT Product.freezer_id,
                           Description_freezer.freezer_name,
                           Product.box_num,
                           Product.prod_num,
                           DATE_FORMAT(Product.date_in, '%%Y-%%m-%%d') AS date_formatted_in,
                           DATE_FORMAT(Product.date_out, '%%Y-%%m-%%d') AS date_formatted_out,
                           Product.period,
                           Product.quantity,
                           Product.type_id,
                           Product.descr_id,
                           Description_product.product_name,
                           Description_product.text_descr """
    if param == "all":
        return select_col + param_all
    if param == "all-one":
        return select_col + param_one
    if param == "inside":
        return select_col + param_all_inside
    if param == "inside-one":
        return select_col + param_one_inside
    if param == "outside":
        return select_col + param_all_outside
    if param == "outside-one":
        return select_col + param_one_outside

    return


"""
SQL request to insert a new freezer for a specific user.
Parameters passed to the request in that order:
- number of  boxes
- freezer name
- a user token
"""
INSERT_FREEZER = """BEGIN;
                    INSERT INTO Description_freezer (number_boxes, freezer_name) VALUES(%s, %s);
                    INSERT INTO List_freezer (freezer_id, token) VALUES(LAST_INSERT_ID(),%s);
                    COMMIT;"""

"""
SQL request to insert a new product for a specific user.
Parameters passed to the request in that order:
- product name
- product description
- type of the product
- a user token
- a freezer id
- a type id
- a date of input
- a period
- a box number
- a product number inside the  box
- a quantity
"""

INSERT_PRODUCT = """BEGIN;
                    INSERT INTO Description_product (product_name, text_descr)  VALUES (%s, %s);
                    INSERT INTO Product_to_type (descr_id, type_id)  VALUES (LAST_INSERT_ID(), %s);
                    INSERT INTO Product (token, descr_id, freezer_id, type_id, date_in,
                    period, box_num, prod_num, quantity) VALUES(%s,LAST_INSERT_ID(),%s,%s,%s,%s,%s,%s,%s) ;
                    COMMIT;"""

"""
SQL request to update product name.
Parameters passed to the request in that order:
- product name
- product description id
"""

UPDATE_PRODUCT_NAME = """BEGIN;
                         UPDATE Description_product
                         SET product_name =%s
                         WHERE descr_id =%s;
                         COMMIT;"""

"""
SQL request to update product description.
Parameters passed to the request in that order:
- product description
- product description id
"""
UPDATE_TEXT_DESCR = """BEGIN;
                       UPDATE Description_product
                       SET text_descr =%s
                       WHERE descr_id =%s;
                       COMMIT;"""

"""
SQL request to update freezer name and boxes.
Parameters passed to the request in that order:
- freezer name
- number of boxes
- freezer id
"""
UPDATE_FREEZER_NAME_AND_BOXES = """BEGIN;
                                   UPDATE Description_freezer
                                   SET freezer_name =%s,
                                       number_boxes=%s
                                   WHERE freezer_id =%s;
                                   COMMIT;"""

"""
SQL request to update freezer id of a product.
Parameters passed to the request in that order:
- freezer id
- product id
"""
UPDATE_FREEZER_ID = """BEGIN;
                       UPDATE Product
                       SET freezer_id =%s
                       WHERE prod_id =%s;
                       COMMIT;"""

"""
SQL request to update the type a product.
Parameters passed to the request in that order:
- type id
- product description id
"""
UPDATE_TYPE_ID = """BEGIN;
                    SET @newtype = %s;
                    UPDATE Product
                    SET type_id = @newtype
                    WHERE prod_id =%s;
                    UPDATE Product_to_type
                    SET type_id = @newtype
                    WHERE descr_id = %s;
                    COMMIT;"""

"""
SQL request to update date of input of a product.
Parameters passed to the request in that order:
- date of input
- product id
"""
UPDATE_DATE_IN = """BEGIN;
                    UPDATE Product
                    SET date_in = %s
                    WHERE prod_id = %s;
                    COMMIT;"""

"""
SQL request to remove the output date of a product.
Parameters passed to the request in that order:
- product id
"""
REMOVE_DATE_OUT = """BEGIN;
                     UPDATE Product
                     SET date_out = NULL
                     WHERE prod_id = %s;
                     COMMIT;"""

"""
SQL request to update date of output of a product.
Parameters passed to the request in that order:
- date of output
- product id
"""
UPDATE_DATE_OUT = """BEGIN;
                     SET @mydate = %s;
                     UPDATE Product
                     SET date_out = CASE
                         WHEN @mydate > date_in THEN @mydate
                         ELSE date_out
                         END
                     WHERE prod_id = %s;
                     COMMIT;"""

"""
SQL request to update the period of a product.
Parameters passed to the request in that order:
- period
- product id
"""
UPDATE_PERIOD = """BEGIN;
                   UPDATE Product
                   SET period = %s
                   WHERE prod_id = %s;
                   COMMIT;"""

"""
SQL request to update the quantity of a product.
Parameters passed to the request in that order:
- quantity
- product id
"""
UPDATE_QUANTITY = """BEGIN;
                     UPDATE Product
                     SET quantity = %s
                     WHERE prod_id = %s;
                     COMMIT;"""

"""
SQL request to update the emplacement of a product.
Parameters passed to the request in that order:
- freezer id
- box number
- product number
- product id
"""
UPDATE_EMPLACEMENT = """BEGIN;
                     UPDATE Product
                     SET freezer_id = %s,
                         box_num = %s,
                         prod_num = %s
                     WHERE prod_id = %s;
                     COMMIT;"""

"""
SQL request to delete a freezer.
Parameters passed to the request in that order:
- freezer id
"""
DELETE_FREEZER = """BEGIN;
                    SET @freezeID = %s;
                    DELETE FROM List_freezer
                    WHERE freezer_id = @freezeID;
                    DELETE FROM Description_freezer
                    WHERE freezer_id = @freezeID;
                    COMMIT;"""
