create table turma(id serial primary key,
    capacidade int,
    ano int not null,
    sigla varchar(3) not null unique
);

create table sala(id serial primary key,
    cod_sala int not null unique,
    capacidade int not null
);

create table predio(id serial primary key,
    cod_pred int not null unique,
    endereco varchar(124)
);

create table disciplina(id serial primary key,
    nome varchar(25),
    cod_disci int not null unique
);

create table curriculo(id serial primary key,
  cod_curri int,
  opcional boolean,
  graduacao varchar(264),
  faculdade varchar(264),
  ano_graduacao date
);

create table curso(id serial primary key,
    cod_curso int unique,
    nome_curso varchar(10)
);

alter table turma
    add column id_sala int,
    add constraint fk_turma_sala foreign key (id_sala) references sala(id);

alter table sala
    add column id_pred int,
    add constraint fk_sala_predio foreign key (id_pred) references predio(id);

alter table disciplina
    add column id_turma int,
    add constraint fk_disciplina_turma foreign key (id_turma) references turma(id);

alter table curriculo
    add column id_disci int,
    add constraint fk_curriculo_disciplina foreign key (id_disci) references disciplina(id);

alter table curso
    add column id_curri int,
    add constraint fk_curriculo_curso foreign key (id_curri) references curriculo(id);
-- digite os códigos SQL aqui