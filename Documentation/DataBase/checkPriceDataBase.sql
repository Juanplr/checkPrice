CREATE DATABASE checkPrice;

Use checkPrice;

CREATE TABLE usuario (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30),
    user_name VARCHAR(20) UNIQUE NOT NULL,
    correo VARCHAR(40) UNIQUE,
    contrasena VARCHAR(50) NOT NULL,
    es_administrador BOOLEAN
);

CREATE TABLE producto (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    codigo_de_barras VARCHAR(20) UNIQUE NOT NULL,
    precio REAL NOT NULL,
    id_usuario INTEGER,
    id_categoria INTEGER,
    FOREIGN KEY (id_usuario) REFERENCES usuario (id),
    FOREIGN KEY (id_categoria) REFERENCES categoria (id)
);

CREATE TABLE categoria (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20)
);

INSERT INTO
    categoria (nombre)
VALUES ("Panaderia"),
    ("Higiene"),
    ("Belleza y Salud"),
    ("Bebidas"),
    ("Basicos");