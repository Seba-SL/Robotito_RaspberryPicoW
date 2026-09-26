import time
import network

ap = None
clientes_anterior = []


def iniciar_red(SSID, PASSWORD):

    global ap

    ap = network.WLAN(network.AP_IF)

    ap.active(True)
    ap.config(
        ssid=SSID,
        password=PASSWORD
    )

    while not ap.active():
        pass

    print("Wi-Fi iniciado")
    print("SSID:", SSID)
    print("IP:", ap.ifconfig()[0])


def actualizar():



    return 3