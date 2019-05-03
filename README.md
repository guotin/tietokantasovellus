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

## Lähdekoodin lataaminen ja sovelluksen asennus

Asennusohjeissa oletetaan, että käytössä on Linux-käyttöjärjestelmä ja Python3 (3.5 tai uudempi). Myös Git-ohjelmistosta on hyötyä projektin kloonaamisessa.

* Lataa tämä Git-repositorio koneellesi zip-pakettina tai kloonaa se komennolla `git clone https://github.com/guotin/tietokantasovellus`

* Navigoi projektin juurikansioon ja luo tarvittava virtuaaliympäristö komennolla `python3 -m venv venv`

* Käynnistä luomasi virtuaaliympäristö komennolla `source venv/bin/activate`

* Asenna projektin vaatimat riippuvuudet komennolla `pip install -r requirements.txt`

## Sovelluksen käynnistäminen paikallisesti

Tehtyäsi ylemmän kohdan asennuksen ohjeiden mukaisesti, olet valmis käynnistämään sovelluksen paikallisesti.

* Käynnistä sovellus komennolla `python run.py`

* Sovellus pyörii nyt selaimessasi osoitteessa `localhost:5000`

## Sovelluksen asentaminen omalle Heroku-palvelimelle

Sovellus on mahdollista asentaa toimimaan pilvipalvelussa. Tässä ohjeet projektin asentamiseen omalle Heroku-palvelimelle. Asennuksessa vaaditaan Heroku CLI -ohjelmistoa ja omia Heroku käyttäjätunnuksia.

* Luo uusi Heroku-sovellus. Komentoon syötetään nimi omalle sovellukselle.

  ```
  heroku create HALUTTU-NIMI
  ```

* Lisää Herokun tiedot paikalliseen Git-versionhallintaan komennolla

  ```
  git remote add heroku https://git.heroku.com/HALUTTU-NIMI.git
  ```

* Lähetä sovellus Herokuun

  ```
  git add .
  git commit -m 'Commit message'
  git push heroku master
  ```
* Tee Herokuun tietokannan ympäristömuuttuja ja luo tarvittava tietokanta
  ```
  heroku config:set HEROKU=1
  heroku addons:add heroku-postgresql:hobby-dev
  ```
* Uudelleenkäynnistä Heroku-sovellus, jotta muutokset tulevat varmasti voimaan
  ```
  heroku restart
  ```
* Sovellus pyörii nyt määrittelemälläsi sivulla. Voit selvittää tarkan osoitteen Herokun omilta sivuilta kirjautumalla tunnuksillasi sisään.

## Pääkäyttäjätunnusten luominen omaan sovellukseen

Jos haluat käyttää kaikkia toiminnallisuuksia omassa sovelluksessa, joudut luomaan admin-tunnukset.

Tämä tapahtuu paikallisessa versiossa avaamalla paikallisen tietokannan `/application/books.db` SQLite3:lla ja syöttämällä seuraavan komennon:

```
INSERT INTO account (username, password, admin) values ('admin', 'admin', '1');
```

Heroku käyttää PostegreSQL:llää ja voit avata tämän komennolla `heroku pg:psql` (asennuksen jälkeen). Nyt voit syöttää taas seuraavan komennon admin-tunnuksien luomiseen:

```
INSERT INTO account (username, password, admin) values ('admin', 'admin', '1');
```

## Testitunnukset demoversioon

Sovellukselle on jo olemassa Herokussa pyörivä demoversio ja sitä pääsee käyttämään siirtymällä siihen alempaa löytyvän linkin avulla. Demoversiossa sinulla on pääsy testitunnuksiin. "Admin" tunnuksilla on pääkäyttäjän oikeudet eli oikeudet kaikkien kirjojen ja arvosteluiden poistamiseen.

* username: `test`, password: `test`

* username: `admin`, password: `admin`


## Sovelluksen käyttöohjeet

* Siirry Heroku-linkistä sovellukseen tai asenna ohjelma omalle tietokoneellesi/Heroku-palvelimellesi ohjeiden mukaisesti.

* Rekisteröityminen tapahtuu painamalla sivuston oikeasta ylänurkasta painiketta `Register`.

* Kirjautuminen olemassaolevilla tunnuksilla tapahtuu oikeassa ylänurkassa sijaitsevalla `Login` -painikkeella.

* Julkisen kirjalistan tarkastelu tapahtuu painamalla `Public book list` -painiketta. Julkiselta listalta voit siirtyä tietyn kirjan       arvosteluihin painamalla `Browse reviews for this book`, muokata kirjan tietoja painamalla `Update data` tai merkata kirjan luetuksi     painamalla `Mark this book as read`. Pääkäyttäjä voi lisäksi poistaa täältä tietyn kirjan `Delete book` -painikkeella. Pääkäyttäjän     siirtyessä tarkastelemaan tietyn kirjan arvosteluita, hänellä on valta poistaa kenen tahansa arvostelu `Delete review` -painikkeella.

* Lukemasi kirjat näet siirtymällä omalle kirjalistallesi `Your book list` -painikkeella. Täällä voit antaa arvosteluita kirjalle `Give   a review` -painikkeella tai poistaa kirjan omalta kirjalistaltasi painamalla `Delete book from your list`. 

* Antamasi kirja-arvostelut näet listattuna painamalla `Your reviews` -painiketta. Täällä voit muokata arvosteluasi painamalla `Update     review` tai poistaa arvostelusi painamalla `Delete review`.

* Uuden kirjan lisäys foorumin tietokantaan onnistuu `Add a book` -painikkeella. Kirjan lisääminen sivustolle lisää sen myös omalle       listallesi eli merkkaa sen luetuksi.

* 5 aktiivisinta arvostelijaa näet `Reviewer hall of fame` -painikkeella.

* 5 luetuinta kirjaa näet `Most read books` -painikkeella.

* 5 parhaiten arvosteltua kirjaa näet `Best graded book` -painikkeella.



Jotkin edellämainituista toiminnallisuuksista vaativat sisäänkirjautumisen. Sivusto ehdottaa heti sisäänkirjaantumista, jos tällaista   toimintoa koitetaan tehdä ilman valtuuksia. Kaikkia painikkeita ei myöskään välttämättä ole näkyvissä, jos käyttäjä ei ole kirjautunut   sovellukseen tai hänellä ei ole pääkäyttäjän oikeuksia.



## Linkkejä

[Heroku](https://enigmatic-lake-26343.herokuapp.com/)

[Tietokantakaavio ja CREATE TABLE -lauseet](https://github.com/guotin/tietokantasovellus/blob/master/documentation/database_documentation.md)

[Käyttäjätarinat ja SQL-kyselyt](https://github.com/guotin/tietokantasovellus/blob/master/documentation/user_stories.md) (englanniksi)

[Loppudokumentti](https://github.com/guotin/tietokantasovellus/blob/master/documentation/conclusion.md)
