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
      // Blink green LED 3 times
      for (int i = 0; i < 3; i++) {
        digitalWrite(greenLED, HIGH);
        delay(200);
        digitalWrite(greenLED, LOW);
        delay(200);
      }
    }

    else if (command == "PHISH") {
      // Blink red LED + buzzer 3 times
      for (int i = 0; i < 3; i++) {
        digitalWrite(redLED, HIGH);
        digitalWrite(buzzer, HIGH);
        delay(200);

        digitalWrite(redLED, LOW);
        digitalWrite(buzzer, LOW);
        delay(200);
      }
    }

    else {
      digitalWrite(greenLED, LOW);
      digitalWrite(redLED, LOW);
      digitalWrite(buzzer, LOW);
    }
  }
}
