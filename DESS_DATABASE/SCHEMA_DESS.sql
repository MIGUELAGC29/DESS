CREATE DATABASE ENCUESTAS_DESS;
USE ENCUESTAS_DESS;

CREATE TABLE UNIDAD_ACADEMICA(
ID_UA INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
NOMBRE VARCHAR(500),
SIGLAS VARCHAR(200));

CREATE TABLE PROGRAMA_ACADEMICO(
ID_PA INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
NOMBRE VARCHAR(600),
ID_UA INTEGER UNSIGNED NOT NULL,
FOREIGN KEY (ID_UA) REFERENCES UNIDAD_ACADEMICA(ID_UA));

CREATE TABLE USUARIO(
ID_USUARIO INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
NOMBRE VARCHAR(50) NOT NULL,
APELLIDO1 VARCHAR(50) NOT NULL,
APELLIDO2 VARCHAR(50) NOT NULL,
CURP VARCHAR(50) NOT NULL,
SEXO VARCHAR(30),
EDAD INTEGER UNSIGNED NOT NULL,
ESTADO_CIVIL VARCHAR(50) NOT NULL,
EMAIL VARCHAR(100) NOT NULL,
TELEFONO VARCHAR(50) NOT NULL,
PAIS VARCHAR(200) NOT NULL,
CODIGO_POSTAL VARCHAR(10) NOT NULL,
ENTIDAD_FEDERATIVA VARCHAR(200) NOT NULL, 
ALCALDIA_MUNICIPIO VARCHAR(200) NOT NULL, 
ID_UA INTEGER UNSIGNED NOT NULL, 
ID_PA INTEGER UNSIGNED NOT NULL,
FOREIGN KEY (ID_UA) REFERENCES UNIDAD_ACADEMICA(ID_UA),
FOREIGN KEY (ID_PA) REFERENCES PROGRAMA_ACADEMICO(ID_PA));

CREATE TABLE CUESTIONARIO(
ID_CUESTIONARIO INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
NOMBRE VARCHAR(200) NOT NULL,
DESCRIPCION VARCHAR(500) NOT NULL);

