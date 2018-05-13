*freezer* `GET`
------------
To obtain the informations about all freezer associated to a specific user identified by its token.

The prototype of the request:
```
localhost:5000/freezers/<token>
```
Parameters:
- `<token>`: A user's token

This request returns a JSON object of the form:
```
[
    {
        "freezer_id": 1,
        "freezer_name": "frigo 1",
        "number_boxes": 4
    },
    ...
]
```
### A simple example
This is a simple example using the `curl` tool:
```
>>> curl http://localhost:5000/freezers/5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92
```

---

*freezer* `POST`
--------------
The prototype of the request:
```
localhost:5000/freezers/<token>
```
Parameters:
- `<token>`: A user's token


It is possible to add a new freezer for a specific user identified by its token.
The post method need to be used to add it and has to respect the JSON format which follows
the following schema:
```
{
    "num_boxes": "4",
    "name": "my_name"
}
```
- `num_boxes`: An `integer` that represent the number of boxes.
- `name`: An `string` that represents the new name given to the freezer.
### A simple example
This is a simple example using the `curl` tool:
```
>>> curl -H "Content-Type: application/json" -X POST -d '{"num_boxes":"4", "name":"toy"}' http://localhost:5000/freezers/5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92
```

---

---

*freezer* `PUT`
--------------
The prototype of the request:
```
localhost:5000/freezers/<token>
```
Parameters:
- `<token>`: A user's token


It is possible to update an existing freezer if you want to change the name of your freezer or/and change the number of
boxes that it has. The Put request uses a JSON to send data to the server. The JSON format uses the following schema:
```
{
    "freezer_id": the id of an exisitng freezer,
    "num_boxes": "4",
    "name": "my_name"
}
```
- `freezer_id`: An `integer` that represents the id of an existing freezer that belongs to the user with the token given.
- `num_boxes`: An `integer` that represent the number of boxes. Can be leaved empty if we do not want to update the number of boxes.
- `name`: An `string` that represents the new name given to the freezer. Can be leaved empty if we do not want to update the name.


### A simple example
This is a simple example using the `curl` tool:
```
>>> curl -H "Content-Type: application/json" -X PUT -d '{"freezer_id":3, "num_boxes":"", "name":"toy"}' http://localhost:5000/freezers/5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92
```

---

*freezer* `DELETE`
--------------
The prototype of the request:
```
localhost:5000/freezers/<token>
```
Parameters:
- `<token>`: A user's token


It is possible to delete a freezer. But to delete this one, it needs to follows some conditions.
This freezer should be empty and do not have an history. In other words, this freezer must not have any link with a product.
The DELETE request uses a JSON to send data to the server. The JSON format uses the following schema:
```
{
    "freezer_id": the id of an exisitng freezer
}
```
- `freezer_id`: An `integer` that represents the id of an existing freezer that belongs to the user with the token given.

### A simple example
This is a simple example using the `curl` tool:
```
>>> curl -H "Content-Type: application/json" -X DELETE -d '{"freezer_id": "an exisitng id"}' http://localhost:5000/freezers/5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92
```
