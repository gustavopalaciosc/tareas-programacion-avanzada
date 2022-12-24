# Diagrama de Clase Tarea 1 

## Menús 
Para la tarea se creo la clase abtracra ```Menu```, de la cual heredan ```MenuInicio```, ```MenuEntrenador```, ```MenuEntrenamiento```, ```MenuSimulacion```, ```MenuCrearObjeto```, ```MenuUtilizarObjeto``` y ```MenuEstadoEntrenador```.

## Programones
Se creo la clase abstracta ```Programon```, de la cual heredan las clases ```Agua```, ```Fuego``` y ```Planta```.

## Objetos
Se creo la clase abstracta ```Objeto```, de la cual heredan ```Baya``` y ```Pocion```. A partir de las dos útlimas clases, hereda la clase ```Caramelo```

## Entrenador
Para modelar la entidad Entrenador, se creo la clase ```Entrenador```.

## Liga Programon
Para modelar la entidad Liga Programon, se creo la clase ```LigaProgramon```.

## Relaciones generales entre las distintas clases
Dentro de la clase ```MenuInicio``` se instancia la clase ```MenuEntrenador```, la cual a su vez recibe instancias de ```MenuEntrenamiento```, ```MenuSimulacion```, ```MenuCrearObjeto```, ```MenuUtilizarObjeto``` y ```MenuEstadoEntrenador```. Todas estas instancias - menos la de ```MenuInicio``` - reciben una misma instancia de ```LigaProgramon```, la cual es instanciada en ```MenuInicio```. 
La instancia de ```LigaProgramon``` contiene varias instancias de la clase ```Entrenador```, la cual a su vez contiene varias instancias de las clases ```Programon``` y  ```Objeto```.

