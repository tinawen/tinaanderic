import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.jinja2')

@app.route("/rsvp")
def rsvp():
    return render_template('rsvp.jinja2')

@app.route("/event")
def event():
    return render_template('event.jinja2')

@app.route("/registry")
def registry():
    return render_template('registry.jinja2')

@app.route("/gallery")
def gallery():
    return render_template('gallery.jinja2')

@app.route("/stories")
def stories():
    return render_template('stories.jinja2')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
