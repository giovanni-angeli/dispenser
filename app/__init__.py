from flask import Flask
    
app = Flask(__name__, instance_relative_config=True)

try:
    from flask_debugtoolbar import DebugToolbarExtension
    toolbar = DebugToolbarExtension(app)
except:
    print("cannot import and use DebugToolbarExtension")

# Load the default configuration
app.config.from_object('config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

from app import views


