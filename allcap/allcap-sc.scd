s.boot

// warp_controller.scd
(
// 1. Debug OSC
OSCdef(\oscDebug, { |msg|
    "OSC recibido:".postln;
    msg.postln;
}, '/touch');

// 2. SynthDef
SynthDef(\granularWarp, {
    arg bufnum, pointer=0, freqScale=1, windowSize=0.05, amp=0.7;
    var sig = Warp1.ar(
        1, bufnum, 
        pointer.clip(0, 1), 
        freqScale.clip(0.25, 4), 
        windowSize.clip(0.001, 0.2),
        overlaps: 8
    ) * amp;
    Out.ar(0, sig ! 2);
}).add;

// 3. Sistema principal
s.waitForBoot {
    ~buffer = Buffer.read(s, Platform.resourceDir +/+ "sounds/a11wlk01.wav", action: {
        ~warp = Synth(\granularWarp, [\bufnum, ~buffer]);
        
        OSCdef(\touchControl, { |msg|
            var vals = msg[1..3];
            if(vals.size == 3) {
                ~warp.set(
                    \pointer, vals[0].linlin(800, 3500, 0, 1),
                    \freqScale, vals[1].linlin(800, 3500, 0.5, 2),
                    \windowSize, vals[2].linlin(800, 3500, 0.001, 0.1)
                );
                "Controles actualizados:".postln;
                ["Pointer", "FreqScale", "WindowSize"].do { |name, i|
                    (name + ": " + vals[i]).postln;
                };
            };
        }, '/touch');
    });
};
)