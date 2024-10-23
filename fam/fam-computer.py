import serial
import time
from pythonosc import dispatcher
from pythonosc import osc_server

# Configura el puerto serial
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)  # Ajusta según tu sistema

# Función para enviar valores a CPX vía serial
def send_to_cpx(values):
    led_data = ','.join(map(str, values)) + '\n'  # Formatear como "val1,val2,val3,...\n"
    ser.write(led_data.encode('utf-8'))
    print(f"Enviado a CPX: {led_data.strip()}")

# Función para manejar mensajes OSC
def osc_handler(unused_addr, *args):
    # Asume que args contiene tantos valores como LEDs a controlar
    values = list(args)
    print(f"Recibido OSC: {values}")
    send_to_cpx(values)

# Configurar el dispatcher para recibir mensajes OSC
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/leds", osc_handler)  # Mapeo del mensaje OSC "/leds"

# Configurar el servidor OSC
ip = "127.0.0.1"  # Localhost
port = 57120      # Puerto OSC donde se escuchará
server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)

print(f"Escuchando en {ip}:{port} para mensajes OSC...")
server.serve_forever()
