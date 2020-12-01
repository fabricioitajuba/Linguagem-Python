//Exemplo de utilização do Arduino com o Python
//Recebe um dado pela serial e envia outro
//Eng. Fabrício de Lima Ribeiro
//01/12/2020
//Fonte: https://www.youtube.com/watch?v=WV4U51TlRaQ&list=PLaulI0GDfISkOZnJKNpEN74dS3sD-3zsU&index=4

int analogPin=3;
int data=0;
char userInput;

void setup() {
  Serial.begin(9600);
}

void loop() {
  userInput = Serial.read();
  if(userInput == 'g'){
    for(int i=0; i<10; i++){
      data = analogRead(analogPin);
      Serial.println(data);
    }
  }
}
