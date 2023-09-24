import mysql.connector

# Replace with your database credentials


connection = mysql.connector.connect(host='localhost',user='root',password='1234',database='intimacoes')

cursor = connection.cursor()


cursor.execute("""
    DROP DATABASE IF EXISTS intimacoes;
CREATE DATABASE IF NOT EXISTS intimacoes;
CREATE TABLE IF NOT EXISTS intimacao (
    id VARCHAR(255),
    idOystr VARCHAR(255),
    processo VARCHAR(255),
    diario VARCHAR(255),
    autor VARCHAR(255),
    reu VARCHAR(255),
    dataPostagem VARCHAR(255),
    intimacaoAutomatica VARCHAR(255),
    dataIntimacao VARCHAR(255),
    prazoCumprimento VARCHAR(255),
    classeProcessual VARCHAR(255),
    primeiroDiaPrazo VARCHAR(255),
    ultimoDiaPrazo VARCHAR(255),
    tipo VARCHAR(255),
    meioComunicacao VARCHAR(255),
    distribuicao VARCHAR(255),
    pessoal VARCHAR(255),
    juizo VARCHAR(255),
    dataCumprimento VARCHAR(255),
    leitor VARCHAR(255),
    estatus VARCHAR(255),
    documento VARCHAR(1500),
    movimento VARCHAR(1500),
    evento VARCHAR(255),
    eventoRef VARCHAR(255),
    advogado VARCHAR(255)
);
""")

connection.commit()
