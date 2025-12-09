import mysql.connector
from backend.conectar import connect_db

def insert_pedido_cliente(dados):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO pedido_cliente (data_pedido,valor_total,cliente_idcliente) VALUES (%s,%s,%s)"
            values = (dados['data_pedido'], dados['valor_total'], dados['cliente_idcliente'])
            cursor.execute (sql, values)
            conn.commit()
            return {'status':'sucesso', 'mensagem': 'pedido_cliente criado com sucesso.'}
        except mysql.connector.Error as err:
            return {'status':'erro', 'mensagem': F"Erro ao criar pedido_cliente: {err}"}
        finally:
            cursor.close()
            conn.close()

def read_pedido_cliente():
    conn = connect_db
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pedido_cliente")
            resultados = cursor.fetchall()
            return{'status':'sucesso', 'dados': resultados}
        except mysql.connector.Error as err:
            return{'status':'erro', 'mensagem': f"Erro ao listar pedido_cliente:{err}"}
        finally:
            cursor.close()
            conn.close()


def update_pedido_cliente(dados):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "UPDATE pedido_cliente SET nome VALUES = %s WHERE idpedido_cliente= %s"
            values = (dados['nome'],dados['idpedido_cliente'])
            cursor.execute (sql, values)
            conn.commit()
            return {'status':'sucesso', 'mensagem': f"pedido_cliente {dados['idpedido_cliente']} atualizado com sucesso."}
        except mysql.connector.Error as err:
            return {'status':'erro', 'mensagem': F"Erro ao utilizar pedido_cliente: {err}"}
        finally:
            cursor.close()
            conn.close()

def delete_pedido_cliente(idpedido_cliente):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "DELETE FROM pedido_cliente WHERE idpedido_cliente = %s"
            cursor.execute (sql, (idpedido_cliente,))
            conn.commit()
            return {'status': 'sucesso', 'mensagem': f"pedido_cliente {"idpedido_cliente"} excluido com sucesso"}
        except mysql.connector.Error as err:
            return{'status': 'erro', 'mensagem': f"Erro ao excluir pedido_cliente: {err}"}
        finally:
            cursor.close()
            conn.close()