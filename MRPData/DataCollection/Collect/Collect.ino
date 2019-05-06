int cnt = 0;
char mydata = 1;
#define step_pin 3  
#define dir_pin 2  
#define MS1 5    
#define MS2 4    
#define outpin1 6
#define inpin1 7
#define inpin2 8
#//define outpin2 9

int dir;   
int steps = 1; 


void setup() {
  // put your setup code here, to run once:
 Serial.begin(9600);
 
   //pinMode(MS1, OUTPUT); 

   //pinMode(MS2, OUTPUT);   

   //pinMode(dir_pin, OUTPUT); 

   //pinMode(step_pin, OUTPUT);  

   // the following 3 is for the stoppers

   //pinMode (outpin1, OUTPUT);

   //pinMode(inpin1, INPUT);

   //pinMode(inpin2, INPUT);

   //digitalWrite(MS1, LOW);   

   //digitalWrite(MS2, LOW);   

   //digitalWrite(outpin1, HIGH);  

   //digitalWrite(outpin2, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  mydata = int(Serial.read());
  //pinread1 = digitalRead(inpin1); 
  //pinread2 = digitalRead(inpin2);
  //&& digitalRead(inpin2) == HIGH
  // the point here is to have the direction and moving functions separate! 
  // this way we can have one move fcn, dependent on the direction defined by the direction functions
  Serial.println("Y");
  //if (digitalRead(inpin1) == HIGH && digitalRead(inpin2) == HIGH)
  //      if (mydata == '1')
  //        digitalWrite(step_pin, HIGH);
  //        delay(5);
  //        digitalWrite(step_pin, LOW);   
  //        delay(5);   
  //      if (mydata=='0')
  //        Serial.println("nothing");
  //      if (mydata=='2')
  //        digitalWrite(dir_pin, LOW);
  //      if (mydata=='3')
  //        digitalWrite(dir_pin, HIGH); 
  //if (digitalRead(inpin1) == LOW)
  //    Serial.println("You have reached the end");
  //    digitalWrite(step_pin, LOW);
  //if (digitalRead(inpin2) == LOW)
  //    Serial.println("You have reached the end");
  //    digitalWrite(step_pin, LOW);
}
