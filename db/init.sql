CREATE USER myuser WITH PASSWORD 'correctpassword';
CREATE DATABASE mydatabase;
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;

CREATE TABLE notes (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);