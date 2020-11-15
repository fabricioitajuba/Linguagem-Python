//Exemplo de utilização do Arduino com o Python
//Recebendo varios dados pela serial
//Eng. Fabrício de Lima Ribeiro
//15/11/2020
//Fonte: https://www.youtube.com/watch?v=qg9sO4AD8-A

int analogPin=3;
int data=0;
char userInput;

void setup() {
  Serial.begin(9600);
}

void loop() {
  userInput = Serial.read();

  if(userInput == 'g'){
    data = analogRead(analogPin);
    Serial.println(data);
  }
}
