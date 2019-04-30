# User stories

| As a/an | I want to                                      | So that...                               | Current status  |
| ------- | ---------------------------------------------- | -----------------------------------------|-----------------|
| User    | Register and login to the site                 | I can give book reviews                  | DONE            |
| User    | Add a book to the public book list             | others or I can give it a review         | DONE            |
| User    | Add a book from the public list to my own list | I can give it a review                   | DONE            |
| User    | View my own book list                          | I can see which books I've read          | DONE            |
| User    | Give a specific book a review                  | other users can read my review           | DONE            |
| User    | View reviews for a book                        | I can see what others have liked         | DONE            |
| User    | View my own reviews                            | I can remember which books I've reviewed | DONE            |
| User    | Edit my own review                             | I can fix mistakes                       | DONE            |
| User    | Delete my own review                           | I can undo what I've done                | DONE            |
| User    | Edit the public book list data                 | I can fix mistakes in book data          | DONE            |
| User    | View user statistics                           | I know who to appreciate most            | DONE            |
| User    | View book statistics                           | I can decide which books to read         | DONE            |
| Admin   | Remove book reviews                            | I can remove offensive content           | DONE            |
| Admin   | Remove books from the server database          | I can remove offensive content           | DONE            |

# SQL-queries

### Register to site

~~~~sql
INSERT INTO Account (username, password, admin) VALUES (?, ?, '0');
~~~~

### Login

Check whether user exists with provided input:

~~~~sql
SELECT * FROM Account WHERE username = ? AND password = ?;
~~~~

### Add a book to public list

~~~~sql
INSERT INTO Book (name, author, publication_year) VALUES (?, ?, ?);
~~~~

Adding a book to public list also automatically marks it as read with:

~~~~sql
INSERT INTO Account_book (account_id, book_id) VALUES (?, ?);
~~~~

### Add a book from the public list to private list (mark as read)

~~~~sql
INSERT INTO Account_book (account_id, book_id) VALUES (?, ?);
~~~~

### View private book list

~~~~sql
SELECT * FROM book
  JOIN account_book ON account_book.book_id = book.id
  WHERE account_book.account_id = ?;
~~~~

### Give a book review

~~~~sql
INSERT INTO Review (grade, text, account_id, book_id) VALUES (?, ?, ?, ?);
~~~~

### View reviews for a book

~~~~sql
SELECT account.username as username, book.name as bookname, review.grade as grade, review.id, 
  review.text as reviewtext FROM review"
  JOIN account ON account.id = review.account_id"
  JOIN book ON book.id = review.book_id"
  WHERE book.id = ?;
~~~~
                    
### View own reviews

~~~~sql
SELECT book.name as bookname, review.id as id, review.grade as grade, review.text as reviewtext FROM review
  JOIN account ON account.id = review.account_id
  JOIN book ON book.id = review.book_id
  WHERE account.id = ?; 
~~~~

### Edit my own review

~~~~sql
UPDATE Review SET grade = ?, text = ? WHERE id = ?;
~~~~

### Delete review

~~~~sql
DELETE FROM Review WHERE id = ?;
~~~~

### Update book data

~~~~sql
UPDATE Book SET name = ?, author = ?, publication_year = ? WHERE id = ?;
~~~~

### View user statistics (Most active reviewers)

~~~~sql
SELECT Account.username, COUNT(Review.id) FROM Account
  JOIN Review ON Review.account_id = Account.id
  WHERE Review.account_id = Account.id
  GROUP BY Account.username
  ORDER BY COUNT(Review.id) DESC
  LIMIT 5;
~~~~

### View book statistics

#### Most read books


~~~~sql
SELECT DISTINCT book.name, book.author, book.publication_year,
  (SELECT COUNT(id) FROM account JOIN account_book ON account_book.account_id = account.id WHERE account_book.book_id = book.id)
  AS times_read FROM book
  WHERE (SELECT COUNT(id) FROM account JOIN account_book ON account_book.account_id = account.id 
  WHERE account_book.book_id = book.id) > 0"
  ORDER BY times_read DESC
  LIMIT 5;
~~~~

#### Best graded books

~~~~sql
SELECT DISTINCT book.name, book.author, book.publication_year,
  (SELECT SUM(review.grade) FROM review WHERE review.book_id = book.id) AS grade_sum,
  (SELECT COUNT(review.id) FROM review WHERE review.book_id = book.id) AS grade_count,
  (SELECT SUM(review.grade) / COUNT(review.id) FROM review WHERE review.book_id = book.id) AS grade_order
  FROM book
  WHERE (SELECT COUNT(review.id) FROM review WHERE review.book_id = book.id) > 0
  ORDER BY grade_order DESC
  LIMIT 5;
~~~~
