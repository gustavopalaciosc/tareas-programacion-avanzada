# Tarea 1: DCCampeonato Programón :school_satchel:

## Consideraciones generales :octocat:

El programa hace todo lo que se pide en el enunciado. Para correr el programa se deben agregar todos los archivos en una misma carpeta y ejecutar el archivo ```main.py```. Al iniciar el programa, se da la opción de elegir un entrenador de programones. Al elegir uno, se pasa al menú del entrenador donde se muestran las distintas opciones que tiene el jugador para hacer. Al llevar a cabo una simulación de ronda, en caso de perder se vuelve al menú de inicio y se da nuevamente la opción de elegir un entrenador. En caso de pasar la ronda, se vuelve al menú de entrenador y el entrenador elegido recupera la totalidad de la energía. Para ganar el campeonato se deben ganar las cuatro rondas. En caso de ganar el campeonato, se notifica esto en consola y se vuelve al menú de inicio, para empezar una nueva partida o salir del juego.

En cuanto al Diagrama de clase, este se encuentra en la carpeta ```Diagrama```, la cual contiene el diagrama propiamente tal, en formato jpg, junto con un documento que explica un poco más en detalle las relaciones entre las distintas clases de este programa.


### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Programación Orientada a Objetos (18pts) (22%%)
##### ✅ Diagrama
##### ✅ Definición de clases, atributos, métodos y properties		
##### ✅ Relaciones entre clases
#### Preparación programa: 11 pts (7%)			
##### ✅ Creación de partidas
#### Entidades: 28 pts (19%)
##### ✅ Programón
##### ✅ Entrenador		
##### ✅ Liga	
##### ✅ Objetos		
#### Interacción Usuario-Programa 57 pts (38%)
##### ✅ General	
##### ✅ Menú de Inicio
##### ✅ Menú Entrenador
##### ✅ Menu Entrenamiento
##### ✅ Simulación ronda campeonato
##### ✅ Ver estado del campeonato
##### ✅ Menú crear objeto
##### ✅ Menú utilizar objeto
##### ✅ Ver estado del entrenador
##### ✅ Robustez
#### Manejo de archivos: 12 pts (8%)
##### ✅ Archivos CSV
##### ✅ Parámetros

El bonus no fue implementado para esta tarea.

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. No es necesario agregar ninguna carpeta o archivo extra.



## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```random()``` y ```randint()```.
2. ```sys```: ```exit```.
3. ```abc```: ```ABC``` y ```abstractmethod```.
4. ```beautifultable```: ```Beautifultable()```. Esta libreria debe ser descargada para poder usarse.

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```menus```: Contiene a ```Menu(ABC)```, ```MenuInicio(Menu)```, ```MenuEntrenador(Menu)```, ```MenuEntrenamiento(Menu)```, ```MenuSimulacion(Menu)```, ```MenuCrearObjeto(Menu)```, ```MenuUtilizarObjeto(Menu)```, ```MenuEstadoEntrenador(Menu)```, las cuales modelan los distintos menus que se van mostrando en consola.
2. ```ligaprogramon```: Contiene a ```LigaProgramon```, la cual modela la liga programon.
3. ```objetos```: Contiene a ```Objeto(ABC)```, ```Baya(Objeto)```, ```Pocion(Objeto)``` y ```Caramelo(Objeto)```, las cuales modelan los distintos objetos.
4. ```programon```: Contiene a ```Programon(ABC)```, ```Planta(Programon)```, ```Agua(Programon)``` y ```Fuego(Programon)```, las cuales modelan a los distintos tipos de programones.
5. ```funciones```: Contiene distintas funciones para llevar a cabo funcionalidades del juego y lecturas de archivos .csv. Estas son ```dict_entrenadores()``` la cual retorna un diccionario con los nombres de los entrenadores, ```print_entrenadores()``` la cual imprime las distintas opciones de entrenadores al principio de la partida, ```len_csv_file()``` la cual retorna el numero de filas que tiene un archivo csv, ```print_objetos()```, la cual imprime los objetos de un entrenador en un formato especial, para ser mostrados en el estado del entrenador, y por útlimo esta la función ```beneficio_victoria()```, la cual aplica el beneficio que obtienen los programones al ganar una ronda, según el tipo que sea dicho programon.
6. ```parametros```: Contiene todos los parametros pedidos en el enunciado para la implementacion del programa.
7. ```lista_entrenadores```: contiene la función```lista_entrenadores()``` la cual retorna una lista con instancias de todos los entrenadores, utilizando los datos de ```entrenadores.csv```.
8. ```lista_objetos```: Contiene a ```lista_objetos()```, ```lista_bayas()```, ```lista_pociones()``` y ```lista_caramelos()```. Estas funciones retornan listas con las instancias de todo los objetos, los objetos tipo bayas, los objetos tipo pociones y los objetos tipo caramelos, respectivamente.
9. ```lista_programones```: Contiene a ```lista_programones```. Esta funcion retorna una lista que contiene las instancias de todos los programones contenidos en el archivo csv ```programones.csv```

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Al volver al menu de inicio (desde el menú de entrenador), la partida actual se borra y se dan nuevamente las opciones de entrenadores para empezar un nuevo dccampeonato.

PD: se espera usar el cambio de una linea para la linea 317 del archivo ```menus.py```, pues esta presenta 109 caracteres. Lo mismo para las lineas del archivo ```lista_programones```, que en tres ocaciones excede el máximo de caracteres.