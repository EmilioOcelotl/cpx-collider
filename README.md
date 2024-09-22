# cpx-collider

Conexión entre Circuit Playground Express (CPX) y SuperCollider. Envío de información de los pines con tacto capacitivo por medio de OSC. 

## Entorno virtual

Para todos los ejemplos y casos es necesario generar un entorno virtual. Con python3 y una terminal

``python3 -m venv cpx-collider``

En macOS/Linux es necesario activar el entorno virtual

``source cpx-collider/bin/activate``

en Windows

``cpx\Scripts\activate``

Después es posible instalar la librería python-osc 

``pip3 install python-osc``

También es necesario instalar pyserial

``pip3 install pyserial``

## Circuit Python 

La placa CPX puede ejecutar Circuit Python. El editor Mu puede ser un punto de partida incial. 

## Ejemplo básico

Ejemplo básico para enviar información del tacto capacitivo 

[CPX](./basic/basic-cpx.py) > [Computadora](./basic/basic-computer.py) > [SuperCollider](./basic/basic-sc.scd)