import time
import board
import touchio

# Configurar los pines táctiles capacitivos
touch_pins = [
    touchio.TouchIn(board.A1),  # Pin 1
    touchio.TouchIn(board.A2),  # Pin 2
    touchio.TouchIn(board.A3)   # Pin 3
]

while True:
    # Leer todos los valores y formatearlos como cadena
    values = [str(touch.raw_value) for touch in touch_pins]
    output = "|".join(values)  # Separador por comas
    
    print(output)  # Ejemplo: "1234,5678,9012"
    
    time.sleep(0.1)