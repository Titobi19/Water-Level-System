int trig = 3;
int echo = 4;

void setup() {
  // put your setup code here, to run once:
pinMode(echo,INPUT);
pinMode(trig,OUTPUT);
Serial.begin(9600);
} 

void loop() {
  // put your main code here, to run 
  digitalWrite(trig,HIGH);
  delay(200);
  digitalWrite(trig,LOW); 
 // 20 is the total height of the container i am using
  int period = pulseIn(echo,HIGH);
  int distance = 20-((period/2)/29.1);

  Serial.print("Distance = ");
  Serial.println(distance);
}
