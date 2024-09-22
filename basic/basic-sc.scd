(
OSCdef.new(
    \touchData,
    { |msg|
        var touchValue = msg[1];
        ("Valor recibido: " ++ touchValue).postln;

        // Usar el valor para controlar un parámetro en SuperCollider
        ~freq = (touchValue.linexp(0, 127, 100, 1000));
        ~synth.set(\freq, ~freq);
    },
    '/touch'
);

// Crear un sintetizador para probar
~synth = SynthDef(\simpleSynth, {
    arg freq = 440;
    Out.ar(0, SinOsc.ar(freq) * 0.1);
}).play;
)