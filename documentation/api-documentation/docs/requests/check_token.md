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

