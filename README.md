# Yatzy "Peli"


## Dokumentaatio

[changelog.md](https://github.com/JuusoSaavalainen/ot-harjoitusty-/blob/main/dokumentaatio/changelog.md)

[vaatimusmaarittely.md](https://github.com/JuusoSaavalainen/ot-harjoitusty-/blob/main/dokumentaatio/vaatimusmaarittely.md)

[tyoaikakirjanpito.md](https://github.com/JuusoSaavalainen/ot-harjoitusty-/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[arkkitehtuuri.md](https://github.com/JuusoSaavalainen/ot-harjoitusty-/blob/main/dokumentaatio/arkkitehtuuri.md)

## Asentaminen

1. Asenna riippuvuudet näin:

poetry install

2. Alusta tietokanta komennolla:

- poetry run invoke clean


## Pelin käynnistäminen

1. Käynnistä Yatzy komennolla:

- poetry run invoke start

## Testaaminen

1. Testien ajo onnistuu komennolla:

- poetry run invoke test

2. Testikattavuusraportti voidaan generoida komennolla:

- poetry run invoke coverage-report

3. Pylint raportti komennolla:

- poetry run invoke lint
