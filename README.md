# Kirja-arvostelut

## Kuvaus aiheesta 

Kirja-arvosteluihin tarkoitetulla foorumilla käyttäjät voivat ilmoittaa lukemiaan kirjoja ja antaa niille arvosteluita. Käyttäjät voivat rekisteröityä palveluun ja lisätä julkiselle listalle uuden kirja, jos he ovat sen lukeneet. Yleiseltä listalta voi myös valita lukemiaan kirjoja, jos joku muu on ne jo ehtinyt lisätä aikaisemmin. Lukemalleen kirjalle voi lisätä arvostelun ja kaikille kirjoille on nähtävissä muiden antamat arvostelut. Arvostelu koostuu arvosanasta 0-5 ja vapaamuotoisesta tekstistä. Sivu osaa näyttää arvosteluiden perusteella tilastoja aktiivisimmista arvostelijoista, parhaiten arvostelluista kirjoista ja eniten luetuista kirjoista.

## Toiminnot 

* Kirjautuminen ja rekisteröityminen.

* Kirjan lisääminen julkiselle kirjalistalle. Pääkäyttäjä voi myös poistaa tältä listalta kirjoja.

* Kirjan siirtäminen omalle listalle (kirjan ilmoittaminen luetuksi) ja sieltä poisto.

* Kirja-arvostelun antaminen, sekä sen muokkaus ja poisto.

* Arvosteluiden tarkasteleminen kirjakohtaisesti. Omat arvostelut on myös nähtävissä yhdellä sivulla.

* Yhteenvetokyselyiden tarkastelu

## Asennus omalle tietokoneelle

Asennusohjeissa oletetaan, että käytössä on Linux-käyttöjärjestelmä ja Python3 (3.5 tai uudempi) sekä SQlite3. Myös Git-ohjelmistosta on hyötyä projektin kloonaamisessa.

* Lataa tämä Git-repositorio koneellesi zip-pakettina tai kloonaa se komennolla `git clone https://github.com/guotin/tietokantasovellus`

* Navigoi projektin juurikansioon ja luo tarvittava virtuaaliympäristö komennolla `python3 -m venv venv`

* Käynnistä luomasi virtuaaliympäristö komennolla `source venv/bin/activate`

* Asenna projektin vaatimat riippuvuudet komennolla `pip install -r requirements.txt`

* Käynnistä sovellus komennolla `python run.py`

* Sovellus pyörii nyt selaimessasi osoitteessa `localhost:5000`

## Käyttöohjeet ja testitunnukset Herokuun

### Heroku testitunnukset:

Admin-käyttäjällä on oikeudet kirjojen poistamiseen julkiselta listalta.

* username: `test`, password: `test`

* username: `admin`, password: `admin`


### Sovelluksen käyttöohjeet

* Siirry Heroku-linkistä sovellukseen tai asenna ohjelma omalle tietokoneellesi ohjeiden mukaisesti

* Voit luoda käyttäjän rekisteröitymällä. Lisäksi Heroku-versiossa sinulla on pääsy testitunnuksiin.

* Paikallisessa versiossa joudut luomaan "admin" tunnuksilla varustetun käyttäjän itse avaamalla sovelluksen tietokannan `books.db` SQlite3:lla ja esimerkiksi syöttämällä komennon `INSERT INTO account (username, password, admin) values ('admin', 'admin', '1');`

* Rekisteröitymisen ja kirjautumisen jälkeen sinulla on pääsy kaikkiin muihin sovelluksen toiminnallisuuksiin 


## Linkkejä

[Heroku](https://enigmatic-lake-26343.herokuapp.com/)

[Tietokantakaavio](https://github.com/guotin/tietokantasovellus/blob/master/documentation/database_chart.png)

[Käyttäjätarinat](https://github.com/guotin/tietokantasovellus/blob/master/documentation/user_stories.md)
