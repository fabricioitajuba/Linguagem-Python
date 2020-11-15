//Exemplo de utilização do Arduino com o Python
//Leitura do conversor AD
//Eng. Fabrício de Lima Ribeiro
//15/11/2020

int analogPin=3;
int data=0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  data = analogRead(analogPin);
  Serial.println(data);
}
