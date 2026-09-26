from machine import Pin, PWM
import time

A1 = PWM(Pin(10))
A2 = PWM(Pin(11))

B1 = PWM(Pin(12))
B2 = PWM(Pin(13))

# Frecuencia PWM
A1.freq(1000)
A2.freq(1000)
B1.freq(1000)
B2.freq(1000)


def prueba():

    def pwm(porcentaje):
        return int(porcentaje * 65535 / 100)

    # Todo apagado
    A1.duty_u16(0)
    A2.duty_u16(0)
    B1.duty_u16(0)
    B2.duty_u16(0)


    print("motor A")

    # MOTOR A
    A1.duty_u16(pwm(60))
    A2.duty_u16(0)


    print("motor B")
    # MOTOR B
    B1.duty_u16(pwm(60))
    B2.duty_u16(0)

    time.sleep(3)

    # Parar
    A1.duty_u16(0)
    A2.duty_u16(0)
    B1.duty_u16(0)
B2.duty_u16(0)

def velocidad(porcentaje):
    return int(porcentaje * 65535 / 100)


def parar():
    A1.duty_u16(0)
    A2.duty_u16(0)
    B1.duty_u16(0)
    B2.duty_u16(0)


def adelante(vel):
    d = velocidad(vel)

    A1.duty_u16(d)
    A2.duty_u16(0)

    B1.duty_u16(d)
    B2.duty_u16(0)


def atras(vel):
    d = velocidad(vel)

    A1.duty_u16(0)
    A2.duty_u16(d)

    B1.duty_u16(0)
    B2.duty_u16(d)


def izquierda(vel=60):
    # Rueda izquierda más lenta
    A1.duty_u16(velocidad(30))
    A2.duty_u16(0)

    # Rueda derecha más rápida
    B1.duty_u16(velocidad(vel))
    B2.duty_u16(0)


def derecha(vel=60):
    # Rueda izquierda más rápida
    A1.duty_u16(velocidad(vel))
    A2.duty_u16(0)

    # Rueda derecha más lenta
    B1.duty_u16(0)
    B2.duty_u16(velocidad(30))