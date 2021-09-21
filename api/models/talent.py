# {
#     "id": "TC6",
#     "name": "",
#     "attribute": "dexterity",
#     "base_modifier": 3,  #default 0
#     "action": True,
#     "skill_use": False,
#     "requires_karma": False,
#     "strain": 0,
#     "discipline_talent": ["weaponsmith"],
#     "description": """"""
# },
from api.services.database import db


class Talent(db.Model):
    """
    Talent model with fixed ids for core talents.
    """
    __tablename__ = 'talents'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    attribute = db.Column(db.String, nullable=False)
    base_modifier = db.Column(db.Integer, default=0)
    action = db.Column(db.Boolean, nullable=False)
    skill_use = db.Column(db.Boolean, nullable=False)
    requires_karma = db.Column(db.Boolean, nullable=False)
    strain = db.Column(db.Integer, nullable=False, default=0)
    description = db.Column(db.Text, nullable=False)
    discipline_talent = db.Column(db.ARRAY(db.String), nullable=False)

    @classmethod
    def find_by_id(cls, id):
        talent = Talent.query.filter(Talent.id == id).first()
        return talent

    def save(self):
        """Persists record to database"""
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        """Representation of class: Talent"""
        return '<Talent %r >' % self.name
