
# Daily Chronicle API Server


## Overview
This is an API server for [DailyChronicle](https://github.com/DeepProgram/DailyChronicle.git) web
## Features

**1. User Signup and Login System**

The API server provides endpoints for user signup and login, enabling users to create accounts and securely authenticate themselves.

- Signup
    - Endpoint: **/signup**
    - Method: POST
    - Request Payload:
        ```bash
        {
         "username": "your_username",
         "password": "your_password"
        }
        ```
    - Response:
        ```bash
        {
         "hint": "user_signup_successful",
         "code": 1,
         "token": token
        }
        ```
- Login
    - Endpoint: **/login**
    - Method: GET
    - Request Query:
        ```bash
        username=username
        password=password
        ```
    - Response:
        ```bash
        {
         "hint": "login_successful",
         "code": 1,
         "token": token
        }
**2. Secure Password Storage**

User passwords are securely hashed using bcrypt before storing them in the database, ensuring that sensitive information is protected.

**3. JSON Web Token (JWT) Authentication**

Upon successful login, the API issues a JSON Web Token (JWT) to the user, which is used to authenticate subsequent requests to protected routes.

**4. SQL Database with SQLAlchemy**

The API server utilizes SQLAlchemy, a popular Object-Relational Mapping (ORM) library, to interact with a SQL database for storing user data and daily notes.

**5. Daily Notes Management**

Users can create, read, update, and delete daily notes using dedicated endpoints.

- **Get All Notes**
    - Endpoint: **/note/view**
    - Method: GET
    - Authorization: Bearer your_jwt_token
    - Response:
    
    ```bash
    [
        {
            "note_id": 1,
            "note_title": "Note Title 1",
            "note_body": "Note body text...",
            "created_at": 1690899018,
            "modified_at": 1690899043
        },
        {
            "id": 2,
            "title": "Note Title 2",
            "body": "Note body text...",
            "created_at": 1690899055,
            "modified_at": 1690899070
        }
    ]

- **Add a New Note**
    - Endpoint: **/note/add**
    - Method: POST
    - Authorization: Bearer your_jwt_token
    - Request Payload:
        ```bash
        {
         "note_title": "New Note Title",
         "note_body": "New note body text..."
        }```

    - Response:
        ```bash
        {
         "hint": "note_add_successful",
         "code": 1
        }
        ```
- **Edit a Note**
    - Endpoint: **/note/update**
    - Method: PUT
    - Authorization: Bearer your_jwt_token
    - Request Payload:
        ```bash
        {
         "note_id": 1
         "note_title": "New Note Title",
         "note_body": "New note body text..."
        }```

    - Response:
        ```bash
        {
         "hint": "notes_updated",
         "code": 1
        }```
- **Delete a Note**
    - Endpoint: **/note/delete**
    - Method: DELETE
    - Authorization: Bearer your_jwt_token
    - Request Payload:   
        ```bash
        {
         "note_id": 1
        }```

    - Response:
        ```bash
        {
         "hint": "note_deleted",
         "code": 1
        }
        ```

**6. Error Handling**

The API server provides informative error responses to help users and developers understand and address potential issues.

- **400 Bad Request**: Invalid request data or missing required fields.
- **401 Unauthorized**: The request lacks valid authentication credentials.
- **403 Forbidden**: The user is not authorized to access the requested resource.
- **404 Not Found**: The requested resource could not be found.
- **500 Internal Server Error**: An unexpected error occurred on the server.

## Motivation
The motivation behind creating and maintaining **DailyChronicleServer** stems from a strong belief in the power of journaling to promote personal growth, reflection, and well-being. In today's fast-paced digital world, maintaining a daily journal has become increasingly important as a means to capture our thoughts, experiences, and emotions in a secure and private environment
## Fronetend
Setup [DailyChronicle](https://github.com/DeepProgram/DailyChronicle.git) for connection between backend and frontend
## Requirements
+ [FastAPI](https://fastapi.tiangolo.com/)
+ [SQLAlchemy](https://www.sqlalchemy.org/)
+ [Python-Jose [Cryptography]](https://python-jose.readthedocs.io/en/latest/)
+ [Passlib [Bcrypt]](https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html)
## Installation

Install **DailyChronicleServer** with python

```bash
  git clone https://github.com/DeepProgram/DailyChronicleServer.git
  cd DailyChronicleServer
  pip install -r requirements.txt
  uvicorn main:app --reload
```
    