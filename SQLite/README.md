# **Exemplo de uso do Python com o SQLite**

- Para ter acesso ao banco via linux, recomento o "DB Browser for SQLite"

- Comando sql para criação da tabela:
CREATE TABLE 'notas' ('id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 'nome' TEXT, 'nota' INTEGER)

- Comando sql para criação da tabela caso ela não exista:
CREATE TABLE IF NOT EXISTS 'notas' ('id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 'nome' TEXT, 'nota' INTEGER)
