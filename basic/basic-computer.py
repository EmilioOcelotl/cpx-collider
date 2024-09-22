import serial
import time
from pythonosc import udp_client

# Configura el puerto serial (ajusta el nombre del puerto según tu sistema)
# En Windows sería algo como 'COM3', en Linux/Mac sería '/dev/ttyACM0'
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

# Configura el cliente OSC
ip_address = "127.0.0.1"  # IP de destino (localhost para SuperCollider)
port = 57120              # Puerto donde SuperCollider escucha OSC
osc_client = udp_client.SimpleUDPClient(ip_address, port)

# Leer datos del CPX y enviarlos como OSC
while True:
    if ser.in_waiting > 0:
        # Leer línea desde el puerto serial y eliminar cualquier espacio extra
        touch_value = ser.readline().decode('utf-8').strip()
        
        if touch_value.isdigit():  # Asegurarse de que sea un número válido
            touch_value = int(touch_value)
            # Mapear el valor (opcional, si necesitas ajustar los rangos)
            print(touch_value)
            mapped_value = max(0, min(127, (touch_value - 100) * 127 // (2000 - 100)))

            # Enviar el valor por OSC
            osc_client.send_message("/touch", mapped_value)
            print(f"Enviado: {mapped_value}")
    
    time.sleep(0.1)
