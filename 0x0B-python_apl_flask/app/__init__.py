from flask import Flask
from flask sqlalchamy import SQLAlchemy

app = Flask (__name__)
app.config['SQLACHEMY_DATABASE_URI'] = "sqlit://database.db"
app.config['SQLACHEMY_TARCK_MODIFICATION'] = False
app.config['SQLACHEMY_KEY_'] = "key-goes- here"
db = SQLAlchemy(app)