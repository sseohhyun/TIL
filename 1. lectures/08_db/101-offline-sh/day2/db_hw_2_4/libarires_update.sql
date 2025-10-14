USE libraries;

UPDATE 
  books
SET 
  price = 12.99,
  genre = 'Science Fiction',
  publisher = "'Charles Scribner's Sons" 
WHERE
  isbn = '9780451524935';

SELECT * FROM books;