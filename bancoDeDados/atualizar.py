import sqlite3

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text,idade integer, email text)")

cursor.execute("UPDATE pessoas SET nome = '' WHERE idade = ")

banco.commit() 

print("Dados atualizados com sucesso!")