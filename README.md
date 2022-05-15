# Yatzy :game_die: "Peli"

## Dokumentaatio

[Käyttöohje](https://github.com/JuusoSaavalainen/yatzy_game/blob/main/dokumentaatio/kayttoohje.md)

[Changelog](https://github.com/JuusoSaavalainen/ot-harjoitusty-/blob/main/dokumentaatio/changelog.md)

[Vaatimusmaarittely](https://github.com/JuusoSaavalainen/ot-harjoitusty-/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Tyoaikakirjanpito](https://github.com/JuusoSaavalainen/ot-harjoitusty-/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[Arkkitehtuuri](https://github.com/JuusoSaavalainen/ot-harjoitusty-/blob/main/dokumentaatio/arkkitehtuuri.md)


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
