# This file should contain records you want created when you run flask db seed.
#
# Example:
# from yourapp.models import User

# initial_user = {
#     'username': 'superadmin'
# }
# if User.find_by_username(initial_user['username']) is None:
#     User(**initial_user).save()

from db.model_seeds.user_seeds import seed_users

seed_users()

from db.model_seeds.talent_seeds.seed_all_tallents import seed_talents

seed_talents()
