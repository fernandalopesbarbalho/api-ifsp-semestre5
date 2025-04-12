from flask import Flask, Blueprint
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from app.main.pessoa.pessoa_controller import api as pessoa_ns
from app.main.prontuario.prontuario_controller import api as prontuario_ns

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
blueprint = Blueprint('api', __name__)
app.register_blueprint(blueprint)

api = Api(app, title='Api Flask Expieriments', version='1.0', description='Api de experimentos com python flask', prefix='/api')

api.add_namespace(pessoa_ns, path='/pessoa')
api.add_namespace(prontuario_ns, path='/prontuario')