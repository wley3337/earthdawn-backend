from api.utils.password_helpers import create_password_digest
from api.models.user import User

user_seeds = [{
    "username": "test1",
    "password_digest": create_password_digest('123'),
    "first_name": "test1first",
    "last_name": "test1last"
}, {
    "username": "test2",
    "password_digest": create_password_digest('123'),
    "first_name": "test2first",
    "last_name": "test2Last"
}]


def seed_users():
    """Seeds User if username is not found"""
    for user_seed in user_seeds:
        if User.find_by_username(user_seed["username"]) is None:
            print("{0} username not found".format(user_seed["username"]))
            saved_user = User(**user_seed).save()
            print("{0} user saved".format(saved_user.username))
        else:
            print("{0} username found".format(user_seed["username"]))
