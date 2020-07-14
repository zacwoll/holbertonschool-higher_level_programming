-- Write a script that creates the database hbtn_0d_usa and the table states
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS htbn_0d_usa.states (id INT UNIQUE AUTO_INCREMENT NOT NULLL PRIMARY KEY,
name VARCHAR(256) NOT NULL);
