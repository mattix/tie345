# Demo 3

## Tehtävät

- Lämpötila- ja kosteussensorin tehtävät
  - [X] Sensori toimintakuntoon ja dataa ruutuun
  - [X] Sensorin dataa Google Sheetsiin
- Kameran tehtävät
  - [X] Kamera käyttökuntoon
  - [X] Raspin kameran kuvaa ja videoa repoon
  - [X] Liikkeentunnistava kamera.
  - [X] Aseta kamera ottamaan kuva aina tasatunnein
  - [ ] Toteuta web-palvelin, josta voi hakea uusimman tallennetun kuvan

## Huomioita

Pip asennus: https://pip.pypa.io/en/stable/installing/

Kuvan tallennus: sudo raspistill -o test2.jpg``
Videon tallennus: `sudo raspivid -b 10000000 -o test.h264 -t 3000`

Flask asennus: `sudo apt-get install python3-flask`

### Bonus 5
rootin crontab:
```
0 * * * * raspistill -o /home/matti/demo3/static/latest.jpg
```

## Oppimispäiväkirja

### Mikä oli uutta?

### Mikä oli hankalaa tai epäselvää?

### Kauanko käytit aikaa?
