
from gpiozero import PWMLED
import ADS1x15
import time
import math

# Pin I2C y registro del ADS1115
ADS = ADS1x15.ADS1115(1, 0x48)
# Modo de lectura única
ADS.setMode(ADS.MODE_SINGLE)
# Ganancia del ADC +-6,144V
ADS.setGain(ADS.PGA_4_096V)
# Factor de conversión a voltaje
factor = ADS.toVoltage()

# Pines PWM para LEDs azul y rojo
LEDAzul = PWMLED(26)
LEDRojo = PWMLED(19)

# Variables para temperatura
vcc = 3.3  # Voltaje de referencia
r = 10000  # Resistencia fija
beta = 3900  # Constante beta
t0 = 298.15  # Temp. de referencia en Kelvin
t = 0  # Temp. en °C
rt = 0  # Resistencia del termistor

while True:
    # Lectura analógica del potenciómetro y termistor
    LecturaPote = ADS.readADC(3)
    LecturaTerm = ADS.readADC(1)

    # Conversión de lecturas a voltaje
    LecturaPoteVoltaje = LecturaPote * factor
    LecturaTermVoltaje = LecturaTerm * factor

    # Cálculo de la resistencia del termistor
    rt = (r * LecturaTermVoltaje) / (vcc - LecturaTermVoltaje)

    # Conversión a temperatura usando Steinhart-Hart
    t = beta / (math.log(rt / r) + (beta / t0))
    t = t - 273.15  # Conversión a °C

    # Escalado del voltaje del potenciómetro a 0-30°C
    TempPote = (LecturaPoteVoltaje / 3.3) * 30

    # Diferencia entre temperatura deseada y medida
    diff = abs(TempPote - t)

    # Limitar diferencia a 5°C máx.
    if diff > 5:
        diff = 5

    # Control de LEDs según diferencia de temperatura
    if TempPote > t:
        LEDRojo.value = diff / 5  # Ajusta brillo LED rojo
        LEDAzul.value = 0         # Apaga LED azul
    elif TempPote < t:
        LEDAzul.value = diff / 5  # Ajusta brillo LED azul
        LEDRojo.value = 0         # Apaga LED rojo
    else:
        LEDAzul.value = 0         # Apaga ambos LEDs
        LEDRojo.value = 0

    # Muestra los valores en consola
    print("Termistor: {0:.3f} V, {1:.3f} °C".format(LecturaTermVoltaje, t))
    print("Potenciómetro: {0:.2f} °C".format(TempPote))

    time.sleep(1)  # Espera antes de la siguiente interación
