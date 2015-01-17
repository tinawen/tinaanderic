import os
from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template('index.jinja2')

@app.route("/rsvp")
def rsvp():
    return render_template('rsvp.jinja2')

@app.route("/event")
def event():
    return render_template('event.jinja2')

@app.route("/accommodation")
def accommodation():
    return render_template('accommodation.jinja2')

@app.route("/gallery")
def gallery():
    return render_template('gallery.jinja2')

@app.route("/stories")
def stories():
    return render_template('stories.jinja2')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
