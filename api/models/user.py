from api.services.database import db


class User(db.Model):
    """
    User model. Primary association and ownership
    reference for characters
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False, index=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    password_digest = db.Column(db.String, nullable=False)

    @classmethod
    def find_by_username(cls, username):
        return User.query.filter(User.username == username).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        """Representation of class: Username"""
        return '<User %r >' % self.username
