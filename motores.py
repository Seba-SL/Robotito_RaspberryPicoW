from machine import Pin, PWM
import time


# ============================================================
# CONFIGURACIÓN DE PINES
# ============================================================

A1 = PWM(Pin(10))
A2 = PWM(Pin(11))

B1 = PWM(Pin(8))
B2 = PWM(Pin(9))


# Frecuencia del PWM
FRECUENCIA = 1000  # Hz

A1.freq(FRECUENCIA)
A2.freq(FRECUENCIA)
B1.freq(FRECUENCIA)
B2.freq(FRECUENCIA)


# ============================================================
# CONTROL DE VELOCIDAD
# ============================================================

def duty(velocidad):
    """
    Convierte velocidad de 0-100 % a duty de 0-65535.
    """
    velocidad = max(0, min(100, velocidad))
    return int(velocidad * 65535 / 100)


def parar():
    A1.duty_u16(0)
    A2.duty_u16(0)
    B1.duty_u16(0)
    B2.duty_u16(0)


# ============================================================
# MOVIMIENTO
# ============================================================
def adelante(velocidad=100):
    d = duty(velocidad)
    
    A1.duty_u16(0)
    A2.duty_u16(d)
    
    B1.duty_u16(0)
    B2.duty_u16(d)
    

def atras(velocidad=100):
    d = duty(velocidad)
        
    A1.duty_u16(d)
    A2.duty_u16(0)
        
    B1.duty_u16(d)
    B2.duty_u16(0)



def izquierda(velocidad=20):

    d = duty(velocidad)

    A1.duty_u16(0)
    A2.duty_u16(0)

    B1.duty_u16(0)
    B2.duty_u16(d)



def derecha(velocidad=20):

    d = duty(velocidad)

    A1.duty_u16(0)
    A2.duty_u16(d)

    B1.duty_u16(0)
    B2.duty_u16(0)



# ============================================================
# PRUEBA DE MOTORES
# ============================================================

def prueba():

    print("=== PRUEBA DE MOTORES ===")

    print("Adelante 50 %")
    adelante(50)
    time.sleep(10)

    parar()
    time.sleep(10)

    print("atras 100 %")
    atras(100)
    time.sleep(5)

    parar()
    time.sleep(10)

    print("Adelante 100 %")
    adelante(100)
    time.sleep(5)

    parar()
    time.sleep(10)

    print("Atrás 10 %")
    atras(60)
    time.sleep(10)

    parar()

    print("=== FIN DE PRUEBA ===")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

# prueba()