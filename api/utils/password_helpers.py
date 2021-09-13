import bcrypt


def create_password_digest(password):
    """
    Given a password, it creates a bcrypt password digest
    with 12 rounds of salt/work. It converts password to
    'utf-8' before encryption.
    """
    utf_password = password.encode('utf-8')
    return bcrypt.hashpw(utf_password,
                         bcrypt.gensalt(rounds=12)).decode('utf-8')


def password_matches(password, password_digest):
    """
    Returns true if password genarates password digest
    """

    utf_password = password.encode('utf-8')
    utf_password_digest = password_digest.encode('utf-8')

    if bcrypt.checkpw(utf_password, utf_password_digest):
        return True
    else:
        return False
