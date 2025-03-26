create table alunos(nome varchar(64) not null,
                    cpf varchar(11) not null unique,
                    data_nascimento date not null,
                    data_matricula date not null,
                    matricula varchar(10) not null unique,
                    endereco varchar(128));

create table cursos(nome varchar(64) not null,
                    cod_turma varchar(10) not null unique,
                    data_inicio date not null,
                    data_fim date,
                    componentes varchar(128));

create table professores(
    nome varchar(64) not null,
    cpf varchar(11) not null unique,
    formacao varchar(64) not null,
    data_inicio date not null
);