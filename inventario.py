from presentacion import cargar_menu

# cargar_menu()
from datos.repositorios.repo_almacen import listado_almacenes
from prettytable import PrettyTable

table_almacenes = PrettyTable()
almacenes = listado_almacenes()
for almacen in almacenes:
    print(f'{almacen.id_almacen} - {almacen.nombre_almacen} - {almacen.direccion_almacen} - {almacen.telefono_almacen}')

