# El siguente codigo 
# codigo disponible de https://www.youtube.com/watch?v=2NhHYtTNGv8

from machine import *
# microsegunso
from utime import *

# programa para hacer que uno de los leds de raspberry pi pico parpadee
# 25, porque allí viene soldado, solo alli esta en el pin 25
miLed = Pin(25,Pin.OUT)

# para hacer que parpade, hacer un bucle
noSalirse = True
while noSalirse:
    miLed.on()
    # esperamos un tiempo, esta en la biblioteca utime
    sleep(1.0)
    miLed.off()
    sleep(5)
    
    

