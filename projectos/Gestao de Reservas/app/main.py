from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from datetime import datetime

# Definindo a estrutura de dados para uma reserva
class Reserva(BaseModel):
    nome_cliente: str
    email_cliente: str
    telefone_cliente: str
    tipo_quarto: str
    numero_quarto: str
    check_in: int
    check_out: int
    status: str

app = FastAPI()

# Função para conectar ao banco de dados
def conectar_bd():
    conn = sqlite3.connect('hotel.db')
    return conn

# Verifica se a tabela de reservas existe, se não existir, cria a tabela
def verificar_tabela_reservas():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_cliente TEXT,
            email_cliente TEXT,
            telefone_cliente TEXT,
            tipo_quarto TEXT,
            numero_quarto TEXT,
            check_in INTEGER,
            check_out INTEGER,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Verifica se o banco de dados existe, se não existir, cria o banco e a tabela
verificar_tabela_reservas()

# Endpoint para criar uma nova reserva
@app.post("/reservas/")
async def criar_reserva(reserva: Reserva):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO reservas (nome_cliente, email_cliente, telefone_cliente, tipo_quarto, 
        numero_quarto, check_in, check_out, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (reserva.nome_cliente, reserva.email_cliente, reserva.telefone_cliente,
          reserva.tipo_quarto, reserva.numero_quarto, reserva.check_in,
          reserva.check_out, reserva.status))
    conn.commit()
    conn.close()
    return {"mensagem": "Reserva criada com sucesso"}

# Endpoint para obter todas as reservas
@app.get("/reservas/")
async def obter_reservas():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reservas')
    reservas = cursor.fetchall()
    conn.close()
    return {"reservas": reservas}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
