# Käyttöohje

Lataa sovelluksen viimeisin [release](https://github.com/JuusoSaavalainen/yatzy_game/releases)

## Konfigurointi

- ei konfiguraatiota

## Ohjelman käyttäminen / aloittaminen

Ennen sovelluksen käynnistystä riippuvuudet on asennettava komennolla:

```bash
poetry install
```

Tämän jälkeen voidaan tietokanta alustaa komennolla:

```bash
poetry run invoke clean
```

Jos haluat myöhemmin esimerkiksi nollata *Highscoret* tai kirjautumistiedot
voit käyttää samaa komentoa 'clean' joka nollaa tietokannan

Näiden toimien jälkeen voidaa ohjelma käynnistää komennolla:

```
poetry run invoke start
```


## Kirjautuminen / Rekisteröinti

Sovelluksen käynnistyessä aukeaa kirjautumiseen ja rekistyröimiseen luotu näkymä:

![](https://github.com/JuusoSaavalainen/yatzy_game/blob/main/dokumentaatio/kuvat/Screenshot%20from%202022-05-15%2016-04-02.png)

Kirjautuminen tapahtuu syöttämällä käyttäjänimen + salasana ja tämän jälkeen painamalla 'Login' nappia.
Tämä ei tosin onnistu ennekuin käyttäjä on rekistyröitynyt. Rekistöröityminen onnistuu syöttämällä
haluamansa nimen + salasanan ja tämän jälkeen klikkaamalla 'Register' nappia.

Rekistyröityessä on syytä huomioida että vain alle 8 merkkiä pitkät nimet ovat kelvollisia järjestelmässä
Toinen huomioitava asia on salasanojen käyttö. Sovelluksen kirjautumis toiminto on hyvin muodollinen ja 
siksi myös salasanojen säilytykseen ei ole kiinnitetty erityistä huomiota. Tämän vuoksi suosittelen käyttämään
salasanana esimerkiksi pistettä tai pilkkua.

## Yatzy peli

Kun kirjautumis näkymästä ollaan päästy eteenpäin rekisteröinnin / kirjautumisen kautta aukeaa itse peli:

![](https://github.com/JuusoSaavalainen/yatzy_game/blob/main/dokumentaatio/kuvat/Screenshot%20from%202022-05-15%2016-04-59.png)

Pelin tarkoitus on kerätä erilaisia pisteitä tuottavia yhdistelmiä nopista noppia heittämällä. 
Pelistä voidaan poistua sulkemalla näkymä. 

