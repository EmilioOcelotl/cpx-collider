# serial_to_osc.py
import serial
from pythonosc import udp_client
import time

# Configuración OSC
osc_client = udp_client.SimpleUDPClient("127.0.0.1", 57120)

# Configuración Serial
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

def parse_serial_data(data):
    try:
        return [int(val) for val in data.split('|') if val.isdigit()]
    except:
        return None

while True:
    if ser.in_waiting > 0:
        raw_data = ser.readline().decode('utf-8').strip()
        print(f"Dato serial recibido: {raw_data}")  # Depuración
        
        values = parse_serial_data(raw_data)
        
        if values and len(values) == 3:
            # Enviar OSC (asegurar que son números, no strings)
            osc_client.send_message("/touch", values)
            print(f"Enviado OSC: {values}")  # Depuración
    
    time.sleep(0.01)