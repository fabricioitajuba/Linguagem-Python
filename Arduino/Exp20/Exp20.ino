//Exemplo de utilização do Arduino com o Python
//Leitura do conversor AD e plotar no gráfico
//Eng. Fabrício de Lima Ribeiro
//17/11/2020


const int analogInPin = A0;
int sensorValue = 0;
float voltageValue = 0;
unsigned long lastTime = 0 , sampleTime = 100;

void setup() {
  
  Serial.begin(9600);

}

void loop() {

  if(millis()-lastTime>sampleTime){

    lastTime = millis();
    sensorValue = analogRead(analogInPin);
    voltageValue = scaling(sensorValue, 0, 1023, 0, 5);
    Serial.println(voltageValue);    
    
  }

}

float scaling(float x, float in_min, float in_max, float out_min, float out_max){

  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
  
}
