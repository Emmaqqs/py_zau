import mysql.connector 
connection = mysql.connector.connect( 
    host="localhost", 
    user="root", 
    password="rootpassword"    
) 
cursor = connection.cursor() 
print("Conexión al servidor MySQL establecida.")
departamentos = [ 
("Recursos Humanos",), 
("IT",), 
("Marketing",) 
] 
cursor.executemany("INSERT INTO departamentos (nombre) VALUES (%s)", 
departamentos) 
connection.commit() 
print(f" {cursor.rowcount} departamentos insertados.")