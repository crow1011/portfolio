from flask import Flask
from app.controllers import mod_tst

app = Flask(__name__)
app.register_blueprint(mod_tst)
