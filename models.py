from app import db

class Guest(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  group_id = db.Column(db.Integer)
  name = db.Column(db.String(80))
  email = db.Column(db.String(120))
  primary = db.Column(db.Boolean())

  def __init__(self, group_id, name, email, primary=False):
    self.group_id = group_id
    self.name = name
    self.email = email
    self.primary = primary
