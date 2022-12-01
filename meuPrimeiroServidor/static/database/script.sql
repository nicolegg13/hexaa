PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

CREATE TABLE jogadores(
    id_jogador INTEGER NOT NULL,
    valor TEXT NOT NULL,
    nome TEXT NOT NULL,
    PRIMARY KEY(id_jogador)
);

INSERT INTO jogadores(id_jogador, valor, nome) VALUES (1, 'richarlison', 'richarlison');
INSERT INTO jogadores(id_jogador, valor, nome) VALUES (2, 'vinicius_jr', 'vinicius jr');
INSERT INTO jogadores(id_jogador, valor, nome) VALUES (3, 'daniel_alves', 'daniel alves');

