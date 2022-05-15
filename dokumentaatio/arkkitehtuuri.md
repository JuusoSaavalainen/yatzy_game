# Arkkitehtuurikuvaus

## Rakenne

Alkeellinen pakkaus mallinnus

![pakkausrakenne](https://github.com/JuusoSaavalainen/ot-harjoitusty-/blob/main/dokumentaatio/kuvat/pakkausrakenne.png)


## Tietojen pysyväistallennus

Ohjelman tietojen tallentamisesta pysyväismuistiin vastaa [Loginrepo](https://github.com/JuusoSaavalainen/yatzy_game/blob/main/src/repot/yatzyrepo.py)
Se tarjotaa mahdollisuudet lisätä, ja päivittää tietoa tietokantaan. Toteutettu SQLite tietokannan avulla jossa taulu user.
Taulusta löytyy *username*, *password*, *score* ja *active* joiden avulla tuloksia, aktiivisuutta ja tilitietoja ylläpidetään.
Tietokanta voidaan alustaa ja alustetaan tiedostossa [intialize_database.py](https://github.com/JuusoSaavalainen/yatzy_game/blob/main/src/data/intialize_database.py)

## Päätoiminnallisuus

### Kirjautuminen

Sisäänkirjautumista kuvattu sekvenssikaaviolla 

![](https://github.com/JuusoSaavalainen/yatzy_game/blob/main/dokumentaatio/kuvat/login_sekvenssi.png)

Tässä näkyy miten login painikkeen yhteydessä toimitaan. Käytännössä repositoryn metodeilla varmistetaan että kyseinen käyttäjä saa kirjautua ja se asetetaan aktiiviseksi jos näin on jonka jälkeen GUI sulkeutuu ja peli aukeaa. Jos jokin menee vikaan kuten väärät kirjautumistiedot näytetään ruudulla sille kuuluvaa error viestiä


### Rekistöröityminen

Rekistyröitymistä kuvaava sekvenssikaavio:

![](https://github.com/JuusoSaavalainen/yatzy_game/blob/main/dokumentaatio/kuvat/registerreal.png)

Kaaviossa kuvattu toiminta on hyvin lähellä loginin toimintaa. Erona lähinnä se että databasesta tarkistetaan löytyykö jo joku joka on ottanut nimen.
Tämän päättyessä ei myöskään avata peliä vaan vain joko luodaan tai ollaan luomatta uusi käyttäjä tietokantaan.




