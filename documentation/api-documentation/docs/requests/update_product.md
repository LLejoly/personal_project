*add_product* `POST`
-------------
To update an existing product for an exisitng user into the database.
You can use this request. A JSON object must be sent with a specific architecture.
If all information are correct a status code 200 will be returned.
Otherwise an error status code is returned with a JSON object.
This JSON object has two fields `details` and `status`.
The `status` field contains the error status code sent and `details` field contains a text that explains the reason of that status code.

The route of the request is the following one:
```
localhost:5000/update_product/<freezer_id>/<box_num>/<inside>/<token>
```
Parameters:
- `<freezer_id>`: An `integer` that represents the id of an existing freezer that belongs to the user with the token given. If we want to select all freezers that belongs to a user the id 0 must be specified.
- `<box_num>`: An `integer` that identifies the box where the product is stored.
- `<prod_num>`: An `integer` that identifies the product inside the box previously referred.
- `<inside>`: An `integer` that specifies if the product is still in the freezer or not. If the integer given is strictly higher than 0 than it means it is inside otherwise it is outside.
- `<token>`: A user's token that corresponds to an existing account.

The strcuture of the  JSON object to send:
```
{
    "product_name": "name",
    "text_descr": "description",
    "freezer_id": number,
    "type_id": number,
    "date_in" datetime YYY-MM-DD,
    "date_out" datetime YYY-MM-DD,
    "period":" number,
    "box_num": number,
    "prod_num": number,
    "quantity": number
}
```
Explanation of the  JSON object:

- `product_name`: A `string` that represents the name given to the new product.
- `text_descr`: A `string` that represents the description of the product.
- `freezer_id`: An `integer` that represents the id of an existing freezer that belongs to the user with the token given.
- `type_id`: An `integer` that represents the identifier of an existing product type. TO know the different product types you can refer to the request `types`.
- `date_in`: A `datetime` with the format YYYY-MM-DD that represents the date when the product was added to the freezer.
- `period`: An `integer` that represents the period in months for which the product can stay in the freezer.
- `box_num:` An `integer` that represents the freezer box where to add the new product.
- `prod_num`: An `integer` that represents the an available identifier inside the selected box to identify the product inside this box.
- `quantity`: An `integer` that represents the quantity in terms of people for which the product can be consumed.

### A simple example
This is a simple example using the `curl` tool:
```
>>> curl -d '{"product_name":"Glace au citronnee","text_descr":"", "freezer_id":"","type_id":"","date_in":"", "date_out": "", "period":"","box_num":"","prod_num":"","quantity":""}' -H "Content-Type: application/json" -X POST http://localhost:5000/update_product/1/1/1/1/5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92

```