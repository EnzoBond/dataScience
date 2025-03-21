create table alunos (id int primary key, 
nome varchar(255), 
cpf varchar(11), 
data_nascimento date, 
data_matricula date, 
endereco varchar(255));

create table cursos(id int primary key,
    nome varchar(255),
    cod_turma varchar(10),
    data_inicio date,
    data_fim date,
    componentes varchar(255)
);

create table professores(
    id int primary key,
    nome varchar(255),
    cpf varchar(11),
    formacao varchar(255),
    data_inicio date
);


CREATE TABLE turmas(
    cod_turma VARCHAR(10),
    data_inicio date,
    data_fim date,
);

ALTER TABLE cursos drop column cod_turma,
    drop COLUMN data_inicio,
    drop COLUMN data_fim;