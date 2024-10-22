#include <Adafruit_NeoPixel.h>
#define PIN            17   // Pin para la tira de NeoPixels
#define NUMPIXELS      45   // Número de LEDs en la tira
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(115200);
  strip.begin();
  strip.show();  // Inicializa todos los LEDs apagados
}

void loop() {
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');  // Leer línea de la entrada serial
    input.trim();  // Elimina espacios en blanco

    if (input.length() > 0) {
      // Divide la cadena en valores separados por comas
      int ledValues[NUMPIXELS];
      int index = 0;
      char *token = strtok((char *)input.c_str(), ",");
      while (token != nullptr && index < NUMPIXELS) {
        ledValues[index++] = atoi(token);  // Convierte cada valor a entero
        token = strtok(nullptr, ",");
      }
      
      // Actualiza los LEDs
      for (int i = 0; i < NUMPIXELS; i++) {
        strip.setPixelColor(i, strip.Color(ledValues[i], ledValues[i], ledValues[i]));  // Asume que cada valor es el brillo
      }
      strip.show();  // Refresca los LEDs
    }
  }
}
