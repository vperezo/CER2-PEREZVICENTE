# CER2 - Catálogo Patrimonio Vivo

## Instalación y ejecución

1. Instalar las dependencias:
   ```
   python -m pip install -r requirements.txt
   ```
2. Aplicar las migraciones:
   ```
   python manage.py migrate
   ```
3. Ejecutar el servidor:
   ```
   python manage.py runserver
   ```
4. Abrir http://127.0.0.1:8000/ en el navegador.

## Datos de prueba

El proyecto incluye el archivo `db.sqlite3` con 4 categorías y 12 lugares patrimoniales ya cargados.

## Usuarios y permisos

| Usuario | Rol | Permisos |
|---|---|---|
| admin | Superusuario | Accede a `/admin/` y administra todo |
| editor1 | Grupo Editores | Ver, agregar y modificar lugares |
| lector1 | Sin grupo | Solo ve la sección de gestión, sin agregar ni modificar |

Las contraseñas no se publican en el repositorio. Para probar con credenciales propias se puede crear un administrador con: `python manage.py createsuperuser`

Los permisos se configuran en `/admin/`: en Grupos → Editores se asignan los permisos de "lugar patrimonial" (ver, agregar y modificar), y en Usuarios se asocia cada usuario a su grupo.

Las imágenes de los lugares se cargan desde URLs externas, por lo que se necesita conexión a internet para verlas.