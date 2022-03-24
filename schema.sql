CREATE USER 'vaticletest_user'@'localhost' IDENTIFIED BY 'password';
CREATE DATABASE vaticletest_db;
GRANT SELECT, INSERT, DELETE ON vaticletest_db.* TO 'vaticletest_user'@'localhost' IDENTIFIED BY 'password';
USE vaticletest_db;

CREATE TABLE v_stations (sid CHAR(16) PRIMARY KEY, sname VARCHAR(128), lati DOUBLE, longi DOUBLE );

CREATE TABLE v_lines (lid INTEGER PRIMARY KEY, lname VARCHAR(128) );

CREATE TABLE v_sline (lid INTEGER, pos INTEGER UNSIGNED, sid CHAR(16),
     FOREIGN KEY (lid) REFERENCES v_lines (lid),
     FOREIGN KEY (sid) REFERENCES v_stations (sid),
     PRIMARY KEY (lid, pos) );
