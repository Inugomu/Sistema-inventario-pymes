from decouple import config
from peewee import MySQLDatabase

def conectar ():
    database = MySQLDatabase('inventario_pyme', **{'charset': 'utf8mb4', 'host': 'localhost', 'port': 3306, 'user': 'root'})
    return database