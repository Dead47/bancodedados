import sqlite3

nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
email = input("Qual seu email? ") 

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text,idade integer, email text)")

cursor.execute("INSERT INTO pessoas VALUES('"+nome+"',"+str(idade)+", '"+email+"')")

banco.commit() 

cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall)
print("Dados salvos com sucesso!") 