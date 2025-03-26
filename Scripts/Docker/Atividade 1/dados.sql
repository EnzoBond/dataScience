create table turma(id id_turma primary key,
    capacidade int,
    ano int not null,
    sigla varchar(3) not null unique
);

create table sala(id id_sala primary key,
    cod_sala int not null unique,
    capacidade (50) not null
);

create table predio(id id_pred primary key,
    cod_pred int not null unique,
    endereco varchar(124)
);

create table disciplina(id id_disci primary key,
    nome varchar(25),
    cod_disci int not null unique
);

create table curriculo(id id_curri primary key,
  cod_curri int,
  graduacao varchar(264),
  faculdade varchar(264),
  ano_graduacao date
);

create table curso(id id_curso primary key,
    cod_curso int unique,
    nome_curso varchar(10)
);

alter table sala add column id_predio int, add constraint fk_sala_predio foreign key (id_predio) references predio(id_predio)
alter table turma add column id_sala int, add constraint fk_turma_sala foreign key (id_sala) references sala(id_sala)
alter table disciplina add column id_turma varchar, add constraint fk_disciplina_turma foreign key (id_turma) references turma(id_turma)
alter table curriculo add column id_disci int, add constraint fk_curriculo_disciplina foreign key (id_disci) references disciplina(id_disci)
alter table curso add column id_curri int, add constraint fk_curriculo_curso foreign key (id_curri) references curriculo(id_curriqq)
