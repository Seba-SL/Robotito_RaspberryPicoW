
import network
import socket
import time
import motores

ap = None
servidor = None

modo_ojos = "automatico"

EXPRESIONES = (
    "automatico",
    "normal",
    "guino",
    "sonrisa",
    "enojado",
    "corazon",
    "grande",
)

ultimo_movimiento = time.ticks_ms()
TIMEOUT_SEGURIDAD = 800

HTML = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Robot Pico W</title>
<style>
body {
  font-family: Arial, sans-serif;
  background: #edf2f7;
  text-align: center;
  padding: 15px;
}
.panel {
  max-width: 340px;
  margin: auto;
  background: white;
  padding: 20px;
  border-radius: 18px;
}
button {
  width: 85px;
  height: 65px;
  margin: 4px;
  font-size: 26px;
  border: 0;
  border-radius: 12px;
  color: white;
  background: #2563eb;
  touch-action: none;
  user-select: none;
}
.stop { background: #dc2626; }
input { width: 90%; }
</style>
</head>
<body>
<div class="panel">
<h2>Robot Pico W</h2>
<p>Velocidad: <span id="valor">40</span>%</p>
<input id="vel" type="range" min="10" max="100" value="40"
 oninput="valor.textContent=this.value">
<p>
<button data-m="adelante">▲</button>
</p>
<p>
<button data-m="izquierda">◀</button>
<button class="stop" id="stop">■</button>
<button data-m="derecha">▶</button>
</p>
<p>
<button data-m="atras">▼</button>
</p>
<p>Soltá el botón para detener el robot.</p>
</div>

<hr style="margin: 25px 0;">

<h3>Expresiones del robot</h3>

<div class="caras">
  <button class="cara" onclick="cambiarOjos('automatico')">🤖<br><small>Auto</small></button>
  <button class="cara" onclick="cambiarOjos('normal')">👀<br><small>Normal</small></button>
  <button class="cara" onclick="cambiarOjos('guino')">😉<br><small>Guiño</small></button>
  <button class="cara" onclick="cambiarOjos('sonrisa')">😊<br><small>Sonrisa</small></button>
  <button class="cara" onclick="cambiarOjos('enojado')">😠<br><small>Enojado</small></button>
  <button class="cara" onclick="cambiarOjos('corazon')">😍<br><small>Corazón</small></button>
  <button class="cara" onclick="cambiarOjos('grande')">👁️<br><small>Sorpresa</small></button>
</div>

<p id="estadoOjos">Modo automático</p>

<style>
.cara {
  width: 85px;
  height: 65px;
  margin: 4px;
  padding: 5px;
  font-size: 23px;
  background: #475569;
  border-radius: 12px;
}

.cara small {
  font-size: 11px;
}
</style>

<script>
async function cambiarOjos(expresion) {
  const estado = document.getElementById("estadoOjos");

  estado.textContent = "Cambiando expresión...";

  try {
    const respuesta = await fetch(
      "/ojos?e=" + expresion,
      {cache: "no-store"}
    );

    if (!respuesta.ok) {
      throw new Error("Error HTTP");
    }

    estado.textContent = await respuesta.text();

  } catch (error) {
    estado.textContent = "Error de conexión";
  }
}
</script>

<script>
let accion = null;
let repetidor = null;

function enviar(m) {
  const v = document.getElementById("vel").value;
  fetch("/cmd?m=" + m + "&v=" + v,
        {cache: "no-store"}).catch(() => {});
}

function detener() {
  accion = null;
  if (repetidor !== null) {
    clearInterval(repetidor);
    repetidor = null;
  }
  enviar("stop");
}

document.querySelectorAll("[data-m]").forEach(b => {
  b.addEventListener("pointerdown", e => {
    e.preventDefault();
    if (repetidor !== null) clearInterval(repetidor);
    accion = b.dataset.m;
    enviar(accion);
    repetidor = setInterval(() => {
      if (accion) enviar(accion);
    }, 200);
  });

  b.addEventListener("pointerup", e => {
    e.preventDefault();
    detener();
  });

  b.addEventListener("pointercancel", detener);
  b.addEventListener("contextmenu", e => e.preventDefault());
});

document.getElementById("stop").addEventListener(
  "pointerdown", e => {
    e.preventDefault();
    detener();
  }
);

window.addEventListener("pointerup", detener);
window.addEventListener("blur", detener);
document.addEventListener("visibilitychange", () => {
  if (document.hidden) detener();
});
</script>
</body>
</html>
"""


def iniciar_red(SSID, PASSWORD):
    global ap, servidor, ultimo_movimiento

    motores.parar()

    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(ssid=SSID, password=PASSWORD)

    while not ap.active():
        time.sleep_ms(50)

    print("Wi-Fi iniciado")
    print("SSID:", SSID)
    print("IP:", ap.ifconfig()[0])

    servidor = socket.socket()
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind(("0.0.0.0", 80))
    servidor.listen(2)
    servidor.settimeout(0)

    ultimo_movimiento = time.ticks_ms()

    print("Servidor web iniciado")


def ejecutar_comando(ruta):
    global ultimo_movimiento

    if not ruta.startswith("/cmd?"):
        return

    try:
        consulta = ruta.split("?", 1)[1]
        datos = {}

        for elemento in consulta.split("&"):
            partes = elemento.split("=", 1)
            if len(partes) == 2:
                datos[partes[0]] = partes[1]

        accion = datos.get("m", "stop")
        velocidad = int(datos.get("v", "40"))
        velocidad = max(0, min(100, velocidad))

        if accion in ("adelante", "atras", "izquierda", "derecha" ):
            if velocidad == 0:
                motores.parar()
            else:
                getattr(motores, accion)(velocidad)
                ultimo_movimiento = time.ticks_ms()
        else:
            motores.parar()

    except Exception as e:
        print("Error de comando:", e)
        motores.parar()

def ejecutar_comando_ojos(ruta):
    global modo_ojos

    try:
        consulta = ruta.split("?", 1)[1]
        parametros = {}

        for elemento in consulta.split("&"):
            partes = elemento.split("=", 1)

            if len(partes) == 2:
                parametros[partes[0]] = partes[1]

        expresion = parametros.get("e", "automatico")

        if expresion not in EXPRESIONES:
            return "Expresion no valida"

        modo_ojos = expresion

        print("Expresion seleccionada:", modo_ojos)

        return "Modo: " + modo_ojos

    except Exception as e:
        print("Error de expresion:", e)
        return "Error"

def obtener_modo_ojos():
    return modo_ojos


def actualizar():
    global ultimo_movimiento

    # Parada de seguridad si dejan de llegar órdenes
    if time.ticks_diff(time.ticks_ms(),ultimo_movimiento) > TIMEOUT_SEGURIDAD:
        motores.parar()

    if servidor is None:
        return 0

    try:
        cliente, remoto = servidor.accept()
    except OSError:
        return 0

    try:
        cliente.settimeout(0.2)
        peticion = cliente.recv(1024)

        if not peticion:
            return 0

        linea = peticion.decode("utf-8", "ignore").split("\r\n")[0]
        partes = linea.split(" ")

        if len(partes) < 2:
            return 0

        ruta = partes[1]

        if ruta.startswith("/cmd?"):
            ejecutar_comando(ruta)
            cuerpo = "OK"
            tipo = "text/plain"

        elif ruta.startswith("/ojos?"):
            cuerpo = ejecutar_comando_ojos(ruta)
            tipo = "text/plain"

        elif ruta == "/":
            cuerpo = HTML
            tipo = "text/html; charset=utf-8"

        else:
            cuerpo = "Ruta no encontrada"
            tipo = "text/plain"

        respuesta = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: " + tipo + "\r\n"
            "Connection: close\r\n"
            "Cache-Control: no-store\r\n"
            "\r\n" + cuerpo
        )

        cliente.send(respuesta.encode())
        return 1

    
    except OSError as e:
            # Un navegador puede abrir una conexion
            # y no enviar datos a tiempo.
            if e.args and e.args[0] in (110, 11):
                return 0

            print("Error de red HTTP:", e)
            motores.parar()
            return 0

    except Exception as e:
            print("Error HTTP:", e)
            motores.parar()
            return 0

    finally:
        try:
            cliente.close()
        except Exception:
            pass
