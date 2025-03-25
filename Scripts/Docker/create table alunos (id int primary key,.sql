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

create table professores(id int primary key,
    nome varchar(255),
    cpf varchar(11),
    formacao varchar(255),
    data_inicio date
);


CREATE TABLE turmas(id serial primary key,
    cod_turma VARCHAR(10),
    data_inicio date,
    data_fim date,
);


-- Versão 2
ALTER TABLE cursos
    drop column cod_turma,
    drop COLUMN data_inicio,
    drop COLUMN data_fim;

Alter table
  cursos drop column cod_turma,
  drop column data_inicio,
  drop column data_fim;

-- Versão 3:
create table componentes(
  id serial primary key,
  ementa text,
  data_inicio date not null,
  data_fim date
);

alter table cursos drop column componentes;


create table enderecos(
  id serial primary key,
  logradouro varchar(255) not null,
  rua varchar(255) not null,
  numero varchar(10) not null,
  complemento varchar(255),
  bairro varchar(255) not null,
  cidade varchar(255) not null,
  estado varchar(2) not null,
  cep varchar(8) not null,
  tipo varchar(10) not null
);

--Versão 5
Alter table turmas add column id_curso integer not null,
  add constraint fk_turmas_cursos foreign key (id_curso) references cursos(id),
  add column id_aluno integer not null,
  add constraint fk_turmas_alunos foreign key (id_aluno) references alunos(id);


alter table componentes add column id_curso not null,
   add constraint fk_componentes_cursos foreign key (id_curso) references cursos(id);
   add column id_prof integer not null,
   add constraint fk_componentesq_prof foreign key (id_prof) references professores(id);