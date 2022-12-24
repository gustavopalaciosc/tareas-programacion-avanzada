# Tarea 0: Star Advanced :rocket: :milky_way:

## Consideraciones generales :octocat:

Para la Tarea 0 se implementaron todas las funcionalidades pedidas. Para correr el programa, se debe ejecutar el archivo ```main.py```. El juego se lleva a cabo por medio de menus. Cuando una partida es guardada, los datos de esta se guardan en la carpeta ```partidas```, y el puntaje parcial que se lleva hasta el momento se guarda en el archivo ```puntajes.txt```. Si se descubren todas las casillas sin bestias, se guarda el puntaje y se borra la partida, pues ya se habra ganado. En caso de perder, se borra la partida y el puntaje guardado, en caso de haberlo. Si se inicia una partida con un nombre de usuario que ya fue utilizado, y esta partida se guarda, los datos de la ultima se sobreescribiran, quedando guardada la partida y puntajes actuales. 


## Cosas implementadas y no implementadas :white_check_mark: :x:

#### Programación Orientada a Objetos:
##### ✅ Menú de Inicio
##### ✅ Funcionalidades		
##### ✅ Puntajes
#### Flujo del Juego:
##### ✅ Menú de Juego
##### ✅ Tablero		
##### ✅ Bestias	
##### ✅ Guardado de partida		
#### Término del Juego:
##### ✅ Fin del juego	
##### ✅ Puntajes	
#### Genera:
##### ✅ Menús
##### ✅ Parámetros
##### ✅ PEP-8

Para esta tarea, no fue implementado el Bonus.

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. En el mismo directorio en que este el archivo ```main.py``` se debe tener los siguientes archivos:
1. ```menus.py```
2. ```partida.py```
3. ```contabilizador_enemigos.py```
4. ```eliminar_partida.py```
5. ```guarda_puntajes.py```
6. ```ranking_puntajes.py```
7. ```verificador_coordenadas.py```
8. ```parametros.py```: este archivo corresponde al entregado por el equipo docente en el repositorio Syllabus. 
9. ```tablero.py```: este archivo corresponde al entregado por el equipo docente en el repositorio Syllabus.

Los archivos ```parametros.py``` y ```tablero.py``` deben ser sacados de la carpeta **T0** del repositorio **Syllabus** del curso.


Además se debe crear los siguientes archivos y directorios adicionales dentro del directorio donde este el archivo ```main.py``` y los demás archivos del programa:
1. ```partidas/```: carpeta donde se guardaran los datos de las partidas en curso en archivos del tipo **.txt**, los cuales llevaran como nombre el nombre de usuario elegido al principio de la partida. En dichos archivos, la informacion se guardara en el siguiente formato: {nombre de usuario};{largo del tablero};{ancho del tablero};{informacion del tablero descubierto};{tablero del jugador};{numero de bestias};{numero de casillas descubiertas}. Los datos del tablero estan guardados como el string "110N10110", el cual representaria un tablero del tipo [[1, 1, 0], [N, 1, 0], [1, 1, 0]].
2. ```puntajes.txt```: archivo donde se guardaran los puntajes de las partidas.


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```math```: fue usada la funcion  ```ceil``` para redondear el numero de bestias por tablero.
2. ```random```: fue usada la funcion ```shuffle``` para mezclar las posiciones de las bestias en el tablero.
3. ```os```: fueron usadas las funciones ```listdir```, para obtener los nombres de usuarios asociados a partidas guardadas en la carpeta ```partidas```, y ```remove```, para eliminar los archivos con informacion de una partida de la carpeta ```partidas```.

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```menus.py```: Contiene las clases ```MenuInicio``` y ```MenuJuego``` las cuales contienen como metodos las distintas opciones que debia contener el menú de inicio y el menú de juego, respectivamente. 
2. ```partida.py```: Contiene las clases ```Partida``` y ```PartidaEmpezada```, las cuales contienen los atributos y metodos necesarios para llevar a cabo la partida. ```PartidaEmpezada``` tiene cuatro atributos extras, los cuales son obtenidos de los archivos contenidos en la carpeta ```partidas```.
3. ```contabilizador_enemigos.py```: Contiene la función ```cont_enemigos```, la cual fue utilizada para rellenar el tablero de referencia (no el mostrado al jugador) con los contabilizadores de bestias cercanas.
4. ```eliminar_partida.py```: Contiene la función ```eliminar_partida```, la cual elimina la partida asociada al usuario especificado de la carpeta ```partidas```.
5. ```guarda_puntajes.py```: Contiene las funciones ```guarda_puntajes```, ```sobreescribir_puntaje``` y ```eliminar_puntaje```, las cuales sirven para manejar la informacion de los puntajes de los jugadores.
6. ```ranking_puntajes.py```: Contiene la función ```ranking_puntajes```, la cual fue crada para ordenar el ranking de puntajes guardados.
7. ```verificador_coordenadas.py```: Contiene la función ```verificar_cordenadas```, la cual fue usada para procesar el input del usuario cuando elige las coordenadas durante el juego, verificando que sean validas. 

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Se puede crear una partida con un nombre de usuario que ya esta usado. Si se guarda esta nueva partida, se sobreecribe la informacion de la nueva partida en la carpeta ```partidas```.
2. Cuando se guarda una partida, tambien se guarda el puntaje que se lleva asociado a dicha partida.
3. Si se descubre una bestia (y por consiguiente se pierde :pensive:), se borra la partida y el puntaje asociados al usuario, en caso de que se haya guardado la partida anteriormente.
4. Si se descubren todas las casillas sin bestias, se termina el juego, se guarda el puntaje asociado al usuario, y se borra la informacion de la partida guardada en la carpeta ```partidas```, en caso de estar guardada.
5. Durante el juego, para elegir una coordenada, el input debe estar en el siguiente formato: {letra}{numero}


PD: Para el menu de juego, se agrego la opción **Ver tablero**, la cual imprime el tablero del jugador hasta el momento. Así, si se carga una partida guardada, se puede ver en que estado esta el tablero. De todos modos, al elegir la opcion **Descubrir sector**, se imprime el tablero antes de pedirle al jugador las coordenadas de la casilla a descubrir.
