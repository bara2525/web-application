
DROP TABLE IF EXISTS kategorie;
DROP TABLE IF EXISTS role;
DROP TABLE IF EXISTS uživatel;
DROP TABLE IF EXISTS historie_ceny;
DROP TABLE IF EXISTS produkt;

CREATE TABLE kategorie (
                             id_kategorie INTEGER PRIMARY KEY AUTOINCREMENT,
                             název TEXT UNIQUE NOT NULL,
                             popis TEXT NOT NULL,
                             id_uživatele INTEGER,
                             FOREIGN KEY (id_uživatele) REFERENCES uživatel(id_uživatele)
);

CREATE TABLE role (
                        id_role INTEGER PRIMARY KEY AUTOINCREMENT,
                        název TEXT NOT NULL
);

CREATE TABLE uživatel (
                            id_uživatele INTEGER PRIMARY KEY AUTOINCREMENT,
                            jméno TEXT NOT NULL,
                            příjmení TEXT NOT NULL,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL,
                            id_role INTEGER,
                            FOREIGN KEY (id_role) REFERENCES role(id_role)
);

CREATE TABLE produkt (
                         id_produktu INTEGER PRIMARY KEY AUTOINCREMENT,
                         název TEXT NOT NULL,
                         výrobce TEXT NOT NULL,
                         id_kategorie INTEGER,
                         FOREIGN KEY (id_kategorie) REFERENCES kategorie(id_kategorie)
);

CREATE TABLE historie_ceny (
                                 id_ceny INTEGER PRIMARY KEY AUTOINCREMENT,
                                 odkdy TEXT,
                                 dokdy TEXT,
                                 cena INTEGER ,
                                 komentář TEXT NOT NULL,
                                 id_produktu INTEGER,
                                 FOREIGN KEY (id_produktu) REFERENCES produkt(id_produktu)
);


INSERT into role VALUES(1,'administrátor');
INSERT into role VALUES(2,'user');

INSERT into uživatel VALUES (1,'admin','webu','admin','heslo', 1);


INSERT INTO uživatel(id_uživatele,jméno,příjmení,username,password,id_role) VALUES (2,'Jirka','Nový','jirkan','password',2);
INSERT INTO uživatel(id_uživatele,jméno,příjmení,username,password,id_role) VALUES (3,'Bob','Cooper','bobc','password',2);
INSERT INTO uživatel(id_uživatele,jméno,příjmení,username,password,id_role) VALUES (4,'John','Watson','johnw','password',2);
INSERT INTO uživatel(id_uživatele,jméno,příjmení,username,password,id_role) VALUES (5,'Jim','Jones','jimjo','password',2);

INSERT INTO kategorie(id_kategorie, název, popis, id_uživatele) VALUES (0,'','',1);
INSERT INTO kategorie(id_kategorie, název, popis, id_uživatele) VALUES (1,'kategorie1','nalezeno na eshopu',3);
INSERT INTO kategorie(id_kategorie, název, popis, id_uživatele) VALUES (2,'kategorie2','obchod',2);
INSERT INTO kategorie(id_kategorie, název, popis, id_uživatele) VALUES (3,'kategorie3','nikde',5);
INSERT INTO kategorie(id_kategorie, název, popis, id_uživatele) VALUES (4,'kategorie4','nalezeno na ulici',3);

INSERT INTO produkt(id_produktu,název,výrobce,id_kategorie) VALUES (1,'bílé víno','billa',1);
INSERT INTO produkt(id_produktu,název,výrobce,id_kategorie) VALUES (2,'červené víno','lidl',2);
INSERT INTO produkt(id_produktu,název,výrobce,id_kategorie) VALUES (3,'rosé','billa',2);
INSERT INTO produkt(id_produktu,název,výrobce,id_kategorie) VALUES (4,'šumivé víno','albert',1);
INSERT INTO produkt(id_produktu,název,výrobce,id_kategorie) VALUES (5,'líkérové víno','tesco',3);
INSERT INTO produkt(id_produktu,název,výrobce,id_kategorie) VALUES (6,'šampaňské','penny',4);


INSERT INTO historie_ceny(id_ceny,odkdy,dokdy,cena,komentář,id_produktu) VALUES (1,'2000-11-30','2001-02-04',100,'zde nějaký komentář',3);
INSERT INTO historie_ceny(id_ceny,odkdy,dokdy,cena,komentář,id_produktu) VALUES (2,'1990-08-09','1991-10-11',155,'dobry rocnik',1);
INSERT INTO historie_ceny(id_ceny,odkdy,dokdy,cena,komentář,id_produktu) VALUES (3,'2002-11-01','2006-07-25',120,'moc drahé',3);
INSERT INTO historie_ceny(id_ceny,odkdy,dokdy,cena,komentář,id_produktu) VALUES (4,'2010-03-04','2011-12-20',300,'průměrná cena',5);
INSERT INTO historie_ceny(id_ceny,odkdy,dokdy,cena,komentář,id_produktu) VALUES (5, '1950-01-10','1987-02-08',200,'dobrá cena pro tento produkt',6);
