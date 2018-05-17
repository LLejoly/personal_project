*get_product* `GET`
------------------
Gives the possibility to retrieve products of a specific user by specifying some parameters to the request
If the parameters given are correct a JSON and the status code 200 are returned.
Otherwise an error status code is returned with a JSON object.
This JSON object has two fields `details` and `status`.
The `status` field contains the error status code sent and `details` field contains a text that explains the reason of that status code.

The route of the request is the following one:
```
localhost:5000/get_product/<param>/<freezer_id>/<token>
```
Parameters:

- `<params>`: A `string` that define the parameter that we want three parameters are possible:
  - `all`: Selects all products.
  - `inside`: Selects only products that are inside freezers.
  - `outside`: Selects only products that are outside freezers.
- `<freezer_id>`: An `integer` that represents the id of an existing freezer that belongs to the user with the token given. If we want to select all freezers that belongs to a user the id 0 must be specified.
- `<token>`: A user's token that corresponds to an existing account.


Example of the JSON object returned:
```
[
  {
    "box_num": 1, 
    "date_formatted_in": "2016-12-31", 
    "date_formatted_out": "2017-03-02", 
    "descr_id": 2, 
    "freezer_id": 1, 
    "freezer_name": "frigo 1", 
    "period": 6, 
    "prod_num": 2, 
    "product_name": "glace vanille", 
    "quantity": 1, 
    "text_descr": "glace maison au aromatis\u00e9e \u00e0 la vanille", 
    "type_id": 24
  },
  {
    "box_num": 1, 
    "date_formatted_in": "2017-12-26", 
    "date_formatted_out": null, 
    "descr_id": 4, 
    "freezer_id": 1, 
    "freezer_name": "frigo 1", 
    "period": 6, 
    "prod_num": 4, 
    "product_name": "Soupe de No\u00ebl", 
    "quantity": 4, 
    "text_descr": "Soupe \u00e0 base de tomate, brocolli et poisson", 
    "type_id": 1
  },
  ...
  ] 
```
Explanation of the JSON object:

- `box_num`: An `integer` that represents the freezer box where the product is stored.
- `date_formatted_in`: Represents the input date of the product in the freezer. The format of the date is YYYY-MM-DD.
- `date_formatted_out`: Represents the output date of the product in the freezer. The format of the date is YYYY-MM-DD. If there is no output the value is simply null.
- `descr_id`: An `integer` that represent the identifier of the product description.
- `freezer_id`: An `integer` that represents the identifier of the freezer.
- `freezer_name`; A `string` that represents the freezer name.
- `period`: An `integer` that represents the period in months for which the product can stay in the freezer.
- `prod_num`: An `integer`that represents the identifier of the product inside the freezer box.
- `product_name`: A `string` that represents the name of the product.
- `text_descr`: A `string` that represents the description of the product.
- `type_id`: An `integer` that represents  the type identifier of the product.
