Sitio web para la gestión de torneos de Yugioh. En el cual se almacena la información de los torneos, sus participantes, resultados de partidas, deck de los participantes y mucho más.

## Backend
- Django Rest Framework

Es una aplicación Django subdividida en 3 aplicaciones:

- Users: Contiene todo lo relacionado con los tipos de usuarios, permisos, y consultas a sus tablas.
- Ygo: Contiene todo lo relacionado con el juego Yugioh, las cartas, decks, arquetipos.
- Tournamet: Toda la parte de administrar los torneos, partida, ronda y participantes.

Por cada aplicación se han agregados consultas útiles adicionales al CRUD


### Instalación
El server de Django para desarrollo es seguir lo planteado en el archivo development.py y para producción production.py, puesto que usamos SQLite para las pruebas.
En el modo producción el deploy depende del hosting, aquí sería necesario la instalación de gunicorn y dj_database_url para este.
En modo desarrollo sería usar el tutorial de instalación de Django:

Para que se creen las migraciones
```
$ python manage.py makemigrations
```
Para que esas migraciones se ejecuten en la Bases de datos
```
$ python manage.py migrate
```

Crear una cuenta de administrador
```
$ python manage.py createsuperuser
```
Poblar la base de datos con datos por defecto.
```
$ python manage.py Shell
```
En el Shell:
```
$ from populate import run
$ run()
```
Levantar el servidor
```
$ python manage.py runserver
```
### Arquitectura Clean
El proyecto está dividido por carpetas como si fuera una arquitectura clean, lo cual no se cumple pues todas las capas son dependientes del framework Django.