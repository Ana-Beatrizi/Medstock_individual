import requests
import urllib.parse
# validar nome
def validar_nome(nome):
    if len(nome) < 3:
        return {"valida": False, "mensagem": "O nome deve ter pelo menos 3 letras!"}
    

    possui_numero = True
    for caractere in nome:
        if caractere.isdigit():
            possui_numero = False
            break
    if not possui_numero:
        return {"valida": False, "mensagem": "O nome não deve possuir números!"}
    

    contem_espaco = False
    for caractere in nome:
        if caractere.isspace():
            contem_espaco = True
            break
    if not contem_espaco:
        return {"valida": False, "mensagem": "O nome deve conter pelo menos um espaço"}

    return nome

#validar senha

def validar_senha(senha):
    #regra 1: tamanho mínimo 
    if len(senha) < 8:
        return {"valida": False, "mensagem": "A senha deve ter pelo menos 8 caracteres"}
    
    #regra 2: precisa ter número 
    tem_numero = False 
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
            break
    if not tem_numero:
        return {"valida": False, "mensagem": "A senha deve ter pelo menos um numero/dígito."}
    
    # Regra 3: precisa ter letra maiuscula 
    tem_maiuscula = False 
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
            break
    if not tem_maiuscula:
        return {"valida": False, "mensagem": "A senha deve ter pelo menos uma letra maiúscula."}
    
    #regra 4: precisa ter letra minúscula 
    tem_minuscula = False
    for caractere in senha:
        if caractere.islower():
            tem_minuscula = True
            break
    if not tem_minuscula:
        return {"valida": False, "mensagem": "A senha deve ter pelo menos uma letra minúscula."}
    
    #se passou em todas as regras 
    return senha

#CPF

def validar_cpf(cpf):
    if len(cpf) < 11:
        return{"valida": False, "mensagem": "CPF inválido!"}
    
    possui_letra = True
    for caractere in cpf:
        if caractere.isalpha():
            possui_letra = False
            break
        if not possui_letra:
            return{"valida": False, "Mensagem": "Não deve possuir Letra!"}
        
    possui_espaco = True
    for caractere in cpf:
        if caractere.isspace():
            possui_espaco = False
        if not possui_espaco:
            return{"valida": False, "Mensagem": "Não deve possuir espaço!"}
        
        return cpf
    
# =======================================================================
#========== VALIDAÇÃO EXTERNA CPF
def valida_cpf(cpf, token):
    url = "https://api.invertexto.com/v1/validator"

    params = {
        "token": token,
        "value": cpf 
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status() 

    
        data = response.json()
        return data
    
    except requests.exceptions.HTTPError as errh:
        print("Erro HTTP:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Erro de conexão:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout:", errt)
    except requests.exceptions.RequestException as err:
        print("Erro:", err)

    return None

def valida_externa_cpf(cpf):
    token2 = "22601|DhtAI0atZD6XdPErFqF1sG0c5jQ2y9Vy"
    resultado = valida_cpf(cpf, token2)
    if resultado:
        return resultado
    return {"valida": False, "mensagem": "Erro ao validar CPF externamente!"}

# ===============================================================
# ============ VALIDAÇÃO EXTERNA EMAIL
def validar_email(email, token):
    base_url = "https://api.invertexto.com/v1/email-validator"

    #codifica o email
    email_encoded = urllib.parse.quote(email)

    # monta url com email na rota
    url = f"{base_url}/{email_encoded}"

    params = {"token": token}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        return data
    
    except requests.exceptions.HTTPError as errh:
        print("Erro HTTP:", errh)
    except requests.exceptions.ConnectionError as errc:
        print('Erro de conexão:', errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout:", errt)
    except requests.exceptions.RequestException as err:
        print("Erro:", err)
    return None


def valida_externa_email(email):
    token1 = "22558|TvTq03AbZrLvC2Db5SLfeCW67P49qnQ3"
    resultado = validar_email(email, token1)
    if resultado:
        return(resultado)
    else:
        return {"valida": False, "mensagem": "Erro ao validar email externamente!"}
