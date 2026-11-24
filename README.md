# Sistema de Inventario PYME

## Integrantes
- Antonella González
- Laura Arriagada

## Descripción General
Aplicación de consola desarrollada en Python para la gestión de inventario de una PYME, implementada bajo una arquitectura en 3 capas (`presentacion`, `negocio`, `datos`) más capa `auxiliares`, utilizando el ORM Peewee y base de datos relacional MySQL. Incluye autenticación con contraseñas encriptadas, control de acceso por roles (`ADMINISTRADOR` y `OPERADOR`), CRUD completo de entidades principales y control de movimientos de stock.

## Dependencias
- Python 3.10 o superior
- MySQL Server (WAMP / XAMPP)
- Librerías Python (`requirements.txt`):
  - `peewee==3.17.8` (ORM)
  - `PyMySQL==1.1.1` (Conector MySQL)
  - `bcrypt==4.2.1` (Encriptación de contraseñas)
  - `maskpass==0.3.7` (Ocultamiento de contraseñas en consola)
  - `prettytable==3.12.0` (Tablas formateadas en consola)
  - `python-decouple==3.8` (Variables de entorno)

## Procedimiento de Instalación
1. Clonar el repositorio e ingresar al directorio del proyecto:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd Sistema-inventario-pymes


   