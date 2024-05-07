from flask import Blueprint, jsonify, request

bp = Blueprint("api", __name__)

#Daqui para baixo as rotas

@bp.route("/api/argumentos/<string:nome>")
def argumentos(nome:str):
    return jsonify( {"status": 200, "data":nome} )

@bp.route("/api/argumentos")
def arg_implicito(nome:str):
    return jsonify( {"status": 200, "data":nome} )

@bp.route("/api/idades", methods = ("GET",))
def idades():
    from random_data import pessoas
    import funcoes
    num = funcoes.maior_de_50(pessoas)
    return jsonify( {"status": 200, "data": num} )

@bp.route("/api/salario", methods = ("GET",))
def salario():
    from random_data import pessoas
    import funcoes
    num = funcoes.mais_2000(pessoas)
    return jsonify( {"status": 200, "data": num} )

@bp.route("/api/maiores_salarios", methods = ("GET",))
def dados():
    from random_data import pessoas
    import funcoes
    num = funcoes.maior_salario(pessoas)
    return jsonify( {"status": 200, "data": num} )

@bp.route("/api/salario_media", methods = ("GET",))
def media_salarial():
    from random_data import pessoas
    import funcoes
    num = funcoes.media_profissoes(pessoas)
    return jsonify( {"status": 200, "data": num} )

@bp.route("/api/salario_idade", methods = ("GET",))
def intervalo():
    from random_data import pessoas
    import funcoes
    num = funcoes.maior_2000_sexo(pessoas)
    return jsonify( {"status": 200, "data": num} )

if __name__ == 'main':
    bp.run(debug=True)
