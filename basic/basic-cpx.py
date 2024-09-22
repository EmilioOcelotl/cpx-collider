# Código básico para enviar valores del pin con tacto capacitivo por el puerto serial 

import time
import board
import touchio

# Configurar el pin capacitivo (ejemplo: A1)
touch_pin = touchio.TouchIn(board.A1)

while True:
    # Leer el valor crudo del sensor capacitivo
    touch_value = touch_pin.raw_value
    print(touch_value)  # Enviar el valor por el puerto serial
    time.sleep(0.1)