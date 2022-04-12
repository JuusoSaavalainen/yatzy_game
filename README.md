# Yatzy "Peli"


## Dokumentaatio

[changelog.md](https://github.com/JuusoSaavalainen/ot-harjoitusty-/blob/main/dokumentaatio/changelog.md)

[vaatimusmaarittely.md](https://github.com/JuusoSaavalainen/ot-harjoitusty-/blob/main/dokumentaatio/vaatimusmaarittely.md)

[tyoaikakirjanpito.md](https://github.com/JuusoSaavalainen/ot-harjoitusty-/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[arkkitehtuuri.md](https://github.com/JuusoSaavalainen/ot-harjoitusty-/blob/main/dokumentaatio/arkkitehtuuri.md)

## Asentaminen

1. Asenna riippuvuudet näin:

poetry install

## Komentorivin toiminnot

1. Käynnistä Yatzy komennolla:

- poetry run invoke start

2. Testien ajo onnistuu komennolla:

- poetry run invoke test

3. Testikattavuusraportti voidaan generoida komennolla:

- poetry run invoke coverage-report

4. Pylint raportti:

- poetry run invoke lint
