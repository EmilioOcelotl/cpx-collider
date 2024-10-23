#include <Adafruit_NeoPixel.h>

#define PIN            A1   // Pin para la tira de NeoPixels
#define NUMPIXELS      300   // Número de LEDs en la tira (15 LEDS, 3 valores por cada LED RGB)

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
      int ledValues[NUMPIXELS * 3];  // Almacena los valores RGB para cada LED
      int index = 0;
      char *token = strtok((char *)input.c_str(), ",");
      while (token != nullptr && index < NUMPIXELS * 3) {
        ledValues[index++] = atoi(token);  // Convierte cada valor a entero
        token = strtok(nullptr, ",");
      }
      
      // Actualiza los LEDs
      for (int i = 0; i < NUMPIXELS; i++) {
        int r = ledValues[i * 3];      // Rojo
        int g = ledValues[i * 3 + 1];  // Verde
        int b = ledValues[i * 3 + 2];  // Azul
        strip.setPixelColor(i, strip.Color(r, g, b));  // Establece el color del LED i
      }
      strip.show();  // Refresca los LEDs
    }
  }
}