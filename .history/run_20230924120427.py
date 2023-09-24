import mysql.connector

# Replace with your database credentials

config = {
    "host": "localhost",
    "user": "root",
    "password": "1234",
    "database": "intimacoes"
}


connection = mysql.connector.connect(**config)

cursor = connection.cursor()


cursor.execute("""
    LOAD XML INFILE '/var/lib/mysql/xml/file.xml'
    INTO TABLE intimacao
    ROWS IDENTIFIED BY '<intimacoes>';
""")

connection.commit()
