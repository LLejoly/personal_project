*custom_tendency* `GET`
------------------
Gives the possibility to obtain a personalized tendency of a specific based on his previous consumptions and the products that are in his freezers.
If the parameters  given are correct a JSON and the status code 200 are returned.
Otherwise an error status code is returned with a JSON object.
This JSON object has two fields `details` and `status`.
The `status` field contains the error status code sent and `details` field contains a text that explains the reason of that status code.

The route of the request is the following one:
```
localhost:5000/custom_tendency/<token>
```
Parameters:

- `<token>`: A user's token that corresponds to an existing account.


Example of the JSON object returned:
```
{
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
  		}
        ...
    ]
}
```
Explanation of the JSON object:

- `freq`: An `integer` that represents the number of time the product type appears in the database.
- `latest`: The date of the last product of that type that left the user’s freezers.
- `type_id` : An `integer` that represents the identifier of an existing product type. To know the different product types you can refer to the request `types`.
- `type_name_en`: A `string` that represents the name of the product type in English
- `type_name_fr`: A `string` that represents the name of the product type in French