CREATE TYPE stav_objednavky AS ENUM ('nova','zpracovana','stornovana');
CREATE TYPE typ_produktu AS ENUM ('standard','premium','lux');


CREATE TABLE zakaznik (
    id SERIAL PRIMARY KEY,
    jmeno VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    verifikovany BOOLEAN DEFAULT FALSE,
    kredit FLOAT DEFAULT 0
);


CREATE TABLE produkt (
    id SERIAL PRIMARY KEY,
    nazev VARCHAR(100) NOT NULL,
    cena FLOAT NOT NULL,
    typ typ_produktu NOT NULL
);

CREATE TABLE objednavka (
    id SERIAL PRIMARY KEY,
    zakaznik_id INT NOT NULL REFERENCES zakaznik(id) ON DELETE CASCADE,
    datum TIMESTAMP DEFAULT NOW(),
    stav stav_objednavky DEFAULT 'nova'
);

CREATE TABLE polozka (
    id SERIAL PRIMARY KEY,
    objednavka_id INT NOT NULL REFERENCES objednavka(id) ON DELETE CASCADE,
    produkt_id INT NOT NULL REFERENCES produkt(id) ON DELETE CASCADE,
    mnozstvi INT NOT NULL CHECK (mnozstvi > 0)
);


CREATE TABLE sklad (
    produkt_id INT PRIMARY KEY REFERENCES produkt(id) ON DELETE CASCADE,
    mnozstvi INT NOT NULL CHECK (mnozstvi >= 0)
);


CREATE VIEW view_objednavky_detail AS
SELECT o.id AS objednavka_id,
       z.jmeno || ' ' || z.email AS zakaznik,
       o.datum,
       o.stav,
       p.nazev AS produkt,
       pol.mnozstvi,
       p.cena,
       (pol.mnozstvi * p.cena) AS cena_celkem
FROM objednavka o
JOIN zakaznik z ON o.zakaznik_id = z.id
JOIN polozka pol ON pol.objednavka_id = o.id
JOIN produkt p ON pol.produkt_id = p.id;


CREATE VIEW view_produkty_sklad AS
SELECT p.nazev, p.typ, s.mnozstvi
FROM produkt p
JOIN sklad s ON s.produkt_id = p.id;


INSERT INTO zakaznik (jmeno, email, verifikovany, kredit) VALUES
('Jan Novak','jan.novak@email.cz', TRUE, 1000),
('Eva Malá','eva.mala@email.cz', FALSE, 500),
('Petr Svoboda','petr.svoboda@email.cz', TRUE, 750);

INSERT INTO produkt (nazev, cena, typ) VALUES
('Notebook', 20000, 'premium'),
('Mys', 500, 'standard'),
('Monitor', 5000, 'standard'),
('Klavesnice', 1200, 'standard'),
('Sluchatka', 1500, 'lux');

INSERT INTO sklad (produkt_id, mnozstvi) VALUES
(1, 10),
(2, 50),
(3, 20),
(4, 30),
(5, 15);


INSERT INTO objednavka (zakaznik_id, stav) VALUES (1, 'nova');

INSERT INTO polozka (objednavka_id, produkt_id, mnozstvi) VALUES
(1, 1, 1),
(1, 2, 2);
