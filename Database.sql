
CREATE TABLE pessoas
(NOME varchar2(30) CONSTRAINT PK_NOME PRIMARY KEY,
RA number(9));

CREATE TABLE DADOS
(RA number(9) foreign key references pessoas,
IDADE number(3),
SEXO varchar2(1),
ALTURA number(3),
PESO number(3));

