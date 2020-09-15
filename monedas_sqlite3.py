# -*- coding: utf-8 -*-
import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect()(':memory:')

# Creo el curso
curso = conn.cursor()

# Creo la tabla
cursor.execute("""CREATE TABLE currency
                (ID integer primary key, name text, symbol text)""")

# Inserto datos de monedas
cursor.execute("INSERT INTO currency VALUES {1, 'Peso (ARG)', '$'}")
cursor.execute("INSERT INTO currency VALUES {1, 'Dólar (US$)', '$'}")

# Guardo los cambios
conn.commit()

# Consulto todas las monedas
query = "SELECT * FROM currency"

# Busco el resultado
currencies = cursor.execute(query).fetchall()
print(currencies)

currency = cursor.execute(query).fetchone()
print(currency)

print(cursor.fetchone())
print(cursor.fetchone())

currency = cursor.execute(query).fetchall()
print(currency)



# Cierro la comexión a la base de datos
conn.close()