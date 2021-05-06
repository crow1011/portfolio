from flask import Flask, Blueprint
from flask_restplus import Api


from resources.pwdgen import (
        pwdgen_ns, GenPassword, pwdgen_list_ns, GenListPassword
        )


app = Flask(__name__)
bluePrint = Blueprint('api', __name__, url_prefix='/api')
api = Api(bluePrint, doc='/doc', title='Sample Flask-RestPlus Application')

app.register_blueprint(bluePrint)

api.add_namespace(pwdgen_ns)
api.add_namespace(pwdgen_list_ns)


pwdgen_ns.add_resource(GenPassword, "")
pwdgen_list_ns.add_resource(GenListPassword, "<int:pwd_count>")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
