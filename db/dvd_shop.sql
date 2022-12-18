DROP TABLE films;
DROP TABLE directors;
DROP TABLE distributors;


CREATE TABLE directors (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE distributors (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE films (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  director_id INT REFERENCES directors(id) ON DELETE CASCADE,
  distributor_id INT REFERENCES distributors(id) ON DELETE CASCADE,
  stock_quantity INT,
  buying_price INT,
  selling_price INT,
  profit INT
);