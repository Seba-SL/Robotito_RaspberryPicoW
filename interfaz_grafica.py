from machine import Pin, I2C,SoftI2C
from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
import ojos_robot
import time




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

    ojos_robot.enojado(display)
    time.sleep_ms(700)
    # Volver al centro
    ojos_robot.dibujar_ojos(0,display)
    time.sleep_ms(700)
    
    ojos_robot.ojo_grande(display)
    
    time.sleep_ms(700)
    ojos_robot.sonrisa2(display)


    time.sleep_ms(700)
    ojos_robot.sonrisa(display)

    time.sleep_ms(700)
    ojos_robot.ojos_corazon(display)
        
    
    # Pequeña pausa
    time.sleep_ms(800)


def mensaje(display):
    display.fill(0)
    display.text("Hola!!", 40, 28)
    display.show()
    time.sleep_ms(800)