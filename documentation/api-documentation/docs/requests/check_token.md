*check_token* `GET`
------------------
Gives the possibility to check the validity of a token. If this one is valid
a response with the status code 200 is returned.
Otherwise an error status code is returned with a JSON object.
This JSON object has two fields `details` and `status`.
The `status` field contains the error status code sent and `details` field contains a text that explains the reason of that status code.

The route of the request is the following one:
```
localhost:5000/check_token/<token>
```
Parameters:

- `<token>`: A user's token that corresponds to an existing account.

