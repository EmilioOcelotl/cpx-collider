// Definir un OSCdef para enviar los valores de los LEDs
(
OSCdef(\ledControl, { |msg|
    var ledValues = msg[1..(45 * 3)];  // Tomar los primeros valores correspondientes a 45 LEDs (3 valores por LED)
    m.sendMsg("/leds", *ledValues);  // Enviar por OSC al programa Python
}, '/ledsDef');
)

(
// Generador de valores y envío continuo por OSC
~ledControlSend = {
    SendReply.kr(
        Impulse.kr(10),  // Impulso a 30 Hz para generar datos cada ~33ms
        '/ledsDef',  // Mensaje OSC
        Array.fill(45 * 3, { |i|
            // Generar valores aleatorios o basados en FFT para cada LED RGB
			Demand.kr(Onsets.kr(FFT(LocalBuf(512), SoundIn.ar(0)), 0.5), 0, Dseq([255, 0, 0, [100, 0, 255].choose, 0, 0, 255], inf)) // Valores entre 0 y 255 para RGB
        })
    );
};
)

coin
// Iniciar el envío continuo
~ledControlSend.value;

// Libera el OSCdef cuando ya no lo necesites
 OSCdef(\ledControl).free;

s.meter
