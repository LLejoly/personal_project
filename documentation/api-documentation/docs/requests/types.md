*types* `GET`
-------------
To obtain the different types of products that can be used with the database.
You can use this request. You will obtain a JSON that contains serveral information
about the different types and the status code 200 if the information given are corrects.
Otherwise an error status code is returned with a JSON object.
This JSON object has two fields `details` and `status`.
The `status` field contains the error status code sent and `details` field contains a text that explains the reason of that status code.

The route of the request is the following one:
```
localhost:5000/types/<token>
```
Parameters:

- `<token>`: A user's token that corresponds to an existing account.

This request returns a JSON object of the form:
```
[
    {
        "type_id": 1,
        "type_name_en": "soup",
        "type_name_fr": "soupe"
    },
    {
        "type_id": 2,
        "type_name_en": "meal soup",
        "type_name_fr": "soupe repas"
    },
    ...
]
```
Explanation of the  JSON object:

- `type_id`: An `integer` that represents the id of the product's type
- `type_name_en`: A `string` that represents the type name in English
- `type_name_fr`: A `string` that represents the The type name in French

### A simple example
This is a simple example using the `curl` tool:
```
>>> curl 'http://localhost:5000/types/5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92'
```

