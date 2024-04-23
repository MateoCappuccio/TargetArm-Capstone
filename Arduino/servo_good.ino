#include <Servo.h>

Servo servo;
int angle = 0; // Initial angle

void setup() {
  servo.attach(9); // Servo connected to pin 9
  servo.write(angle); // Set initial position
  delay(100);
}

void loop() {
  // Rotate clockwise (increasing angle)
  for (angle = 0; angle <= 60; angle++) {
    servo.write(angle); // Set servo position
    delay(100); // Delay for smooth motion
  }
  
  // Rotate counter-clockwise (decreasing angle)
  for (angle = 60; angle >= 0; angle--) {
    servo.write(angle); // Set servo position
    delay(100); // Delay for smooth motion
  }
}
// This code has the tilting starting at +30 and goes to -30
