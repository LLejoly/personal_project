Smart freezer User's Guide
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
a response with the status 200 is returned in other cases a response with the status 400 is returned.
```
localhost:5000/check_token/<token>
```
Parameters:

- `<token>`: A user's token


*types* `GET`
-------------
It is possible to obtain the different types of products present in the database.
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
- `type_name_en`: The name of the type in English
- `type_name_fr`: The name of the type in French

### A simple example
This is a simple example using the `curl` tool:
```
>>> curl 'http://localhost:5000/types/5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92'
```

---

*freezer* `GET`
------------
To obtain the informations about all freezer associated to a specific user identified by its token.
```
localhost:5000/freezers/<token>
```
Parameters:
* `<token>`: A user's token

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
It is possible to add a new freezer for a specific user identified by its token.
The post method need to be used to add it and has to respect the JSON format which follows
the following schema:
```
{
    "num_boxes": "4",
    "name": "my_name"
}
```
The post request is:
```
localhost:5000/freezers/<token>
```
### A simple example
This is a simple example using the `curl` tool:
```
>>> curl -H "Content-Type: application/json" -X POST -d '{"num_boxes":"4","name":"toy"}' http://localhost:5000/freezers/5b68dab9a6c606171473091280898d1c9e581159173d6ba267f3418a6573ae92
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
