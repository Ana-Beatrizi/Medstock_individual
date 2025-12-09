import mysql.connector
from conectar import connect_db
# INSERT CLIENTE
def insert_cliente(dados):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO cliente (nome, email, cpf, senha) VALUES (%s, %s, %s, %s)"
            values = (dados['nome'], dados['email'], dados['cpf'], dados['senha'])
            cursor.execute(sql, values)
            conn.commit()
            return{'status': 'sucesso', 'mensagem': f'Cliente adicionado com sucesso'}

        except mysql.connector.Error as err:
            return{'status': 'erro', 'mensagem': f'erro: {err}'}
        finally:
            cursor.close()
            conn.close()

# READ CLIENTE
def read_cliente(idcliente):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM cliente WHERE idcliente = {idcliente}")
            resultados = cursor.fetchone()

            return {'status': 'sucesso', 'dados': resultados}

        except mysql.connector.Error as err:
            return{'status': 'erro', 'mensagem': f'erro: {err}'}
        finally:
            cursor.close()
            conn.close()

# UPDATE CLIENTE
def update_cliente(dados):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "UPDATE cliente set nome = %s where idcliente = %s"
            values = (dados['nome'], dados['idcliente'])
            cursor.execute(sql, values)
            conn.commit()

            return{'status': 'sucesso', 'mensage': f'Nome: {dados['nome']} atualizado com sucesso'}


        except mysql.connector.Error as err:
            return{'status': 'erro', 'mensagem': f'erro: {err}'}
        finally:
            cursor.close()
            conn.close()

# DELETE CLIENTE
def delete_cliente(idcliente):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "DELETE from cliente where idcliente = %s "
            cursor.execute(sql, (idcliente,))
            conn.commit()
            return{'status': 'sucesso', 'mensagem': 'cliente deletado com sucesso'}

        except mysql.connector.Error as err:
            return{'status': 'erro', 'mensagem': f'erro: {err}'}
        finally:
            cursor.close()
            conn.close()