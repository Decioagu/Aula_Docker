import sqlite3

# Caminho do banco dentro do container (volume)
db_path = "/app/data/meubanco.db"

# Cria/abre o banco SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Cria tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    email TEXT
    )
""")

# Insere um registro
cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", ("Decio", "decio@email.com"))

# Salva alterações
conn.commit()

# Lê todos os registros
cursor.execute("SELECT * FROM clientes")
clientes = cursor.fetchall()

print("Clientes no banco:")
for cliente in clientes:
    print(cliente)

# Fecha conexão
conn.close()
