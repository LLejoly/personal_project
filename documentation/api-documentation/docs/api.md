Freezer User's Guide
==========================

Introduction
------------
The Freezer API is an API used to retrieve data from the smart freezer application. TO use it,
you need to run the api by running the bash script `flask_run.sh`.
The database server need to be active.

Installation
------------
To use the API no installation of specific tools are required.
It can be used with `curl` request, for instance.

Commands
========
A couple of commands can be used. These commands are explained above, for most of them a user's token is needed.
This token can be obtain by the user on the login page. If you do not have an account you can create one on the 
register page.

*check_token* `GET`
------------------
Gives the possibility to check the validity of a token. If this one is valid
a response with the status code 200 is returned in other cases a response with the status code 400 is returned.

The prototype of the request:
```
localhost:5000/check_token/<token>
```
Parameters:

- `<token>`: A user's token


*types* `GET`
-------------
To obtain the different types of products that can be used with the database.
You can use this request. You will obtain a JSON that contains serveral information
about the different types.

The prototype of the request:
```
localhost:5000/types/<token>
```
Parameters:

- `<token>`: A user's token

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
- `type_name_en`: The type name in English
- `type_name_fr`: The type name in French

### A simple example
This is a simple example using the `curl` tool:
```
>>> curl 'http://localhost:5000/types/5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92'
```

---

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

---

*freezer_next_id* `GET`
-------------
The prototype of the request:
```
localhost:5000/freezer_next_id/<freezer_id>/<token>
```
Parameters:
- `freezer_id`: An `integer` that represents the id of an existing freezer that belongs to the user with the token given.
- `<token>`: A user's token

To obtain the next identification of all boxes of a given freezer for the add of a new product.

This request returns a JSON object of the form:
```
{
  "1": 8, 
  "2": 3, 
  "3": 4, 
  "4": 3
}
```
Where for instance, "1" represents the box number and 8 the next available id for the product in the box 1.


### A simple example
This is a simple example using the `curl` tool:
```
>>> curl 'http://localhost:5000/freezer_next_id/1/5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92'
```

---


*add\_product* `POST`
--------------------

```
{
    "product_name":" a name",
    "text_descr":"a free description",
    "freezer_id":"1",
    "type_id":"1",
    "date_in":"2017-12-26",
    "period":"6",
    "box_num":"1",
    "prod_num":"3",
    "quantity":"4"
}
```

---

*get\_product* `GET`
-------------------

---

*update\_product* `POST`
-----------------------
