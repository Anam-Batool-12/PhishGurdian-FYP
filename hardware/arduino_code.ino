int greenLED = 8;
int redLED = 9;
int buzzer = 10;

void setup() {
  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT);
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');

    if (command == "SAFE") {
      digitalWrite(greenLED, HIGH);
      digitalWrite(redLED, LOW);
      digitalWrite(buzzer, LOW);
    } 
    else if (command == "PHISH") {
      digitalWrite(redLED, HIGH);
      digitalWrite(greenLED, LOW);
      digitalWrite(buzzer, HIGH);
    } 
    else {
      // turn all off if unknown command
      digitalWrite(greenLED, LOW);
      digitalWrite(redLED, LOW);
      digitalWrite(buzzer, LOW);
    }
  }
}
