from app import db

class Guest(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  group_id = db.Column(db.Integer)
  name = db.Column(db.String(80))
  email = db.Column(db.String(120))
  is_primary = db.Column(db.Integer)

  def __init__(self, group_id, name, email, is_primary):
    self.group_id = group_id
    self.name = name
    self.email = email
    self.is_primary = is_primary
