# codigo en https://www.youtube.com/watch?v=DJQgQIg_Pd0

import machine
import utime

# los pines van del GP0, GP1, ... GP28
led = machine.Pin(2, machine.Pin.OUT)

# Crear un bucle por siempre
while 1:
    led.value(1)
    utime.sleep(2)
    led.value(0)
    # el tiempo que va demorar el apagado
    utime.sleep(2)
    