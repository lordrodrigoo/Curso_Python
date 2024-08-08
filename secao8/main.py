import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
TABLE_NAME = 'customers'
DB_FILE = ROOT_DIR / DB_NAME


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD - Create Read   Update Delete
# SQL -  INSERT SELECT UPDATE DELETE

# CUIDADO: fazendo delete sem where
# cursor.execute(
#     f'DELETE FROM {TABLE_NAME}'
# )

# DELETE mais cuidadoso
cursor.execute('delete from customers where id=13')

connection.commit()
cursor.close()
connection.close()

# Criando tabela
# cursor.execute(
#     """create table if not exists customers(
#        id integer primary key autoincrement,
#        name text,
#        wight real )"""
# )
# connection.commit()

# Registrando valores nas colunas da tabela
# Atenção com sql injection

# cursor.execute(
#     """insert into customers (name, wight) values
#     ('Rodrigo', 105),
#     ('Maria', 69),
#     ('João', 120)"""
# )
# connection.commit()

# cursor.close()
# connection.close()

# Usando placeholder para maior segurança


# sql = (
#     """insert into customers (name, wight) values
#     (?, ?)"""
# )

# cursor.execute(sql, ('Joana', 55))
# connection.commit()
# cursor.close()
# connection.close()

# executemany

# sql = (
#     """insert into customers (name, wight) values
#     (?, ?)"""
# )

# cursor.executemany(sql, (('jeff', 88), ('Luiz', 99), ('Osvaldo', 77)))

# sql = (
#     """insert into customers (name, wight) values
#     (:nome, :peso)"""
# )
#cursor.execute(sql, {'nome': 'Vanessa', 'peso': 56} )
# cursor.executemany(sql, (
#                         {'nome': 'Carol', 'peso': 56},
#                         {'nome': 'Pablo', 'peso': 76}, 
#                         {'nome': 'brian', 'peso': 88},
#                         {'nome': 'Vanusa', 'peso': 75},
#                         {'nome': 'kely', 'peso': 123},   
#                         ))
# connection.commit()
# cursor.close()
# connection.close()

