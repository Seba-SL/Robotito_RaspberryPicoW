
from machine import Pin, I2C,SoftI2C, PWM
import time
from utime import sleep
import struct

AUDIO_PIN = 15

pwm = PWM(Pin(AUDIO_PIN))


def reproducir_wav(nombre):

    with open(nombre, "rb") as f:

        # Cabecera WAV
        riff = f.read(4)

        if riff != b"RIFF":
            print("No es un archivo WAV")
            return

        f.read(4)              # tamaño
        wave = f.read(4)

        if wave != b"WAVE":
            print("Formato incorrecto")
            return

        # Buscar chunk "fmt "
        while True:
            chunk = f.read(4)
            size = struct.unpack("<I", f.read(4))[0]

            if chunk == b"fmt ":
                fmt = f.read(size)
                break

            f.seek(size, 1)

        audio_format, canales, frecuencia, byte_rate, block_align, bits = \
            struct.unpack("<HHIIHH", fmt[:16])

        print("Formato:", audio_format)
        print("Canales:", canales)
        print("Frecuencia:", frecuencia)
        print("Bits:", bits)

        if audio_format != 1:
            print("El WAV no es PCM")
            return

        if canales != 1:
            print("El WAV debe ser MONO")
            return

        if bits != 8:
            print("El WAV debe ser de 8 bits")
            return

        # Buscar datos
        while True:
            chunk = f.read(4)
            size = struct.unpack("<I", f.read(4))[0]

            if chunk == b"data":
                break

            f.seek(size, 1)

        print("Reproduciendo...")

        # Configurar PWM
        pwm.freq(frecuencia)

        # Reproducir muestras
        datos = f.read(256)

        while datos:

            for muestra in datos:

                # WAV 8-bit unsigned:
                # 0 -> 0%
                # 128 -> 50%
                # 255 -> 100%

                pwm.duty_u16(muestra * 257)

                # Esperar aproximadamente 1/frecuencia
                time.sleep_us(int(1000000 / frecuencia))

            datos = f.read(256)

        pwm.duty_u16(0)

        print("Fin del sonido")