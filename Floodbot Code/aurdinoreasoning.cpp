String command = "";

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    command = Serial.readStringUntil('\n');
  }

  if (command == "MOVE_FORWARD") {
    Serial.println("MOTORS_FORWARD");
  } 
  else if (command == "STOP") {
    Serial.println("MOTORS_STOP");
  }
}