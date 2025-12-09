from app import estoque
def validar_produto(nome):
    if len(nome) <= 0:
        return {"valida": False, "mensagem": "O nome precisa ter pelo menos 1 caractere."}
    tem_numero = False
    for caractere in ["quantidade"]:
        if caractere.isdigit():
            tem_numero = True
            break
    if not tem_numero:
        return {"valida": False, "mensagem": "A quantidade deve ser apenas numeros/dígitos."}

# Entrada


def validar_entrada(estoque):
    if len(estoque["nome"]) < 3:
        return {"valida": False, "mensagem": "O nome deve ter no mínimo 3 letras."}


# Saída


def validar_saida(produto):
    if produto not in estoque:
        return {"valida": False, "mensagem": "O produto deve estar no estoque!"}
    if len(estoque["quantidade"]) > produto:
        return {"valida": True, "mensagem": "Quantidade em estoque disponível!"}