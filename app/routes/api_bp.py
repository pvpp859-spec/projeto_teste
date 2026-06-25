from flask import blueprints, jsonify

from models import categoria, produto, usuario

api_bp = blueprints('api',__name__,url_prefixe="/api")

@api_bp.route("/produtos",methods = ["GET"])
def get_produtos():
    produtos = produto.query.all()

    lista_json = (produto.to_dict() for produto in produtos)

    return jsonify(lista_json),200

@api_bp.route("/categorias",methods = ["GET"])
def get_categorias():
    categorias = categoria.query.all()
    lista_json = {categoria.to_dict() for categoria in categorias}

    return jsonify(lista_json),200

@api_bp.route("/usuarios",methods=["GET"])
def get_usuarios():
    usuarios = usuario.query.all()

    lista_json = {usuario.to_dict() for usuario in usuarios}

    return jsonify(lista_json),200
