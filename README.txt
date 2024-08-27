# Proyecto Bodegas - README.txt

## Descripción
Este proyecto es una aplicación web para gestionar bodegas y realizar cotizaciones. Permite a los usuarios autenticarse, seleccionar bodegas disponibles y obtener una cotización según sus necesidades.

## Requisitos
Antes de ejecutar este proyecto, asegúrate de tener instalados los siguientes componentes:

- Python 3.11.x
- PostgreSQL 12 o superior
- Pipenv o pip (para manejar dependencias)

## Instalación

1. Descargar el archivo:

2. Crear un entorno virtual e instalar dependencias:

- Con pip:
    pip install -r requirements.txt


3. Crear la base de datos en PostgreSQL:
- Accede a PostgreSQL:
  ```
  psql -U postgres
  ```
- Crear una nueva base de datos:
  ```
  CREATE DATABASE bodegas;
  ```

- Crear un nuevo usuario y asignar permisos mediante el archivo .sql en la carpeta.

4. Configurar el archivo `settings.py`:
- Edita el archivo `settings.py` para que apunte a tu base de datos PostgreSQL:
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'nombre_de_la_base_de_datos',
          'USER': 'tu_usuario',
          'PASSWORD': 'tu_contraseña',
          'HOST': 'localhost',
          'PORT': '5432',
      }
  }
  ```

5. Migrar la base de datos:
 ```
 python manage.py migrate
 ```

6. Crear un superusuario:
 ```
 python manage.py createsuperuser
 ```

## Ejecución del Proyecto

Para ejecutar el servidor de desarrollo, usa:


Luego, abre tu navegador y accede a `http://127.0.0.1:8000/`.

## Dependencias

Las dependencias del proyecto están listadas en `requirements.txt`. Aquí algunas de las principales:

- Django==5.0.7
- psycopg2==2.9.3

## Datos de Usuario

Aquí te proporciono algunos datos de usuario para que puedas acceder al sistema:

1. **Administrador**
   - **Usuario:** admin
   - **Contraseña:** admin

2. **Usuarios Regulares**
   - **Usuario:** Pedrito_Bodeguero
   - **Contraseña:** pedrillo123

   - **Usuario:** Juliana Bod
   - **Contraseña:** juliancasablancas123

## Notas Adicionales

- **Archivos Estáticos:** Asegúrate de ejecutar `python manage.py collectstatic` antes de desplegar en producción.
- **Configuración de Seguridad:** Recuerda configurar correctamente las variables de entorno en producción, como `SECRET_KEY` y `DEBUG`.

---

Este `README.txt` cubre los pasos esenciales para poner en marcha el proyecto y proporciona toda la información necesaria sobre dependencias, configuración de base de datos, y usuarios iniciales. Si tienes alguna pregunta o necesitas ayuda adicional, ¡no dudes en contactarme!
