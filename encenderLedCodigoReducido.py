# codigo https://www.youtube.com/watch?v=DJQgQIg_Pd0
# Este ejemplo es para aprender como encender un led

import machine
import utime

# los pines van del GP0, GP1, ... GP28
led = machine.Pin(2, machine.Pin.OUT)

# Crear un bucle por siempre, esto solo funciona si el encendido y apagado es el mismo tiempo
while True:
    led.toggle()
    utime.sleep(2)
    