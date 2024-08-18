DROP DATABASE chatapp;

CREATE DATABASE chatapp;
USE chatapp;

CREATE TABLE users (
    id varchar(255) PRIMARY KEY,
    firstname varchar(255) NOT NULL,
    lastname varchar(255) NOT NULL,
    email varchar(255) UNIQUE NOT NULL,
    password varchar(255) NOT NULL
);

-- groupsはMySQLの予約語のためカラムに使用できず、channelsに変更すると作成できた。
CREATE TABLE channels (
    id serial PRIMARY KEY,
    name varchar(255) NOT NULL
);


CREATE TABLE messeages (
    id serial PRIMARY KEY,
    messeage text,
    uid varchar(255) REFERENCES users(id),
    cid integer REFERENCES channels(id) ON DELETE CASCADE,
    created_at timestamp not null default current_timestamp
);

