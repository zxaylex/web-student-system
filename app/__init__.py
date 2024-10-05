from flask import Flask 
from .config import *
from flask_mysqldb import MySQL
from flask_wtf import CSRFProtect

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        MYSQL_USERNAME=DB_NAME,
        MYSQL_PASSWORD=DB_PASS,
        MYSQL_HOST=DB_HOST,
        MYSQL_PORT=DB_PORT,
        SECRET_KEY=SECRET_KEY
    )

    mysql.init_app(app)
    CSRFProtect(app)

    return app
