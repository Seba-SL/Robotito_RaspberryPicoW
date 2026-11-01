
from machine import Pin, I2C, PWM
import time
import os
import motores
import comunicacionWiFi
import Interfaz_grafica

from ssd1306 import SSD1306_I2C

# ============================================================
# CONFIGURACION
# ============================================================

SSID = "Robot-PicoW"
PASSWORD = "12345678"

# ============================================================
# INICIAR WIFI
# ============================================================

comunicacionWiFi.iniciar_red(SSID, PASSWORD)
# ============================================================
# INICIAR OLED
# ============================================================

i2c = I2C(0,scl=Pin(1),sda=Pin(0),freq=400000)

print("Dispositivos I2C:", i2c.scan())

display = SSD1306_I2C(128, 64, i2c, addr=0x3C)


ultima_expresion = None


# ============================================================
# INICIAR ROBOT
# ============================================================

motores.parar()

led = Pin("LED", Pin.OUT)
led.on()


# ============================================================
# BUCLE PRINCIPAL
# ============================================================

while True:

    # Atender solicitudes del celular
    comunicacionWiFi.actualizar()

    modo = comunicacionWiFi.obtener_modo_ojos()

    Interfaz_grafica.elegir_modo(display, modo ,ultima_expresion)
   # Indicador de funcionamiento
    led.toggle()

    time.sleep_ms(1)

