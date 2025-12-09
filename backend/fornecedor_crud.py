import mysql.connector
from conectar import connect_db
# INSERT Fornecedor
def insert_fornecedor(dados):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO fornecedor (nome_fornecedor, cnpj, email, senha) VALUES (%s, %s, %s, %s)"
            values = (dados['nome_fornecedor'], dados['cnpj'], dados['email'], dados['senha'])
            cursor.execute(sql, values)
            conn.commit()
            return{'status': 'sucesso', 'mensagem': f'Fornecedor adicionado com sucesso'}
        except mysql.connector.Error as err:
            return{'status': 'erro', 'mensagem': f'erro: {err}'}
        finally:
            cursor.close()
            conn.close()
# READ Fornecedor
def read_fornecedor(idfornecedor):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(f"select * from fornecedor where idfornecedor ={idfornecedor} ")
            resultados = cursor.fetchone()
            return {'status': 'sucesso', 'dados': resultados}
        except mysql.connector.Error as err:
            return{'status': 'erro', 'mensagem': f'erro: {err}'}
        finally:
            cursor.close()
            conn.close()
# UPDATE Fornecedor
def update_fornecedor(dados):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "UPDATE fornecedor set nome_fornecedor = %s where idfornecedor = %s"
            values = (dados['nome_fornecedor'], dados['idfornecedor'])
            cursor.execute(sql, values)
            conn.commit()
            return{'status': 'sucesso', 'mensage': f':Nome {dados['nome_fornecedor']} atualizado com sucesso'}
        except mysql.connector.Error as err:
            return{'status': 'erro', 'mensagem': f'erro: {err}'}
        finally:
            cursor.close()
            conn.close()
# DELETE FORNECEDOR
def delete_fornecedor(idfornecedor):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "DELETE from fornecedor where idfornecedor = %s "
            cursor.execute(sql, (idfornecedor,))
            conn.commit()
            return{'status': 'sucesso', 'mensagem': 'Fornecedor deletado com sucesso'}
        except mysql.connector.Error as err:
            return{'status': 'erro', 'mensagem': f'erro: {err}'}
        finally:
            cursor.close()
            conn.close()