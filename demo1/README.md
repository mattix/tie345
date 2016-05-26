# Demo 1

## Tehtävät

- [X] Laitteet kuitattu
- [X] Raspberryn konfigurointi
- [X] Raspberry päivitetty
- [X] Raspberry liitetty verkkoon
- [X] Salasana vaihdettu
- [X] Github-repo
- [X] Raspbian image kirjoitettu
- [X] Etäkäyttö

## Huomioita

- Kirjoitettu raspbian-lite (ei X:ää)
- Etäkäyttönä ssh
- pi-käyttäjältä poistettu salasana (passwd -d, eli asetettu vanhentuneeksi) ja estetty ssh-kirjautuminen (`/etc/ssh/sshd_config` ja AllowUsers)
- Rootilta poistettu ssh-kirjautuminen kokonaan
