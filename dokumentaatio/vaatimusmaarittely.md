# Vaativuusmäärittely

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on mahdollistaa **Yatzy** pelin pelaaminen yksinkertaisella alustalla. Sovellus sisältää rekisteröityneen käyttän joka mahdollistaa käyttäjäkohtaisen highscore seurannan.

## Käyttäjät

Yksi käyttäjärooli _norm käyttäjä_. 

## Käyttöliittymäluonnos

Sovellus koostuu 4 näkymästä. (Mahdollisuuksien ja ajan mukaan myös 5 tai jopa 6 näkymää on mahdollista toteuttaa)

#TODO LISÄÄ KUVA

Sovellus aukeaa näkymään josta voidaan tarkastella **Highscoreja** tai **aloittaa peli**. Pelin aloittaminen vie näkymään jossa kirjataan pelaajien nimet ja samalla saadaan tieto siitä pelataanko peliä yksin vai esim kahdestaan vastakkain. Tämän jälkeen **Start!** vie peliin jossa itse peli on toteutettu. Pelin päättymisen jälkeen on mahdollisuus ottaa uusintaottelu tai lopettaa. Myös **Highscorejen** tarkastelu on mahdollista.   

## Perusversion tarjoama toiminnallisuus

## Aloitusvalikko
- Käyttäjä voi siirtyä tarkastelemaan parhaita tuloksia laskevassa järjestyksessä 
- Käyttäjä voi siirtyä pelaamaan / valitsemaan pelaajien määrä

## Pelaajien valinta
- Käyttäjä/Käyttäjät voivat syöttää nimimerkkin jolle pisteet kirjataan
- Nimimerkkien määrän mukaan voidaan aloittaa joko kaksinpeli tai yksinpeli

## Peli
- Käyttäjä voi vuorollaan heittää noppia 3 kertaa sekä valita säästettäviä noppia ensi kierrokselle
- Käyttäjä voi päättää vuoron ennen 3 heittoa.
- Käyttäjä voi tilanteessa jossa mikään luokka ei sovi saatuihin noppiin päättää ~~ylivaamisen~~ kohteen.
- Vuoron päätyttyä käyttäjä voi valita sopivista paikoista sijoittaa saadut nopat
- Käyttäjä voi tarkastella Highscoreja
- Pelin aikainen pelin päättäminen
- Pelin loputtua uusintapelin mahdollisuus

# Highscores
- Yksinkertainen näkymä jossa käyttäjä voi tarkastella parhaita tuloksia


## Jatkokehitysideoita
- Aloitusvalikossa sekä pelinaikaisesta näkymästä mahdollisuus tarkastella MatchHistoryä 
- Highscorejen detailed view
- Käyttäjä voi vaikuttaa pelin sääntöihin (Esim : Reaaliaikainen pistelaskuri)
- Käyttäjä voi asettaa tavoittelemansa luokan (Esim : vitoset) 
- Käyttäjä voi asettaa nelinumeroisen salasanan nimimerkilleen
