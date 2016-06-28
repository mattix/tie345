#include <wiringPi.h>
#include <signal.h>

const int pirPin = 4; /* BCM GPIO 23 */
const int ledPin = 0; /* BCM GPIO 17 */
int running = 1;
int exitSignal = 0;

/* Clean on signal (i.e. exit) */
void signalHandler(int signal) {
  digitalWrite(ledPin, 0);
  running = 0;
  exitSignal = signal;
}

int main (void) {
  if (wiringPiSetup() == -1)
    return 1;

  signal(SIGINT, signalHandler);

  pinMode(ledPin, OUTPUT);
  pinMode(pirPin, INPUT);

  while(running) {
    digitalWrite(ledPin, digitalRead(pirPin) == HIGH ? 1 : 0);
    delay(100);
  }

  return exitSignal;
}