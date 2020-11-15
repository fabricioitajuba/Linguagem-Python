//Exemplo de utilização do Arduino com o Python
//Leitura do conversor AD
//Eng. Fabrício de Lima Ribeiro
//15/11/2020
//Fonte: https://www.youtube.com/watch?v=iKGYbMD3NT8&list=PLaulI0GDfISkOZnJKNpEN74dS3sD-3zsU&index=5

int analogPin=3;
int data=0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  data = analogRead(analogPin);
  Serial.println(data);
}
