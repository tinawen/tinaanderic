import os
from flask import Flask, render_template, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy

# -----------CONFIGURATION------------
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

# -------------MODELS-------------
class Guest(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  group_id = db.Column(db.Integer)
  name = db.Column(db.String(80))
  email = db.Column(db.String(120))
  is_primary = db.Column(db.Integer)
  coming = db.Column(db.Boolean)
  meal_selection = db.Column(db.Integer)
  last_modified = db.Column(db.DateTime)
  token = db.Column(db.String(20))

  def __init__(self, group_id, name, email, is_primary, token):
    self.group_id = group_id
    self.name = name
    self.email = email
    self.is_primary = is_primary
    self.token = token

# -------------VIEWS-------------
@app.route("/")
def index():
  return render_template('index.jinja2', active="home")

@app.route("/rsvp")
def rsvp():
  return render_template('rsvp.jinja2', active="rsvp")

@app.route("/rsvp/<token>")
def rsvp_with_token(token):
  guests = Guest.query.filter_by(token=token).all()
  if guests:
    return render_template('rsvp_with_token.jinja2', active="rsvp", guests=guests)
  else:
    return render_template('rsvp_with_bad_token.jinja2', active="rsvp")

@app.route("/event")
def event():
  return render_template('event.jinja2', active="event")

@app.route("/accommodation")
def accommodation():
  return render_template('accommodation.jinja2', active="accomodation")

@app.route("/gallery")
def gallery():
  return render_template('gallery.jinja2', active="gallery")

@app.route("/stories")
def stories():
  return render_template('stories.jinja2', active="stories")

@app.route("/registry")
def registry():
	return render_template('registry.jinja2', active="registry")

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
