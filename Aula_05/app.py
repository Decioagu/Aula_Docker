import mysql.connector

# Configurações de conexão (mesmo que você passou no docker run do MySQL)
config = {
    'user': 'decio',
    'password': 'decio123',
    'host': 'container_mysql_aula_05',  # nome do container: __NOME DO CONTAINER MYSQL__
    'database': 'banco_docker',
    'port': 3306
}

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Teste: mostrar tabelas
    cursor.execute("SHOW TABLES;")
    tabelas = cursor.fetchall()

    print(" ======================= Tabelas existentes no banco  =======================")
    for t in tabelas:
        print("-", t[0] if t else " ======================= Nenhuma tabela ======================= ")

except mysql.connector.Error as err:
    print(" ======================= Erro ao conectar no MySQL ======================= ", err)

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
