# Tarea 3: DCCard-Jitsu 🐧🥋



## Consideraciones generales :octocat:

El programa hace casi todo lo pedido. Para empezar, se pide a cada cliente un nombre de usuario. En caso de que el nombre elegido no cumpla con los requisitos, o que ya este en uso, se le notificara al usuario esto. Luego se pasa a la ventana de espera donde el primer cliente que haya ingresado esperara a un oponente. Una vez que ya esten ambos oponentes, se iniciara una cuenta regresiva, que al llegar a cero cierra la ventana de espera de los respectivos clientes, y abre la ventana de juego. En la ventana de juego se encuentra todos los elementos pedidos en el enunciado. El nombre de la derecha corresponde al nombre del cliente, y el de la izquierda corresponde al nombre del oponente. Para elegir una carta, el jugador debe hacer click sobre esta y posteriormente apretar el boton de selección. Una vez elegida la carta, esta se mostrara en pantalla. Cuando ambos jugadores hayan elegido sus respectivas cartas, se actualizarán ambas interfaces, mostrando la carta del oponente. En caso de ganar, se agrega la ficha correspondiente al color y elemento de la carta utilizada en el lado derecho de la pantalla. En caso de perder, se agregara al lado izquierdo la ficha correspondiente a la carta utilizada por el oponente. Una vez terminada la ronda, pasaran TIEMPO_REINICIO_CARTAS milisegundos hasta que nuevamente se muestren las cartas de los jugadores por la parte de atrás y puedan elegir nuevamente. En este intervalo de tiempo, los jugadores no podran elegir cartas. Una vez que alguno de los dos jugadores cumpla con los requisitos para ganar, pasaran TIEMPO_TERMINAR_PARTIDA milisegundos y se abrira la ventana final, en donde se notificara al jugador si es que perdio o gano. Desde este menú, el jugador podra volver a la ventana de inicio. 
Hay un par de cosas pedidas en el enunciado que no fueron implementadas. El programa no maneja desconexiones repentinas, además de que cuanto se entra a la ventana de espera, estoy suponiendo que el jugador no se saldra. Para ciertas cosas que no implemente, especifique supuestos para entender de que modo se debiera probar el juego para no tener ningún error inesperado. En el caso de que hayan dos clientes en la sala de espera, si ingresa un tercero se le retornara un error a dicho cliente.
Por otro lado, cuando se termina el juego, y se vuelve a la ventana de inicio, iniciar el juego por segunda vez causará un error. 



### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Networking: 26 pts (19%)
##### ✅ Protocolo	
##### ✅ Correcto uso de sockets		
##### ✅ Conexión	
##### ✅ Manejo de Clientes	
##### ❌ Desconexión Repentina: El programa no manjea desconexiones repentinas de clientes ni del servidor.
#### Arquitectura Cliente - Servidor: 31 pts (23%)			
##### ✅ Roles			
##### ✅🟠 Consistencia: Se mantiene coordinada y actualizada la información en el servidor y en los clientes. Sin embargo, para mi tarea no utilicé Locks.		
##### ✅🟠 Logs: se implementaron los logs. Sin embargo, no se notifican los siguentes eventos: cuando se desconecta un cliente, cuando un cliente intenta ingresar a una sala de espera y cuando a un jugador se le acaba el tiempo de ronda.
#### Manejo de Bytes: 27 pts (20%)
##### ✅ Codificación			
##### ✅ Decodificación			
##### ✅ Encriptación		
##### ✅ Desencriptación	
##### ✅ Integración
#### Interfaz Gráfica: 27 pts (20%)	
##### ✅🟠 Ventana inicio: se implementó todo, excepto que si entra un tercer cliente, no se le notifica que la sala esta llena o que ya empezo la partida.		
##### ✅🟠 Sala de Espera: cuando dos clientes ingresan, comienza el contador. Cuando este llega a cero, se abre al ventana de juego y se cierra la ventana de espera. Sin embargo, como no se manejan desconexiones de usuarios, si un cliente se desconecta, no se para el contados y ocurre un error.
##### ✅🟠 Ventana de juego: se implemento casi todo. No se muestra la baraja del oponente, además de que no existe un límite de tiempo para elegir una carta.							
##### ✅ Ventana final
#### Reglas de DCCard-Jitsu: 17 pts (13%)
##### ✅ Inicio del juego			
##### ✅🟠 Ronda: si hay un empate, se elige un ganador al azar. Esto no es lo pedido en el enunciado y no alcancé a cambiarlo.				
##### ✅ Termino del juego
#### Archivos: 8 pts (6%)
##### ✅🟠 Parámetros (JSON): para los paths relacionados con las cartas, estos se pusieron directamente.	
##### ✅ Cartas.py	
##### ✅ Cripto.py




