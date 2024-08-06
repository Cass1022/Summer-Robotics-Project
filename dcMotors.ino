// motor A = right side of motor driver
// motor B = left side of motor driver

// Assigning pins for speed control
int motorSpeedA = 3; // ENB controls speed for motors on the right
int motorSpeedB = 9; // ENA controls speed for motors on the left

// Assigning pins for motors on the right
int motorA1 = 4;
int motorA2 = 5;

// Assignning pins for motors on the left
int motorB1 = 6;
int motorB2 = 7;


void setup() {
  
  // Configure pins to behave as output
  pinMode(motorSpeedA, OUTPUT);
  pinMode(motorSpeedB, OUTPUT);

  pinMode(motorA1, OUTPUT);
  pinMode(motorA2, OUTPUT);
  
  pinMode(motorB1, OUTPUT);
  pinMode(motorB2, OUTPUT);

  // Set motor speed to max (you can adjust these numbers anywhere from 0-255)
  analogWrite(motorSpeedA, 225);
  analogWrite(motorSpeedB, 225);

  // Make motors on the right spin in a certain direction
  digitalWrite(motorA1, HIGH);
  digitalWrite(motorA2, LOW);

  // Make motors on the left spin in a certain direction
  digitalWrite(motorB1, HIGH);
  digitalWrite(motorB2, LOW);

}

void loop() {
  // put your main code here, to run repeatedly:

}
