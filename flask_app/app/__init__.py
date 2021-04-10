from flask import Flask
from app.controllers import mod_tst, mod_gen

app = Flask(__name__)
app.register_blueprint(mod_tst)
app.register_blueprint(mod_gen)

