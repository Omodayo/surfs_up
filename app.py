# Import dependencies
from flask import Flask

# Create a new flask app instance.
app = Flask(__name__)

# Determine the starting point.
@app.route('/')
def hello_world():
    return 'Hello world'

