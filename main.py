from machine import Pin, I2C,SoftI2C, PWM
from utime import sleep
import time
import struct
#import motores
import sonido
import comunicacionWiFi
import interfaz_grafica

from ssd1306 import SSD1306_I2C
import os
print(os.listdir())

AUDIO_PIN = 15

pwm = PWM(Pin(AUDIO_PIN))


SSID = "Robot-PicoW"
PASSWORD = "12345678"
scl = Pin(1)
sda = Pin(0)

comunicacionWiFi.iniciar_red(SSID,PASSWORD)

#Iniciar display oled
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=1000000)
print(i2c.scan())
display = SSD1306_I2C(128, 64, i2c, addr=0x3C)

#print(dir(ojos_robot))#Para ver si se actualizo la libreria de los ojos.
#print(dir(motores))#idem
print(dir(interfaz_grafica))

pin = Pin("LED", Pin.OUT)

print("LED comienza...")


# ============================================================
# Iteración
# ============================================================

while True:
    
    print("Nueva version 6")
    interfaz_grafica.prueba_ojos(display)


    sonido.reproducir_wav("maullido-gato.wav")

    flag_com = comunicacionWiFi.actualizar()
    contador   = flag_com

    
    if contador == 3:
        print(" ¡ Alguien se conectó !!!")
       # interfaz_grafica.mensaje(display)
        contador =  flag_com + 1
    
    time.sleep_ms(100)
