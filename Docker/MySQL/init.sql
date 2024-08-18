DROP DATABASE IF EXISTS chatapp;
CREATE DATABASE chatapp;
USE chatapp;

CREATE TABLE users (
    id varchar(255) PRIMARY KEY,
    firstname varchar(255) NOT NULL,
    lastname varchar(255) NOT NULL,
    email varchar(255) UNIQUE NOT NULL,
    password varchar(255) NOT NULL
);

CREATE TABLE channels (
    id int AUTO_INCREMENT PRIMARY KEY,
    name varchar(255) NOT NULL
);

CREATE TABLE messages (
    id int AUTO_INCREMENT PRIMARY KEY,
    message text,
    uid varchar(255),
    cid int,
    created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (uid) REFERENCES users(id),
    FOREIGN KEY (cid) REFERENCES channels(id) ON DELETE CASCADE
);