#include <wiringPi.h>
#include <signal.h>

const int ledCarRed = 5;
const int ledCarYellow = 6;
const int ledCarGreen = 13;

const int ledPedestrianRed = 19;
const int ledPedestrianGreen = 26;
const int ledPedestrianIndicator = 22;

const int pinButton = 4;
const int pinPir = 23;

const int lightDelay = 1;
const int waitTraffic = 4;

int running = 1;
int exitSignal = 0;

/* Clean on signal (i.e. exit) */
void signalHandler(int signal) {
  digitalWrite(ledCarGreen, 0);
  digitalWrite(ledCarYellow, 0);
  digitalWrite(ledCarRed, 0);
  digitalWrite(ledPedestrianRed, 0);
  digitalWrite(ledPedestrianGreen, 0);
  digitalWrite(ledPedestrianIndicator, 0);

  running = 0;
  exitSignal = signal;
}

void switchToCarRed() {
  digitalWrite(ledPedestrianIndicator, 1);
  if (digitalRead(pinPir) == HIGH) {
    delay(waitTraffic);
  }
  digitalWrite(ledCarGreen, 0);
  digitalWrite(ledCarYellow, 1);
  delay(lightDelay);
  digitalWrite(ledCarYellow, 0);
  digitalWrite(ledCarRed, 1);
  delay(lightDelay);
  digitalWrite(ledPedestrianRed, 0);
  digitalWrite(ledPedestrianGreen, 1);
  digitalWrite(ledPedestrianIndicator, 0);
}

int main (void)
{
  if (wiringPiSetup() == -1)
    return 1;

  signal(SIGINT, signalHandler);

  pinMode(ledCarRed, OUTPUT);
  pinMode(ledCarYellow, OUTPUT);
  pinMode(ledCarGreen, OUTPUT);
  pinMode(ledPedestrianRed, OUTPUT);
  pinMode(ledPedestrianGreen, OUTPUT);
  pinMode(ledPedestrianIndicator, OUTPUT);

  pinMode(pinButton, INPUT);
  pinMode(pinPir, INPUT);

  /* Default values */
  digitalWrite(ledCarGreen, 1);
  digitalWrite(ledCarYellow, 0);
  digitalWrite(ledCarRed, 0);
  digitalWrite(ledPedestrianRed, 1);
  digitalWrite(ledPedestrianGreen, 0);
  digitalWrite(ledPedestrianIndicator, 0);
  
  while(running) {
    if (digitalRead(pinButton) == HIGH) {
      switchToCarRed();
    }
    delay(100);
  }

  return 0;
}
