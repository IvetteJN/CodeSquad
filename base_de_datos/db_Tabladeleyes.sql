CREATE DATABASE Proyecto;
USE Proyecto;


CREATE TABLE leyes(
id_leyes INT PRIMARY KEY AUTO_INCREMENT,
nro_leyes INT NOT NULL,
fecha DATE NOT NULL ,
descripcion VARCHAR(1000) NOT NULL,
categoria VARCHAR(35) NOT NULL,
jurisdiccion VARCHAR(35) NOT NULL,
or_legislativo VARCHAR(200) NOT NULL,
palabra_clave VARCHAR(35) NOT NULL
);

select * from leyes;
