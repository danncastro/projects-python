create database CONTROLE_DE_ESTOQUE;
use CONTROLE_DE_ESTOQUE;
create table cadastro_de_produtos(
    id int not null auto_increment primary key,
    produto varchar (100) not null,
    preco float not null,
    quantidade int not null
);