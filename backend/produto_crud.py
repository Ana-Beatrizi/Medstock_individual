import mysql.connector
from conectar import connect_db

# INSERT PRODUTO
def insert_produto(dados):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO produto (nome, quantidade_estoque, preco, categoria) VALUES (%s,%s,%s,%s)"
            values = (dados['nome'], dados['quantidade_estoque'], dados['preco'], dados['categoria'])
            cursor.execute (sql, values)
            conn.commit()
            return {'status':'sucesso', 'mensagem': 'Produto criado com sucesso.'}
        except mysql.connector.Error as err:
            return {'status':'erro', 'mensagem': F"Erro ao criar Produto: {err}"}
        finally:
            cursor.close()
            conn.close()



# READ PRODUTO
def read_produto(idproduto):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM produto WHERE idproduto = {idproduto}")
            resultados = cursor.fetchone()

            return{'status':'sucesso', 'dados': resultados}
        
        except mysql.connector.Error as err:
            return{'status':'erro', 'mensagem': f"Erro ao listar clientes:{err}"}
        finally:
            cursor.close()
            conn.close()

# UPDATE PRODUTO
def update_produto(dados):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "UPDATE produto SET nome = %s, quantidade_estoque = %s, preco = %s WHERE idproduto= %s"
            values = (dados['nome'], dados['quantidade_estoque'], dados['preco'],dados['idproduto'])
            cursor.execute (sql, values)
            conn.commit()
            return {'status':'sucesso', 'mensagem': f"produto {dados['idproduto']} atualizado com sucesso."}
        except mysql.connector.Error as err:
            return {'status':'erro', 'mensagem': F"Erro ao utilizar produto: {err}"}
        finally:
            cursor.close()
            conn.close()

# DELETE PRODUTO
def delete_produto(idproduto):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            sql = "DELETE FROM produto WHERE idproduto = %s"
            cursor.execute (sql, (idproduto,))
            conn.commit()
            return {'status': 'sucesso', 'mensagem': f"produto {idproduto} excluido com sucesso"}
        except mysql.connector.Error as err:
            return{'status': 'erro', 'mensagem': f"Erro ao excluir produto: {err}"}
        finally:
            cursor.close()
            conn.close()
