/*
  Read the analog input pin A0 on demand ("0" from Serial)
  0 read Analog Input 0
  1 read Analog Input 1
*/

byte Cmd;

void setup() {
  Serial.begin(9600);
}

void loop() {
  while (Serial.available() > 0) {
    Cmd = Serial.read();
    //set the torque output value of motor 1 TILT VALUE
    // read the input on analog pin 0:
    int SensorA0 = analogRead(A0);
    int SensorA1 = analogRead(A1);

    if (Cmd == '0'){  //move one step
      Serial.println(SensorA0);
    }
    if (Cmd == '1'){  //move one step
      Serial.println(SensorA1);
    }
    Serial.flush();
  }
}
