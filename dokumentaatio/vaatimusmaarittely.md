# Vaativuusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on mahdollistaa **Yatzy** pelin pelaaminen yksinkertaisella alustalla. Sovellus sisältää rekisteröityneen käyttäjän joka mahdollistaa käyttäjäkohtaisen highscore seurannan.

## Käyttäjät

Yksi käyttäjärooli _norm käyttäjä_. 

## Käyttöliittymäluonnos

Sovellus koostuu 4 näkymästä.

![](./kuvat/kayttoliittymaluonnos.png)

Sovellus aukeaa näkymään josta voidaan tarkastella **Highscoreja** , **Kirjautua sisään**/**LOGIN** sekä rekistöröityä. Kirjautuminen hoidetaan alkunäkymässä, rekistöröinti vie toiseen ikkunaan. Tämän jälkeen rekistöröity nimi ja salasana sekä painikkeen **LOGIN** painaminen vie peliin jossa itse peli on toteutettu. Pelin päättymisen jälkeen on mahdollisuus ottaa uusintaottelu tai lopettaa. Myös **Highscorejen** tarkastelu on mahdollista.   

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista
- Käyttäjä voi siirtyä tarkastelemaan parhaita tuloksia laskevassa järjestyksessä 
- Käyttäjä voi siirtyä kirjautumaan sisään
- Käyttäjä voi luada uuden käyttäjän


### Kirjautumisen jälkeen
- Automaattinen pelin aloitus
- Käyttäjä voi heittää noppia 3 kertaa sekä valita säästettäviä noppia ensi kierrokselle
- Käyttäjä voi päättää vuoron ennen 3 heittoa.
- Käyttäjä voi tilanteessa jossa mikään luokka ei sovi saatuihin noppiin päättää ~~ylivaamisen~~ kohteen.
- Vuoron päätyttyä käyttäjä voi valita sopivista paikoista sijoittaa saadut nopat
- Käyttäjä voi tarkastella Highscoreja
- Pelin aikainen pelin päättäminen
- Pelin loputtua uusintapelin mahdollisuus

### Highscores
- Yksinkertainen näkymä jossa käyttäjä voi tarkastella parhaita tuloksia


## Jatkokehitysideoita

Mahdollisuuksien mukaan sovellusta/peliä voitaisiin vielä parantaa esim näin:

- Aloitusvalikossa sekä pelinaikaisesta näkymästä mahdollisuus tarkastella MatchHistoryä 
- Highscorejen detailed view
- Käyttäjä voi vaikuttaa pelin sääntöihin (Esim : Reaaliaikainen pistelaskuri)
- Käyttäjä voi asettaa tavoittelemansa luokan (Esim : vitoset) 
