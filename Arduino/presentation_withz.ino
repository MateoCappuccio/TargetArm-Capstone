
#include "LiquidCrystal_I2C.h"
#include <Wire.h>

int red_led = 13;
int green_led = 8;
LiquidCrystal_I2C lcd(0x27,  16, 2); 

void setup() {
   lcd.init();
   lcd.backlight();
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(red_led, OUTPUT);
  pinMode(green_led, OUTPUT);
  Serial.begin(9600);
}

void loop() {
    if (Serial.available() > 0) {
        String inputString = Serial.readStringUntil('\n');
        // Assuming inputString format: "distance_value,z_value"
        int commaIndex = inputString.indexOf(',');
        if (commaIndex != -1) {
            String distanceString = inputString.substring(0, commaIndex);
            String zString = inputString.substring(commaIndex + 1);
            float distance = distanceString.toFloat();
            int z = zString.toInt();
            printDistance(distance);
        }
  }
}

void printDistance(String input) {
  if (distance < 12) {
    digitalWrite(red_led, HIGH); // Turn on red LED
    digitalWrite(green_led, LOW); // Turn off green LED
    lcd.clear(); // Clear the LCD
    lcd.setCursor(0, 0);
    lcd.print("Object at");
    lcd.setCursor(0, 1);
    lcd.print(distance);
    lcd.setCursor(5,1);
    lcd.print("inches");
    lcd.setCursor(9,1);
    lcd.print(z);
    lcd.setCursor(13,1);
    lcd.print("deg");
  } else {
    digitalWrite(green_led, LOW); // Turn off green LED
    digitalWrite(red_led, HIGH); // Turn on red LED
    lcd.clear(); // Clear the LCD
    lcd.setCursor(0, 0);
    lcd.print("Clear");
  }
}
