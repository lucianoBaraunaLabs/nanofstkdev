# Aula 02 - Falando com banco de dados.

Para trazermos algum resultado do banco de dados nós precisamos realizar uma consulta (query).

Para comentarmos em SQL utilizamos `--`.
```
-- Isso é um comentário em sql
```

No exemplo abaixo estamos selecionando as colunas `name`, `birthdate` da tabela
`animals` que tenham `gorilla` como espécie

```
select name, birthdate from animals where species = 'gorilla';

-- Resultado é :
+---------+------------+
|    name |  birthdate |
+=========+============+
|     Max | 2001-04-23 |
|    Dave | 1988-09-29 |
|   Becky | 1979-07-04 |
|     Liz | 1998-06-12 |
|  George | 2011-01-09 |
|  George | 1998-05-18 |
| Wendell | 1982-09-24 |
|   Bjorn | 2000-03-07 |
| Kristen | 1990-04-25 |
+---------+------------+
```

Agora utilizando `*` nós conseguimos pegar todos os valores. No caso abaixo estamos
pegando todos as colunas que tenham como espécie `iguana`.

```
select * from animals where species = 'iguana';

-- Resultado é: 
+--------+--------+------------+
|   name | species |  birthdate |
+========+========+============+
| George | iguana | 2013-10-18 |
| Cheech | iguana | 2006-12-19 |
|   Spot | iguana | 2010-07-23 |
| Andrea | iguana | 1999-09-09 |
+--------+--------+------------+
```