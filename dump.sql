BEGIN TRANSACTION;
CREATE TABLE usuario (
	id INTEGER NOT NULL, 
	nome VARCHAR(150) NOT NULL, 
	cpf VARCHAR(14) NOT NULL, 
	email VARCHAR(150) NOT NULL, 
	senha VARCHAR(256) NOT NULL, 
	formacao VARCHAR(255) NOT NULL, 
	tipo VARCHAR(20) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (cpf), 
	UNIQUE (email)
);
INSERT INTO usuario VALUES(1,'Administrador','000.000.000-00','admin@exemplo.com','pbkdf2:sha256:260000$Uz3y3OgD3B1zN5QA$5d39916371bee40f0b612f057c198fd023fd2caab268d21f59182128eb7b6f33','Gestão','admin');
INSERT INTO usuario VALUES(2,'Felipe','12310321460','g@g.com','pbkdf2:sha256:260000$3Am54m03I6Eu7nc2$5cd67689bc3ac997ee25a620ad3ee7da37560e3bc278519f241361e04d988378','a','participante');
INSERT INTO usuario VALUES(3,'Felipe Cabral','12345678910','felipe@felipe.com','pbkdf2:sha256:260000$DgMO6m89pW7AJN9C$cfde30ffdbc1ba5b8ae89323e4923c0d165cdc598d0060e12197c4a56a4ddbe7','Químico','participante');
INSERT INTO usuario VALUES(4,'Raul','45678912310','raul@raul.com','pbkdf2:sha256:260000$MzjnjZvhheMPBGwR$cd4902311def980503e51d9b4ed543c1dbdbf10711b00f7da229681803fd3f30','a','participante');
INSERT INTO usuario VALUES(5,'Rayane','78912345610','r@r.com','pbkdf2:sha256:260000$4HYtYEKRa7T8qmpA$d42a7674dc4130a8a32a0bc40c54363ac48f4a0c8d2078f5b485bde0650c8c07','med','participante');
INSERT INTO usuario VALUES(6,'teste','45896325789','teste@teste.com','pbkdf2:sha256:260000$7LFfxe1qhkJwdnxR$b8391f3d193aa6762dee0c2c357d082c0fe6f2fb9c39ab96cdae520be0ab94d7','a','participante');
INSERT INTO usuario VALUES(7,'Cat','56947832145','cat@cat.com','pbkdf2:sha256:260000$ZKM74MRGqQYC0JIB$b1ebb89488d723416a041c5a137ba7e1f9899b78d259b6c969425a534f0df3b7','cat','participante');
INSERT INTO usuario VALUES(8,'Nete','96874512694','nete@nete.com','pbkdf2:sha256:260000$KQtWq8kauUPJ3Rcg$1dc5f528d88f65b5f7bee9d1cbbb44540c9e3fea62e862d33788b567da3c9573','Pedagoga','participante');
INSERT INTO usuario VALUES(9,'Klévia','6985478124','klevia@klevia.com','pbkdf2:sha256:260000$7DlcqCxYLQDyZ0fw$f0d1da1cb8717f436e3d6d78a21690ffabb0a9a3246b4f4022bf3859040c9fae','Médica','participante');
CREATE TABLE oficina (
	id INTEGER NOT NULL, 
	titulo VARCHAR(100) NOT NULL, 
	descricao TEXT NOT NULL, 
	ministrante VARCHAR(100) NOT NULL, 
	vagas INTEGER NOT NULL, 
	carga_horaria VARCHAR(10) NOT NULL, estado VARCHAR(2) DEFAULT 'XX' NOT NULL, cidade VARCHAR(100) DEFAULT 'Cidade Padrão' NOT NULL, qr_code VARCHAR(255), 
	PRIMARY KEY (id)
);
INSERT INTO oficina VALUES(1,'Foguetes','Nasa','Elon Musk',13,'20','XX','Cidade Padrão','qrcodes/checkin_1.png');
INSERT INTO oficina VALUES(2,'Oficina Lei Lucas','Enfermeiros','Drauzio Varella',0,'1','XX','Cidade Padrão','qrcodes/checkin_2.png');
INSERT INTO oficina VALUES(3,'Pedagogia ','Paulo Freire','Klevia Delmiro',9,'20','AL','Atalaia','qrcodes/checkin_3.png');
INSERT INTO oficina VALUES(4,'Laboratório Experimental','LEEO','Marília',5,'10','AL','Arapiraca','qrcodes/checkin_4.png');
INSERT INTO oficina VALUES(6,'Orgânica','Experimentos','Jadriane',5,'1','PA','Aurora do Pará','qrcodes/checkin_6.png');
INSERT INTO oficina VALUES(7,'Pedagogia do Amanhã','Práticas do Futuro ','Felipe Cabral',9,'20','MT','Apiacás','qrcodes/checkin_7.png');
INSERT INTO oficina VALUES(8,'Klevia','Delmiro','Edja',29,'20','AL','Atalaia','qrcodes/checkin_8.png');
INSERT INTO oficina VALUES(9,'Oficina de Criação de Sistemas','Aqui vamos aprender o maravilhoso mundo dos sistemas de integração em python','Felipe Cabral',15,'10','AL','Atalaia','static/qrcodes/checkin_9.png');
INSERT INTO oficina VALUES(10,'Oficina de Geração de QRCodes','Aprenda a gerar os melhores QRCodes do Mundo','Tonholo',10,'10','PR','Arapongas','qrcodes/checkin_10.png');
INSERT INTO oficina VALUES(11,'Oficina de Práticas na Educação Física','Educadores de Física com Alunos','Amaro',5,'5','AL','Atalaia','qrcodes/checkin_11.png');
INSERT INTO oficina VALUES(12,'Música - Saxofone','Maestro João','João Márcio',2,'2','PE','Arcoverde','qrcodes/checkin_12.png');
INSERT INTO oficina VALUES(13,'Palestra','Como realizar palestras','Leandro',12,'10','MG','Alagoa','qrcodes/checkin_13.png');
INSERT INTO oficina VALUES(14,'Finally','Teste','Felipe',1,'1','AL','Atalaia','qrcodes/checkin_14.png');
INSERT INTO oficina VALUES(15,'Oficina de Educação Financeira','Aula com Primo Pobre','Paulo Guedes',1,'1','AL','Barra de São Miguel','static/qrcodes/checkin_15.png');
INSERT INTO oficina VALUES(16,'Geografia com 3D','Aprendendo a usar o app Geo3D','George Lima',10,'5','CE','Aracati','qrcodes/checkin_16.png');
CREATE TABLE oficina_dia (
	id INTEGER NOT NULL, 
	oficina_id INTEGER NOT NULL, 
	data DATE NOT NULL, 
	horario_inicio VARCHAR(5) NOT NULL, 
	horario_fim VARCHAR(5) NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(oficina_id) REFERENCES oficina (id)
);
INSERT INTO oficina_dia VALUES(1,1,'2025-01-22','09:00','19:00');
INSERT INTO oficina_dia VALUES(2,1,'2025-01-23','09:00','19:00');
INSERT INTO oficina_dia VALUES(3,2,'2025-01-22','09:00','10:00');
INSERT INTO oficina_dia VALUES(4,3,'2025-02-09','09:00','19:00');
INSERT INTO oficina_dia VALUES(5,3,'2025-02-10','09:00','19:00');
INSERT INTO oficina_dia VALUES(6,4,'2026-01-09','09:00','19:00');
INSERT INTO oficina_dia VALUES(8,6,'2025-02-09','09:00','10:00');
INSERT INTO oficina_dia VALUES(9,7,'2025-09-09','09:00','19:00');
INSERT INTO oficina_dia VALUES(10,7,'2025-09-19','09:00','19:00');
INSERT INTO oficina_dia VALUES(11,8,'2025-01-24','09:00','19:00');
INSERT INTO oficina_dia VALUES(12,8,'2025-01-25','09:00','19:00');
INSERT INTO oficina_dia VALUES(13,9,'2025-01-25','08:00','18:00');
INSERT INTO oficina_dia VALUES(14,10,'2025-01-09','08:00','18:00');
INSERT INTO oficina_dia VALUES(15,11,'2025-02-05','09:00','14:00');
INSERT INTO oficina_dia VALUES(16,12,'2025-01-25','09:00','10:00');
INSERT INTO oficina_dia VALUES(17,13,'2025-01-25','10:00','16:00');
INSERT INTO oficina_dia VALUES(18,14,'2025-01-24','01:03','02:00');
INSERT INTO oficina_dia VALUES(19,15,'2025-01-25','09:00','10:00');
INSERT INTO oficina_dia VALUES(20,16,'2025-02-25','09:00','10:00');
CREATE TABLE inscricao (
	id INTEGER NOT NULL, 
	usuario_id INTEGER, 
	oficina_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(usuario_id) REFERENCES usuario (id), 
	FOREIGN KEY(oficina_id) REFERENCES oficina (id)
);
INSERT INTO inscricao VALUES(3,3,2);
INSERT INTO inscricao VALUES(4,2,1);
INSERT INTO inscricao VALUES(5,3,1);
INSERT INTO inscricao VALUES(6,4,1);
INSERT INTO inscricao VALUES(7,5,1);
INSERT INTO inscricao VALUES(8,7,1);
INSERT INTO inscricao VALUES(9,3,3);
INSERT INTO inscricao VALUES(10,8,1);
INSERT INTO inscricao VALUES(11,8,7);
INSERT INTO inscricao VALUES(12,9,1);
INSERT INTO inscricao VALUES(13,9,8);
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
INSERT INTO alembic_version VALUES('6c75026e1492');
CREATE TABLE checkin (
	id INTEGER NOT NULL, 
	usuario_id INTEGER NOT NULL, 
	oficina_id INTEGER NOT NULL, 
	data_hora TIMESTAMP, 
	palavra_chave VARCHAR(50) NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(usuario_id) REFERENCES usuario (id), 
	FOREIGN KEY(oficina_id) REFERENCES oficina (id)
);
COMMIT;
