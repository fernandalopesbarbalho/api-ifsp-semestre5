from flask_restx import Namespace, Resource, fields
from flask import request
from app.main.prontuario.prontuario_db import ProntuarioDb

api = Namespace('Prontuário', description='Manutenção de dados de prontuário')

modelo = api.model('ProntuarioModel', {
    'id': fields.Integer,
    'descricao': fields.String,
    'paciente': fields.String
})

@api.route('/')
class ProntuarioController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self):
        return ProntuarioDb.obter(), 200
    @api.expect(modelo)
    def post(self):
        return ProntuarioDb.adicionar(request.json), 201

@api.route('/<id>')
class ProntuarioIdController(Resource):
    @api.response(200, "Busca realizada com sucesso")
    def get(self, id: int):
        return ProntuarioDb.obter(int(id)), 200

    @api.response(200, "Busca realizada com sucesso")
    @api.expect(modelo)
    def put(self, id: int):
        dados = request.get_json()
        if not dados:
            return {"erro": "Corpo da requisição ausente ou inválido"}, 400
        return ProntuarioDb.alterar(int(id), dados), 200

    def delete(self, id: int):
        return ProntuarioDb.remover(int(id)), 200