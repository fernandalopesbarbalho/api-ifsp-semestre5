class ProntuarioDb:
    items = [
        {
            'id': 1,
            'descricao': 'Consulta de rotina',
            'paciente': 'Maria Caetano'
        },
        {
            'id': 2,
            'descricao': 'Retorno exame',
            'paciente': 'João Senna'
        },
        {
            'id': 3,
            'descricao': 'Consulta de urgência',
            'paciente': 'Lucas Mendes'
        }
    ]

    @classmethod
    def adicionar(cls, item):
        cls.items.append(item)
        return True
    @classmethod
    def obter(cls, id=None):
        if id:
            return next(filter(lambda x: x['id'] == id, cls.items), {})
        return cls.items
    @classmethod
    def remover(cls, id):
        cls.items = list(filter(lambda x: x['id'] != id, cls.items))
        return {"mensagem": f"Prontuário id {id} deletado com sucesso"}
    @classmethod
    def alterar(cls, id, novo_item: dict):
        item = next(filter(lambda x: x['id'] == id, cls.items), {})
        index = cls.items.index(item)

        if novo_item.get('descricao'):
            item['descricao'] = novo_item.get('descricao')

        if novo_item.get('paciente'):
            item['paciente'] = novo_item.get('paciente')

        cls.items[index] = item
        return item