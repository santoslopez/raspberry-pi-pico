# codigo en https://www.youtube.com/watch?v=quPgphiP9xg
# se construyo el circuito en protoboard para probar el codigo

from machine import Pin
import utime



rojo = Pin(15,Pin.OUT)
amarillo = Pin(13,Pin.OUT)
verde = Pin(16,Pin.OUT)


while True:
    verde.value(1)
    utime.sleep_ms(2000)
    verde.value(0)
    amarillo.value(1)
    utime.sleep_ms(2000)
    amarillo.value(0)
    rojo.value(1)
    utime.sleep_ms(2000)
    rojo.value(0)