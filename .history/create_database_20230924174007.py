import mysql.connector

# Replace with your database credentials


connection = mysql.connector.connect(host='localhost',user='root',password='1234')

cursor = connection.cursor()


cursor.execute("""
    LOAD XML INFILE '/var/lib/mysql/xml/file.xml'
    INTO TABLE intimacao
    ROWS IDENTIFIED BY '<intimacoes>';
""")

connection.commit()
