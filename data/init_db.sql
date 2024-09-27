DROP SCHEMA IF EXISTS StreamSmart CASCADE;
CREATE SCHEMA StreamSmart;

--------------------------------------------------------------
-- Table User
--------------------------------------------------------------

DROP TABLE IF EXISTS StreamSmart.user CASCADE ;
CREATE TABLE StreamSmart.user (
    id_user serial PRIMARY KEY,
    name text,
    password text
);

--------------------------------------------------------------
-- Table Watchlist
--------------------------------------------------------------

DROP TABLE IF EXISTS StreamSmart.watchlist CASCADE ;
CREATE TABLE StreamSmart.watchlist (
    id_watchlist serial PRIMARY KEY,
    id_user FOREIGN KEY REFERENCES StreamSmart.user(id_user),
    name text,
);

