# Tarea 2: DCCruz vs Zombies :zombie::seedling::sunflower:


## Consideraciones generales :octocat:

El programa hace casi todo lo pedido en el enunciado. Para partir debe ejecutarse el script ```main.py```. A continuación aparecera la ventana de inicio, en donde se debera ingresar un nombre de usuario valida. Tras esto, se procede a elegir la cancha en la que se quiere jugar (si se elige la cancha nocturna, no se generarán soles), y posteriormente se abre al ventana de juego. Para empezar el juego se debe pulsar el boton iniciar. Una vez iniciado, se empezaran a generar los zombies de manera aleatoria y se podra empezar a plantar. Para esto, se debe hacer click derecho en la planta que se quiere plantar, y posterior a esto se debe hacer click derecho en el cuadro de pasto en el que se quiere plantar la planta. En caso de elegir un espacio que ya este ocupado, se invalida la elección. Para recolectar los soles, se debe hacer click izquierdo sobre estos. Estas funciones solo pueden hacerse si el juego esta en curso, y no esta pausado. De otro modo, no funcionara. Cuando termina la ronda, se cierra la ventana de juego y se abre la ventana post ronda con toda la información pedida en el enunciado. En esta se puede salir del juego, o pasar a la siguiente ronda, en caso de que el jugador alla ganado al ronda anterior. Al pasar de ronda, se reincia el número de soles y los zombies. 

### Cosas implementadas y no implementadas :white_check_mark: :x:

#### Ventanas: 39 pts (40%)
##### ✅ Ventana de Inicio
##### ✅ Ventana de Ranking	
##### ✅🟠 Ventana principal: la ventana principal permite elegir al usuario el escenario correctamente. En caso de seleccionar los dos escenario o ninguno, no deja continuar. Sin embargo, esto no se notifica como se pidio en el enunciado.
##### ✅🟠 Ventana de juego: la ventana contiene todo lo pedido. Sin embargo, si se intenta poner una planta en un lugar invalido u ocupado por otra planta, esto no se notifica.
##### ✅ Ventana post-ronda
#### Mecánicas de juego: 46 pts (47%)			
##### ✅ Plantas: se implemento todo lo pedido, excepto que cuando un guisante congelado golpea a un zombie, la velocidad de este no disminuye.
##### ✅🟠 Zombies: se implemento todo lo pedido, excepto que cuando un guisante congelado golpea a un zombie, la velocidad de este no disminuye.
##### ✅ Escenarios		
##### ✅🟠 Fin de ronda: se implemento todo, excepto que Crazy Cruz no notifica al usuario que gano la partida
##### ✅🟠 Fin de juego: se implemento todo, excepto que en caso de derrota no se muestra el texto "The Zombies ate your brains!"
#### Interacción con el usuario: 22 pts (23%)
##### ✅ Clicks	
##### ✅🟠 Animaciones: se implementarion los sprites de las entidades, sin embargo estas no llevan a cabo movimientos fluidos.
#### Cheatcodes: 8 pts (8%)
Para el caso de los cheatcodes, se deben apretar las teclas correspondientes al cheatcode de forma continua. Estos funcionan cualquiera sea el orden de las teclas, vale decir, puedo apretar la tecla n, la tecla s y la tecla u, y se activara el cheatcode de los soles extra. 
##### ✅ Pausa
##### ✅ S + U + N
##### ✅ K + I + L
#### Archivos: 4 pts (4%)
##### ✅🟠 Sprites: no se usaron todos los sprites, ya que no se implemento el movimiento fluido de estos.
##### ✅🟠 Parametros.py: no se utiliza el costo de avanzar para esta tarea



## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```puntajes.txt``` en ```T2```
2. ```aparicion_zombies.py``` en ```T2```: este corresponde al script entregado en la carpeta T2 del respositorio Syllabus.
3. ```sprites``` en ```frontend/assets/```: esta corresponde a la carpeta que contiene los sprites a utilizar que fueron entregados en la carpeta T2 de Syllabus.



## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```os```: ```path```
2. ```random```: ```chocie``` y ```randint```  
3. ```PyQt5```: ```QtCore.QObject```, ```QtCore.pyqtSignal```, ```uic```, ```QtWidgets.QApplication```, ```QtWidgets.QCheckBox```, ```QtCore.QTimer``` y ```QtGui.QPixmap```
4. ```sys```: ```exit```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```ventana_inicio.py```: Contiene a ```VentanaInicio```.
2. ```ventana_principal.py```: Contiene a ```VentanaPrincipal```.
3. ```ventana_juego.py```: Contiene a ```VentanaJuego```.
4. ```ventana_post_juego.py```: Contiene a ```VentanaPostJuego```.
5. ```ventana_ranking.py```: Contiene a ```VentanaRanking```.
6. ```logica_inicio.py```: Contiene a ```LogicaInicio```.
7. ```logica_juego.py```: Contiene a ```LogicaJuego```.
8. ```logica_principal.py```: Contiene a ```LogicaPrincipal```.
9. ```logica_ranking```: Contiene a ```LogicaRanking```.
10. ```guisantes.py```: Contiene a ```Guisante```.
11. ```zombies.py```: Contiene a ```Zombie```, ```ZombieClasico``` y ```ZombieRapido```.
12. ```plantas.py```: Contiene a ```PlantaAtaque```, ```Planta```, ```PlantaClasica```, ```PlantaAzul```, ```Girasol``` y ```Patata```.
13. ```soles.py```: Contiene a ```Sol```
14. ```parametros.py```: Contiene todos los parametros entregados en la carpeta Syllabus, más ```PATH_ZOMBIES```, ```PATH_PLANTAS``` y ```PATH_ELEMENTOS_JUEGO```



## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Para los cheatcodes, supuse que no importa el orden en que se opriman las teclas, mientras estas se opriman de manera consecutiva.



PD: Al usar el botón avanzar o el cheatcode kil, este funciona casi siempre, pues me di cuenta que hay veces que esta funcionalidad causa un error, lo cual hace que los sprites de los zombies no desaparezcan en la siguiente ronda. Esto me hace pensar que también podria ocurrir al pasar de ronda sin utilizar estas funciones. En caso de que ocurra, lo cual sera evidente para el jugador, recomiendo cerrar el programa y volver a abrirlo, pues posterior a uno de estos errores logre jugar 14 rondas sin problemas de este tipo. 


## Referencias de código externo :book:

Para realizar mi tarea saqué código de mi propia tarea 0:
1. \<https://github.com/IIC2233/gustavopalaciosc-iic2233-2022-2/blob/main/Tareas/T0/ranking_puntajes.py>: este hace ordena los puntajes de mas alto a más bajo. Está implementado en el archivo ```logica_ranking.py``` en la función ```calcular_ranking```
2. \<https://github.com/IIC2233/gustavopalaciosc-iic2233-2022-2/blob/main/Tareas/T0/guarda_puntajes.py>: este escribe el puntaje del usuario en el archivo ```puntajes.txt```. Está implementado en el archivo ```ventana_post_juego.py``` en la función ```guardar_puntaje```

