-- CREATE DATABASE quanta; 

CREATE TABLE results(

    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    category VARCHAR(100),
    author VARCHAR(255),
    published_date DATE,
    url  VARCHAR(512)

);

CREATE TABLE bookmarked_results(

    id SERIAL PRIMARY KEY,
    time_bookmarked TIMESTAMP,
    result INTEGER REFERENCES results(id)

);

