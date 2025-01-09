# Alx
# Authentication for Event Management API

## Authentication Setup
- The API uses Django REST Framework's `TokenAuthentication`.
- All endpoints require a valid token in the `Authorization` header.

## How to Obtain a Token
1. Register or log in to the system.
2. Use `/api/token/` to obtain a token for your user.

## Example Request
```bash
curl -X GET http://127.0.0.1:8000/api/events/ \
-H "Authorization: Token <your_token>"