## Ejecución :computer:
El módulo principal de la tarea a ejecutar es el script  ```main.py``` que se encuentra en la carpeta del servidor. Posterior a correr este archivo, se debe correr el script ```main.py``` de la carpeta cliente. Recomiendo abrir tres terminales y correr en una la del servidor y en las otras dos la de los clientes.
Además se debe agregar la siguiente carpeta adicional:
1. ```sprites``` en ```\cliente```: esta carpeta de sprites corresponde a la que se nos entregó en el Syllabus, en la carpeta de la Tarea 3.



## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```socket```: ```socket```.
2. ```json```: ```dumps```, ```loads``` y ```load```.
3. ```PyQt5```: ```QtCore.QObject```, ```QtCore.pyqtSignal```, ```uic```, ```QtWidgets.QApplication```, ```QtCore.QTimer``` y ```QtGui.QPixmap```. (debe instalarse)
4. ```threading```: ```Thread```.
5. ```os```: ```path.join```.
6. ```sys```: ```exit```.
7. ```random```: ```choice```.

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```cliente.py```: Contiene a ```Cliente```, la cual hereda de ```QObject```.
2. ```logica_cliente.py```: Contiene a ```LogicaCliente```, la cual hereda de ```QObject```.
3. ```ventana_inicio.py```: Contiene a ```VentanaInicio```.
4. ```ventana_espera.py```: Contiene a ```VentanaEspera```.
5. ```ventana_juego.py```: Contiene a ```VentanaJuego```.
6. ```ventana_final.py```: Contiene a ```VentanaFinal```.
7. ```cripto.py```: Contiene las funciones ```encriptar()``` y ```desencriptar()```.
8. ```funciones.py```: Contiene la función ```read_json()```, utilizada para leer los parametros contenidos en ```parametros.json```.
9. ```servidor.py```: Contiene a ```Servidor```.
10. ```logica_servidor.py```: Contiene a ```LogicaServidor```.
11. ```usuario.py```: Contiene a ```Usuario```.
12. ```cartas.py```: Contiene la función ```get_penguins()```.
13. ```parametros.json```: Contiene todos los parametros utilizados en el programa. Estos estan en formato json.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Solo se conectarán dos clientes a la vez. Este supuesto es para que el juego funcione bien, siendo que no se estaría cumpliendo con todo lo pedido en el enunciado.
2. Una vez que esten todos los clientes conectados, se hace el supuesto de que ninguno tendra una conexión repentina. Nuevamente hago este supuesto por las rezones planteadas en el primer supuesto.
3. Los jugadores no elegiran sus cartas a exactamente el mismo tiempo. 


PD: al terminar el juego, si uno sale con ctrl más C del servidor, se imprimiran todos los logs del juego. Cabe desctacar que para esta parte del servidor, me base mucho en la Actividad Formativa 3.




## Referencias de código externo :book:

Para realizar mi tarea saqué código de la Actividad Formativa 3:
1. \<https://github.com/IIC2233/gustavopalaciosc-iic2233-2022-2/blob/main/Actividades/AF3/servidor/utils.py>: Utilice código de la función ```data_json()``` en mi función ```read_json()```, la cual se encuentra en el módulo ```funciones.py```.



