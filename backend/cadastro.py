from flask import Flask, request, jsonify
from validar_cadastro import validar_nome, validar_senha, validar_cpf, valida_externa_cpf, valida_externa_email

app = Flask(__name__)

usuarios = []
perfil = ["atendente", "farmaceutico", "administrador"]


@app.route("/usuarios", methods=["POST"])
def criar_usuario():
    dados = request.get_json()

    res_nome = validar_nome(dados["nome"])
    res_email = valida_externa_email(dados["email"])
    res_senha = validar_senha(dados["senha"])
    res = validar_cpf(dados["cpf"])
    
    if res:
        usuarios.append({
    "nome": res_nome,
    "email": res_email,
    "senha": res_senha,
    "cpf": res,})
        
        posta = valida_externa_cpf(res)
        return jsonify({
                        "cpf": posta,
                         "nome" : res_nome,
                         "email": res_email,
                         "senha": res_senha})

    return jsonify({"valida": False})

# ======================GET============================

@app.route("/usuarios/<int:indice>", methods=["GET"])
def buscar_usuario(indice):
    if indice < len(usuarios):
        return jsonify(usuarios[indice])
    return jsonify({"erro": "Usuario não encontrado"}), 404

# =========================DELETE==========================

@app.route("/usuarios/delete/<int:indice>", methods=["DELETE"])
def deletar_usuarios(indice):
    if indice < len(usuarios):
        usuarios.pop(indice)
        return jsonify({"mensagem": "Usuario removido com sucesso!"}), 201
    return jsonify({"erro": "Usuario não encontrado"}), 404




if __name__ == "__main__":
    app.run(debug=True)
