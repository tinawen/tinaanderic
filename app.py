import binascii
import os
from flask import Flask, render_template, redirect, url_for, request
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
  return render_template('index.html', active="home")

@app.route("/rsvp")
def rsvp():
  return render_template('rsvp.html', active="rsvp")

@app.route("/rsvp/<token>")
def rsvp_with_token(token):
  guests = Guest.query.filter_by(token=token).all()
  if guests:
    return render_template('rsvp_with_token.html', active="rsvp", guests=guests)
  else:
    return render_template('rsvp_with_bad_token.html', active="rsvp")

@app.route("/event")
def event():
  return render_template('event.html', active="event")

@app.route("/accommodation")
def accommodation():
  return render_template('accommodation.html', active="accomodation")

@app.route("/gallery")
def gallery():
  return render_template('gallery.html', active="gallery")

@app.route("/stories")
def stories():
  return render_template('stories.html', active="stories")

@app.route("/registry")
def registry():
	return render_template('registry.html', active="registry")

# Validate all POST requests by checking if the csrf_token in the
# POST matches our session token. This requires a hidden field to
# be added to each FORM with value csrf_token, e.g.:
# <input name=_csrf_token type=hidden value="{{ csrf_token() }}">
@app.before_request
def csrf_protect():
  if request.method == "POST":
    token = session.pop('_csrf_token', None)
    if not token or token != request.form.get('_csrf_token'):
      abort(400)

def generate_csrf_token():
  if '_csrf_token' not in session:
    session['_csrf_token'] = binascii.hexlify(os.urandom(32))
  return session['_csrf_token']

app.jinja_env.globals['csrf_token'] = generate_csrf_token

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
