-- create databases
CREATE DATABASE IF NOT EXISTS `db_production`;


-- create root user and grant rights
CREATE USER IF NOT EXISTS 'root'@'%' IDENTIFIED BY 'admin';
GRANT ALL ON *.* TO 'root'@'%';