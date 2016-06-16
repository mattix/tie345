# Demo 4

## Tehtävät

- [X] Motion asennettu 1p
- [X] Motion tallentaa kuvat ja lokin eri tiedostoon kuin oletustiedosto. 1p
- [X] Motion tallentaa 2 kuvaa ennen liikettä ja 5 sekunnin ajan (?) liikkeen jälkeen. 1p
- [X] Kun Motion havaitsee liikettä, kuvataan 10 sekunnin video. 2p
- [X] OpenCV asennettu onnistuneesti 2p
- [X] Tee kahden kuvan piirteiden vertailu. Käytä ORB-tunnistinta 2p
- [ ] Hanki kuva, jossa on kasvot. Löydä kasvot Haar-Cascadella. Python/samples-kansiosta löytyy valmiiksi ‘koulutettu’ tunnistin 3p
- [ ] Bonus: Kun Motion havaitsee liikettä kuvattavan alueen keskellä, pikamera kuvaa 15 sekunnin videon tapahtuneesta 1p
- [ ] Bonus: Ota kuva kasvoista picameralla ja tunnista kasvot siitä 2p

## Huomioita

### Motion

Lisätty `bcm2835-v4l2` tiedostoon `/etc/modules` (parempi, kuin `/etc/rc.local`)

Motionia ajettava sudona tai lisättävä käyttäjä video-ryhmään. Jälkimmäistä käytin itse.

En ole varma, tarkoitettiinko tehtävässä "kuvataan 10 sekunnin video" tätä asetusta:

```
# Maximum length in seconds of a movie
# When value is exceeded a new movie file is created. (Default: 0 = infinite)
max_movie_time 10
```

Sen aktivoin, vaikka tuohan tarkoittaa sitä, että uusi videotiedosto luodaan, kun 10 sekuntia tulee täyteen.

### OpenCV
Linkkejä:
- http://docs.opencv.org/master/dc/dc3/tutorial_py_matcher.html
- http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_orb/py_orb.html
- http://docs.opencv.org/3.1.0/d7/d8b/tutorial_py_face_detection.html

Testikuvat ovat CC-lisenssillä:
- https://www.flickr.com/photos/draganbrankovic/23754539739
- https://www.flickr.com/photos/draganbrankovic/23243020106

Torvaldsin kuva cc:
- https://fi.wikipedia.org/wiki/Linus_Torvalds#/media/File:Linus_Torvalds_talking.jpeg

## Oppimispäiväkirja

### Mikä oli uutta?

### Mikä oli hankalaa tai epäselvää?

### Kauanko käytit aikaa?
