# Vaativuusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on mahdollistaa **Yatzy** pelin pelaaminen yksinkertaisella alustalla. Sovellus sisältää rekisteröityneen käyttäjän joka mahdollistaa käyttäjäkohtaisen highscore seurannan.

## Käyttäjät

Yksi käyttäjärooli _norm käyttäjä_. 

## Käyttöliittymäluonnos

Sovellus koostuu 2 näkymästä. Näitä ovat pelinaikainen näkymä ja kirjautumis/rekistöröitymis/highscore näkymä.

Sovellus aukeaa näkymään josta voidaan tarkastella **Highscoreja** , **Kirjautua sisään**/**LOGIN** , rekistöröityä sekä tarkastella apuneovoja. Kirjautuminen hoidetaan alkunäkymässä, rekistöröinti voidaan suorittaa samassa ikkunassa sillä siinä ei tarvita muita tietoja kuin sisäänkirjautumisessa. Rekistyröitymisen jälkeen rekistöröity nimi ja salasana sekä painikkeen **LOGIN** painaminen vie pygame ikkunaan jossa itse peli on toteutettu. Pelin päättymisen jälkeen on mahdollisuus ottaa uusintaottelu tai lopettaa.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista
- Käyttäjä voi siirtyä tarkastelemaan parhaita tuloksia laskevassa järjestyksessä 
- Käyttäjä voi siirtyä kirjautumaan sisään
- Käyttäjä voi luada uuden käyttäjän/rekistöröityä
- Käyttäjä voi katesella 'Help!' painikkeella suosituksia ja apua rekistöröitymiseen


### Kirjautumisen jälkeen
- Automaattinen pelin aloitus
- Käyttäjä voi heittää noppia 3 kertaa sekä valita säästettäviä noppia ensi kierrokselle.
- Käyttäjä voi päättää vuoron ennen 3 heittoa.
- Käyttäjä voi tilanteessa jossa mikään luokka ei sovi saatuihin noppiin päättää ~~ylivaamisen~~ kohteen.
- Vuoron päätyttyä käyttäjä voi valita sopivista paikoista mihin tahtoo sijoittaa saadut nopat/tuloksen.
- Pelaaja voi päättää pelin tai käynnistää sen uudelleen painamall näppäintä J.
- Pelin loputtua uusintapelin mahdollisuus.

### Highscores
- Yksinkertainen näkymä jossa käyttäjä voi tarkastella parhaita tuloksia
- Nimet laskevassa järjestyksessä tuloksen perusteella


## Jatkokehitysideoita

Mahdollisuuksien mukaan sovellusta/peliä voitaisiin vielä parantaa esim näin:

- Aloitusvalikossa sekä pelinaikaisesta näkymästä mahdollisuus tarkastella MatchHistoryä 
- Highscorejen detailed view
- Käyttäjä voi vaikuttaa pelin sääntöihin (Esim : Reaaliaikainen pistelaskuri)
- Käyttäjä voi asettaa tavoittelemansa luokan (Esim : vitoset) 
