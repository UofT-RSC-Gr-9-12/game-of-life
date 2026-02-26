#include <PulseSensorPlayground.h>

// Pulse Sensor Pin
const int PULSE_PIN = A0;
PulseSensorPlayground pulseSensor;

int BPM = 0;
int threshold = 550;

float filteredSignal = 0;
float alpha = 0.4;   // 0.2–0.4 works well for pulse sensors

void setup() {
  Serial.begin(115200);

  // Pulse Sensor Setup
  pulseSensor.analogInput(PULSE_PIN);
  pulseSensor.setThreshold(threshold); // Adjust if needed

  if (pulseSensor.begin()) {
    Serial.println("Pulse Sensor Ready!");
  }
}

void loop() {
  int myBPM = pulseSensor.getBeatsPerMinute();

  if (pulseSensor.sawStartOfBeat()) {
    BPM = myBPM;
    Serial.print("♥ BPM: "); 
    Serial.println(BPM);
  }

  int rawSignal = pulseSensor.getLatestSample();
  filteredSignal = (alpha * rawSignal) + ((1.0 - alpha) * filteredSignal);

  Serial.print(threshold);
  Serial.print(",");
  Serial.println(filteredSignal);

  delay(20);
}