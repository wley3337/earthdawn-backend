# API for Earthdawn front end system

## Deployment

set `APP_SETTINGS= "config.ProductionConfig"`

## Useful python tidbits

- Lock requirements.text in with: `pip freeze > requirements.txt`
- Install requirements.text with: `pip install -r requirements.txt`

## Docs for packages

[python-socketio](https://github.com/miguelgrinberg/python-socketio)
[SocketIO General docs](https://socket.io/docs/v4/#What-Socket-IO-is)
[flask-jwt-extended](https://flask-jwt-extended.readthedocs.io/en/stable/installation/)
[SQLAlchemy](https://docs.sqlalchemy.org/en/14/)
[Flask-DB](https://github.com/nickjj/flask-db)

## Auth Pattern

Auth is done through JWT token set in an HTTP only cookie. It is paired with a `X-CSRF-TOKEN` header that contains the `csrf_access_token`. This must be sent to every protected route. The key for creating the JWT is stored in the env var: `JWT_SECRET_KEY`.

```javascript
headers:{
  // ...,
  'X-CSRF-TOKEN': getCookie('csrf_access_token')
  // ...,
}
```

## Local setup:

To facilitate cookie auth you need to setup a local nginx server that serves both the front end code and back end code from the same domain.
