from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)

#considers your OS and finds the base path so it can work across machines
# basedir = os.path.abspath(os.path.dirname(__file__))

# Begin the Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://venuskario1:u21neq92gei@music-store.cib0pjw76th1.us-east-2.rds.amazonaws.com:5432/music_store_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#Initialize the Database
db = SQLAlchemy(app)

#Init Marshmallow
ma = Marshmallow(app)

from routes import *

# db = SQLAlchemy(app)
if __name__ == '__main__':
    app.run(debug=True)




