CC=gcc
LIBS="-lwiringPi"
CFLAGS="-I. -Wall -Wextra -std=c89 -pedantic -Wmissing-prototypes -Wstrict-prototypes -Wold-style-definition -g -O3"
OBJ=trafficlights.o
DEPS=""

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS) $(LIBS)

trafficlights: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

clean:
	rm $(OBJ) trafficlights