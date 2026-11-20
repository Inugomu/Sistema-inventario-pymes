# Sistema de Inventario PYME

Sistema de gestión e inventario en consola desarrollado en Python utilizando arquitectura en 3 capas (`presentacion`, `negocio`, `datos`) con el ORM Peewee y MySQL.

## Requisitos Previos

- Python 3.10 o superior
- Servidor MySQL (WAMP / XAMPP / MySQL Server)

## Instalación y Configuración

1. **Clonar el repositorio y entrar a la carpeta del proyecto:**
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd Sistema-inventario-pymes

2. Crear y activar el entorno virtual:
   python -m venv .venv
.venv\Scripts\activate

3. Instalar dependencias:
   pip install -r requirements.txt

4.Configurar la base de datos:
   Importar o ejecutar el script datos/sql/basededatos.sql en MySQL.
   copiar .env.example a .env y ajustar las credenciales de conexión (user, password, port).

5.Ejecutar el sistema:
   python inventario.py