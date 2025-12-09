import mysql.connector
from backend.conectar import connect_db

def insert_pedido_fornecedor(dados):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO pedido_fornecedor (valor_total,data_pedido,fornecedor_idfornecedor) VALUES (%s,%s,%s)"
            values = (dados['valor_total'], dados['data_pedido'], dados['fornecedor_idfornecedor'])
            cursor.execute (sql, values)
            conn.commit()
            return {'status':'sucesso', 'mensagem': 'pedido_fornecedor criado com sucesso.'}
        except mysql.connector.Error as err:
            return {'status':'erro', 'mensagem': F"Erro ao criar pedido_fornecedor: {err}"}
        finally:
            cursor.close()
            conn.close()

def read_pedido_fornecedor():
    conn = connect_db
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pedido_fornecedor")
            resultados = cursor.fetchall()
            return{'status':'sucesso', 'dados': resultados}
        except mysql.connector.Error as err:
            return{'status':'erro', 'mensagem': f"Erro ao listar pedido_fornecedor:{err}"}
        finally:
            cursor.close()
            conn.close()


def update_pedido_fornecedor(dados):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "UPDATE pedido_fornecedor SET nome VALUES = %s WHERE fornecedor_idfornecedor= %s"
            values = (dados['nome'],dados['fornecedor_idfornecedor'])
            cursor.execute (sql, values)
            conn.commit()
            return {'status':'sucesso', 'mensagem': f"pedido_fornecedor {dados['fornecedor_idfornecedor']} atualizado com sucesso."}
        except mysql.connector.Error as err:
            return {'status':'erro', 'mensagem': F"Erro ao utilizar pedido_fornecedor: {err}"}
        finally:
            cursor.close()
            conn.close()

def delete_pedido_cliente(idpedido_fornecedor):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "DELETE FROM pedido_cliente WHERE idpedido_fornecedor = %s"
            cursor.execute (sql, (idpedido_fornecedor,))
            conn.commit()
            return {'status': 'sucesso', 'mensagem': f"pedido_fornecedor {"idpedido_fornecedor"} excluido com sucesso"}
        except mysql.connector.Error as err:
            return{'status': 'erro', 'mensagem': f"Erro ao excluir pedido_fornecedor: {err}"}
        finally:
            cursor.close()
            conn.close()