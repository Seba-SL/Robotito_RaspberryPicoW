from machine import Pin, I2C,SoftI2C
from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
import ojos_robot
import time
import random


# Estado interno de la animación
_estado_ojos = "centro"
_tiempo_ojos = time.ticks_ms()
_proxima_accion = random.randint(1000, 3000)
accion = 0


def ojos(display):
     # Mirada al centro
    ojos_robot.dibujar_ojos(0,display)
    time.sleep_ms(1200)  



def ojos_espera(display):
    global _estado_ojos, _tiempo_ojos, _proxima_accion

    ahora = time.ticks_ms()

    # Si todavía no pasó el intervalo, no hacer nada
    if time.ticks_diff(ahora, _tiempo_ojos) < _proxima_accion:
        return

    # Si está mirando al centro, elegir una acción
    if _estado_ojos == "centro":
        accion = random.randint(0, 2)

        if accion == 0:
            ojos_robot.parpadear(display)
            _estado_ojos = "parpadeo"

        elif accion == 1:
            ojos_robot.dibujar_ojos(-4, display)
            _estado_ojos = "izquierda"

        else:
            ojos_robot.dibujar_ojos(4, display)
            _estado_ojos = "derecha"

    # Después de la acción, volver al centro
    else:
        ojos_robot.dibujar_ojos(0, display)
        _estado_ojos = "centro"

    # Registrar el momento y programar el próximo intervalo
    _tiempo_ojos = time.ticks_ms()
    _proxima_accion = random.randint(1000, 3000)




def prueba_ojos(display):

    # Mirada al centro
    ojos_robot.dibujar_ojos(0,display)
    time.sleep_ms(1200)  

    # Mirar hacia la izquierda
    ojos_robot.dibujar_ojos(-4,display)
    time.sleep_ms(500)

    # Volver al centro
    ojos_robot.dibujar_ojos(0,display)
    time.sleep_ms(700)

    # Mirar hacia la derecha
    ojos_robot.dibujar_ojos(4,display)
    time.sleep_ms(500)

  

    

    # Parpadear
    ojos_robot.parpadear(display)

    # Volver al centro
    ojos_robot.dibujar_ojos(0,display)
    time.sleep_ms(700)


    # Parpadear
    ojos_robot.guiño(display)

    # Volver al centro
    ojos_robot.dibujar_ojos(0,display)
    time.sleep_ms(700)

    # Pequeña pausa
    time.sleep_ms(800)


def mensaje(display):
    display.fill(0)
    display.text("Hola!!", 40, 28)
    display.show()
    time.sleep_ms(800)



def gato(display):

    display.fill(0)

    # Ojos
    display.fill_rect(22, 25, 25, 12, 1)
    display.fill_rect(81, 25, 25, 12, 1)

    # Pupilas verticales
    display.fill_rect(32, 27, 5, 8, 0)
    display.fill_rect(91, 27, 5, 8, 0)

    # Boca de gato
    display.line(64, 43, 64, 48, 1)
    display.line(64, 48, 57, 53, 1)
    display.line(64, 48, 71, 53, 1)

    display.show()



def elegir_modo(display, modo,ultima_expresion):

    if modo == "automatico":
        ojos_espera(display)
        ultima_expresion = None

    elif modo != ultima_expresion:

        if modo == "normal":
            ojos_robot.dibujar_ojos(0, display)

        elif modo == "guino":
            ojos_robot.guiño(display)

        elif modo == "sonrisa":
            ojos_robot.sonrisa2(display)

        elif modo == "enojado":
            ojos_robot.enojado(display)

        elif modo == "corazon":
            ojos_robot.ojos_corazon(display)

        elif modo == "grande":
            ojos_robot.ojo_grande(display)

        ultima_expresion = modo