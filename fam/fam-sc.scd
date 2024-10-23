// Definir un OSCdef para enviar los valores de los LEDs
(
OSCdef(\ledControl, { |msg|
    var ledValues = msg[1..45];  // Tomar los primeros 45 valores del mensaje OSC
    m.sendMsg("/leds", *ledValues);  // Enviar por OSC al programa Python
}, '/ledsDef');
)

// Generador de valores y envío continuo por OSC
~ledControlSend = {
    SendReply.kr(
        Impulse.kr(30),  // Impulso a 30 Hz para generar datos cada ~33ms
        '/ledsDef',  // Mensaje OSC
        Array.fill(45, { |i|
            // Generar valores aleatorios o basados en FFT para cada LED
			Demand.kr(Onsets.kr(FFT(LocalBuf(512), SoundIn.ar(0)), 0.5), 0, Drand([0, 255], inf))  // Valores entre 0 y 255 para RGB
        })
    );
};

// Iniciar el envío continuo
~ledControlSend.value;

// Libera el OSCdef cuando ya no lo necesites
 OSCdef(\ledControl).free;  // Descomenta esto si deseas liberar el OSCdef en algún momento
