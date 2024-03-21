from gpiozero import LED, Button #importo las librerias del led, el boton y
from signal import pause         #el comando para pausar.

led = LED(19)                    #declaro la variable del led con la libreria y el pin asignado a este en la placa
button = Button(18)              #y les asigno los pines correspondientes

button.when_pressed = led.on     #con la libreria de button importo la funcion gpiozero, asigno el comando para cuando
button.when_released = led.off   #presione el boton se prenda el led correspondiente y cuando lo suelte se apague

pause()
