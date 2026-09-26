import time


# ============================================================
# OJO
# ============================================================

def ojo(x, y, ancho, alto, display):

    # Centro del ojo
    display.fill_rect(
        x + 5,
        y,
        ancho - 10,
        alto,
        1
    )

    # Parte central
    display.fill_rect(
        x,
        y + 5,
        ancho,
        alto - 10,
        1
    )


# ============================================================
# DIBUJAR LOS DOS OJOS
# ============================================================

def dibujar_ojos(desplazamiento, display):

    display.fill(0)

    # Ojo izquierdo
    ojo(5 + desplazamiento, 5, 52, 28, display)

    # Ojo derecho
    ojo(71 + desplazamiento, 5, 52, 28, display)

    display.show()


# ============================================================
# PARPADEO
# ============================================================

def parpadear(display):

    display.fill(0)

    # Ojos cerrados
    display.fill_rect(5, 18, 52, 4, 1)
    display.fill_rect(71, 18, 52, 4, 1)

    display.show()

    time.sleep_ms(120)

    # Abrir
    dibujar_ojos(0, display)

    time.sleep_ms(100)


# ============================================================
# GUIÑO
# ============================================================

def guiño(display):

    display.fill(0)

    # Ojo izquierdo abierto
    ojo(5, 5, 52, 28, display)

    # Ojo derecho cerrado
    display.fill_rect(71, 18, 52, 4, 1)

    display.show()

    time.sleep_ms(250)

    dibujar_ojos(0, display)

    time.sleep_ms(150)


# ============================================================
# OJO GRANDE
# ============================================================

def ojo_grande(display):

    display.fill(0)

    # Ojo izquierdo
    ojo(8, 11, 43, 22, display)

    # Ojo derecho grande
    ojo(67, 2, 56, 34, display)

    display.show()


# ============================================================
# ENOJADO
# ============================================================

def enojado(display):

    display.fill(0)

    # Ojos
    ojo(5, 9, 52, 25, display)
    ojo(71, 9, 52, 25, display)

    # Ceja izquierda inclinada hacia el centro
    display.line(5, 3, 48, 10, 1)
    display.line(5, 4, 48, 11, 1)

    # Ceja derecha inclinada hacia el centro
    display.line(80, 10, 123, 3, 1)
    display.line(80, 11, 123, 4, 1)

    display.show()


# ============================================================
# SONRISA
# ============================================================

def sonrisa(display):

    display.fill(0)

    # Ojos ligeramente cerrados
    display.fill_rect(5, 17, 52, 5, 1)
    display.fill_rect(71, 17, 52, 5, 1)

    # Sonrisa
    display.line(40, 32, 48, 36, 1)
    display.line(48, 36, 57, 39, 1)
    display.line(57, 39, 71, 39, 1)
    display.line(71, 39, 80, 36, 1)
    display.line(80, 36, 88, 32, 1)

    display.show()


# ============================================================
# SONRISA 2
# ============================================================

def sonrisa2(display):

    display.fill(0)

    # Ojos normales
    ojo(5, 5, 52, 28, display)
    ojo(71, 5, 52, 28, display)

    # Sonrisa
    display.line(40, 34, 48, 37, 1)
    display.line(48, 37, 57, 40, 1)
    display.line(57, 40, 71, 40, 1)
    display.line(71, 40, 80, 37, 1)
    display.line(80, 37, 88, 34, 1)

    display.show()


# ============================================================
# OJOS CORAZÓN
# ============================================================

def ojos_corazon(display):

    display.fill(0)

    # Corazón más grande
    corazon = [
        "   XXX     XXX   ",
        " XXXXXXX XXXXXXX ",
        "XXXXXXXXXXXXXXXXX",
        "XXXXXXXXXXXXXXXXX",
        " XXXXXXXXXXXXXXX ",
        "  XXXXXXXXXXXXX  ",
        "   XXXXXXXXXXX   ",
        "    XXXXXXXXX    ",
        "     XXXXXXX     ",
        "      XXXXX      ",
        "       XXX       ",
        "        X        "
    ]

    # Corazón izquierdo
    x0 = 2
    y0 = 2

    for y, fila in enumerate(corazon):
        for x, pixel in enumerate(fila):
            if pixel == "X":
                display.pixel(x0 + x, y0 + y, 1)

    # Corazón derecho
    x0 = 68
    y0 = 2

    for y, fila in enumerate(corazon):
        for x, pixel in enumerate(fila):
            if pixel == "X":
                display.pixel(x0 + x, y0 + y, 1)

    # Boca grande en forma de U
    display.line(45, 38, 49, 42, 1)
    display.line(49, 42, 56, 45, 1)
    display.line(56, 45, 72, 45, 1)
    display.line(72, 45, 79, 42, 1)
    display.line(79, 42, 83, 38, 1)

    display.show()
