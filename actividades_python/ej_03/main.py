import RPi.GPIO as GPIO  #importo desde la libreria pri.gpio la funcion gpio

# Defino los pines GPIO para los LEDs y el Buzzer
PIN_ROJO = 19
PIN_AZUL = 26
PIN_VERDE = 13
PIN_BUZZER = 22

# Configurar modo de numeración de pines GPIO
GPIO.setmode(GPIO.BCM)

# Configurar pines como salida
GPIO.setup(PIN_ROJO, GPIO.OUT)
GPIO.setup(PIN_AZUL, GPIO.OUT)
GPIO.setup(PIN_VERDE, GPIO.OUT)
GPIO.setup(PIN_BUZZER, GPIO.OUT)

# Función para cambiar el estado de un LED (encender/apagar)
def toggle_led(led_pin):
    current_state = GPIO.input(led_pin)
    GPIO.output(led_pin, not current_state)

# Función para encender el buzzer
def buzz_on():
    GPIO.output(PIN_BUZZER, GPIO.HIGH)

# Función para apagar el buzzer
def buzz_off():
    GPIO.output(PIN_BUZZER, GPIO.LOW)

try:
    # Bucle principal
    while True:
        # Esperar a que el usuario ingrese un comando
        command = input("prompt: ")
        command_parts = command.split()

        # Verificar que el comando tenga dos partes (comando y opción)
        if len(command_parts) == 2:
            action = command_parts[0]
            option = command_parts[1]

            # Verificar si el comando es para el buzzer
            if action == "buzz":
                if option == "on":
                    buzz_on()
                elif option == "off":
                    buzz_off()
                else:
                    print("Opción no válida para el comando 'buzz'")
            # Verificar si el comando es para los LEDs RGB
            elif action == "rgb":
                if option == "red":
                    toggle_led(PIN_ROJO)
                elif option == "blue":
                    toggle_led(PIN_AZUL)
                elif option == "green":
                    toggle_led(PIN_VERDE)
                else:
                    print("Opción no válida para el comando 'rgb'")
            else:
                print("Comando no reconocido")
        else:
            print("Formato de comando incorrecto")

except KeyboardInterrupt:
    # Limpiar pines GPIO antes de salir
 GPIO.cleanup()
