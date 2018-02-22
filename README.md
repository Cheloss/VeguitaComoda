# Pagina Web para el Arriendo de Globos

Esta aplicacion se realizo segun las instruciones del curso de Desarrollo de Web, de la universidad andres bello. Esta subida a Github [Trabajo Final](https://github.com/Cheloss/TrabajoFinal/)

## Problematica y Requerimientos

Juan Carlos Nuñez, hermano del Alumno Marcelo Nuñez, le solicito crear una página web con el motivo de emprender con un negocio de arriendo de Juegos Inflables en la cual se pudieran visualizar los productos que se arriendan y que le permitiera subir nuevos productos, modificarlos o eliminarlos en el futuro

## Ejecución local

El index del proyecto de ejecuta la la ruta local por ejemplo [Localhost](127.0.0.1:8080), para instalar los requemientos puede usar el siguiente comando

```
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver 0.0.0.0:8080
```

Para la creacion, edicion, eliminacion de Juegos Inflables hay que acceder mediante el usuario administrado en la siguiente ruta [Localhost/admin](http://127.0.0.1:8080/admin/). El usuario y contraseña son.
```
User: Chelo
Pass: alaloepa2042
```
Las visualizacion de los juegos se puede ver accediendo click en el menu juegos o en el siguiente enlace [Juegos](http://127.0.0.1:8080/juegos/list/)