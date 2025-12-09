import mysql.connector
from backend.conectar import connect_db

def insert_movimentacao(dados):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO movimentacao (quantidade,data_mov,idorigem) VALUES (%s,%s,%s)"

            values = (dados['quantidade'], dados['data_mov'], dados['idorigem'])
            cursor.execute (sql, values)
            conn.commit()
            return {'status':'sucesso', 'mensagem': 'movimentacao criado com sucesso.'}
        except mysql.connector.Error as err:
            return {'status':'erro', 'mensagem': F"Erro ao criar movimentacao: {err}"}
        finally:
            cursor.close()
            conn.close()

def read_movimentacao():
    conn = connect_db
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM movimentacao")
            resultados = cursor.fetchall()
            return{'status':'sucesso', 'dados': resultados}
        except mysql.connector.Error as err:
            return{'status':'erro', 'mensagem': f"Erro ao listar movimentacao:{err}"}
        finally:
            cursor.close()
            conn.close()


def update_movimentacao(dados):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "UPDATE movimentacao SET nome VALUES = %s WHERE idmovimentacao= %s"
            values = (dados['nome'],dados['idmovimentacao'])
            cursor.execute (sql, values)
            conn.commit()
            return {'status':'sucesso', 'mensagem': f"movimentacao {dados['idmovimentacao']} atualizado com sucesso."}
        except mysql.connector.Error as err:
            return {'status':'erro', 'mensagem': F"Erro ao utilizar movimentacao: {err}"}
        finally:
            cursor.close()
            conn.close()

def delete_movimentacao(idmovimentacao):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "DELETE FROM movimentacao WHERE idmovimentacao = %s"
            cursor.execute (sql, (idmovimentacao,))
            conn.commit()
            return {'status': 'sucesso', 'mensagem': f"movimentacao {"idmovimentacao"} excluido com sucesso"}
        except mysql.connector.Error as err:
            return{'status': 'erro', 'mensagem': f"Erro ao excluir movimentacao: {err}"}
        finally:
            cursor.close()
            conn.close()