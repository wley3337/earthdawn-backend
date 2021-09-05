import bcrypt


def create_password_digest(password):
    """
    Given a password, it creates a bcrypt password digest
    with 12 rounds of salt/work. It converts password to
    'utf-8' before encryption.
    """
    utf_pass = password.encode('utf-8')
    return bcrypt.hashpw(utf_pass, bcrypt.gensalt(rounds=12))
