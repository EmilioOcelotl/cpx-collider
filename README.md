# cpx-collider

Conexión entre Circuit Playground Express (CPX) y SuperCollider. Envío de información de los pines con tacto capacitivo por medio de OSC. 

## Entorno virtual

Para todos los ejemplos y casos es necesario generar un entorno virtual. Con python3 y una terminal

``python3 -m venv cpx-collider-venv``

En macOS/Linux es necesario activar el entorno virtual

``source cpx-collider-venv/bin/activate``

en Windows con PowerShell

``.\venv\cpx-collider\Scripts\activate``

y en Windows con Git Bash

``source cpx-collider-venv/bin/activate``

Después es posible instalar la librería python-osc 

``pip3 install python-osc``

También es necesario instalar pyserial

``pip3 install pyserial``

## Circuit Python 

Es posible [instalar Circuit Python](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-quickstart) en la CPX. [Code with Mu](https://codewith.mu/) es un editor funcional para escribir programas en Circuit Python y leer valores.

## Ejemplo básico

Ejemplo básico para enviar información del tacto capacitivo a SuperCollider. 

[CPX](./basic/basic-cpx.py) > [Computadora](./basic/basic-computer.py) > [SuperCollider](./basic/basic-sc.scd)