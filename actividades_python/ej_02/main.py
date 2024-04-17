from gpiozero import LED  #desde la libreria gpiozero importo la funcion LED
from time import sleep    #importa la funcion sleep, que se usa para pausar la ejecucion del programa durante un tiempo especifico

ledG = LED(19)   #Se crean tres instancias de la clase LED, cada una asociada a un pin GPIO específico (19, 13 y 26, respectivamente). Estos LEDs se denominan ledG, ledR y ledB, probablemente para verde, rojo y azul, respectivamente.
ledR = LED(13)
ledB = LED(26)

while True:        #inicio un bucle infinito donde se enciende el led verde (ledg), espera 0.25 segundos
     ledG.on()     #apaga el led azul(ledb), enciede el led rojo (ledr) y espera un segundo
     sleep(0.25)   #apaga el led verde(ledg), enciende el led azul(ledb), espera 0.5 segundos y apaga el led rojo (ledr) asi haciendo las combinaciones de colores solicitadas
     ledB.off()

     ledR.on()
     sleep(1)
     ledG.off()

     ledB.on()
     sleep(0.25)
     ledR.off()
