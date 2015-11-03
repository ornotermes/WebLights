#include <Adafruit_NeoPixel.h>
#include <avr/power.h>

#define PIN 6

uint8_t leds[451];
uint16_t usedleds = 150;
uint16_t led = 0;
uint8_t r = 0;
uint8_t g = 0;
uint8_t b = 0;

// Parameter 1 = number of pixels in strip
// Parameter 2 = Arduino pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(usedleds, PIN, NEO_GRB + NEO_KHZ800);

// IMPORTANT: To reduce NeoPixel burnout risk, add 1000 uF capacitor across
// pixel power leads, add 300 - 500 Ohm resistor on first pixel's data input
// and minimize distance between Arduino and first pixel.  Avoid connecting
// on a live circuit...if you must, connect GND first.

void setup() {
  // This is for Trinket 5V 16MHz, you can remove these three lines if you are not using a Trinket
#if defined (__AVR_ATtiny85__)
  if (F_CPU == 16000000) clock_prescale_set(clock_div_1);
#endif
  // End of trinket special code
  Serial.begin(9600);

  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
}

void loop() {
  reciveData();
}

void reciveData() {
  while (Serial.available() > 0) {
    switch (Serial.read())
    {
      case 'c':
        strip.clear();
        led = 0;
        break;
      case 's':
        r = Serial.read();
        g = Serial.read();
        b = Serial.read();
        strip.setPixelColor(led, r, g, b),
        led++;
        break;
      case 't':
        strip.show();
        led = 0;
        break;
    }
  }
}
