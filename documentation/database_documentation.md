# Database documentation

## Database chart
<img src="https://github.com/guotin/tietokantasovellus/blob/master/documentation/database_chart.png">

## SQL commands

~~~~sql
CREATE TABLE book (
        id INTEGER NOT NULL,
        name VARCHAR(144) NOT NULL,
        author VARCHAR(144) NOT NULL,
        publication_year INTEGER NOT NULL,
        PRIMARY KEY (id)
)
~~~~

~~~~sql
CREATE TABLE account (
        id INTEGER NOT NULL,
        username VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        admin BOOLEAN NOT NULL,
        PRIMARY KEY (id),
        CHECK (admin IN (0, 1))
)
~~~~

~~~~sql
CREATE TABLE account_book (
        account_id INTEGER NOT NULL,
        book_id INTEGER NOT NULL,
        PRIMARY KEY (account_id, book_id),
        FOREIGN KEY(account_id) REFERENCES account (id),
        FOREIGN KEY(book_id) REFERENCES book (id)
)
~~~~

~~~~sql
CREATE TABLE review (
        id INTEGER NOT NULL,
        grade INTEGER NOT NULL,
        text VARCHAR(500) NOT NULL,
        book_id INTEGER NOT NULL,
        account_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(book_id) REFERENCES book (id),
        FOREIGN KEY(account_id) REFERENCES account (id)
)
~~~~
