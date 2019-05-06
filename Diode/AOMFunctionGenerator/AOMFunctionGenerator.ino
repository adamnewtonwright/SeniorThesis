// Adam Newton Wright
// 01.17.2018
// Code to control the AOM

/*
We want to output 3.3V at a repetition rate of 100 kHz with a duty cycle of 10% ?
 */

float RepRate = 200.0E3; // Desired Repetition Rate
float PulseSep = 5E-6;
float DutyCycle = .2; // Gives desired duty cycle as percentage
float PulseOn =  (1.0E6 * DutyCycle) / (RepRate); // time voltage is on in µs
float PulseOff = (1.0-DutyCycle) * 1.0E6 / (RepRate); // time voltage is off in µs


void setup() 
{
  // DDRB is direct port registering; can look it up on arduino; great for microseconds
DDRB = B10000000; // This should configure pins 8 - 12 as input, pin 13 as output.
//pinMode(13, OUTPUT);           // set pin to input

}

void loop() 
{
  // Turn on pin 13
  PORTB = B10000000;
  //digitalWrite(13, HIGH);       // turn on pullup resistors
  // Stay for certain amount of time
  delayMicroseconds(100);
  // Turn off pin 13
  PORTB = B00000000;
  //digitalWrite(13, LOW);       // turn on pullup resistors
  // Stay off for certain amount of time
  delayMicroseconds(400  );
}
