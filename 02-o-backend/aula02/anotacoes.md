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

## Alguns tipos de SQL

Aqui você encontra apenas uma amostra dos muitos tipos de dados que SQL suporta.

A lista exata de tipos difere de um banco de dados para outro. Para obter uma lista completa de tipos, consulte o manual do banco de dados.

### Tipos de strings e texto
- text — uma string de qualquer comprimento, como os tipos str ou unicode em Python.
- char(n) — uma string de exatamente n caracteres.
- varchar(n) — uma string de até n caracteres.

### Tipos numéricos
- integer — um valor de número inteiro, como int do Python.
- real — um valor de ponto flutuante, como float do Python. Com precisão de até seis casas decimais.
- double precision — um valor de ponto flutuante de precisão mais alta. Com precisão de até 15 casas decimais.
- decimal — um valor decimal exato.

### Tipos de data e hora
- date — uma data do calendário; incluindo dia, mês e ano.
- time — um momento exato do dia.
- timestamp — data e hora juntos.

### Select Where.

Aqui estamos selecionando todos os nomes dos animais que não são iguais a `gorilla` e `Max`.

```
select name from animals where species !='gorilla' and name !='Max';

+-------------+
|        name |
+=============+
|      Andrea |
|       Bruno |
|     Charlie |
|       Della |
|        Emma |
|        Fred |
|      George |
|       Molly |
|     Eliezer |
|    Giuseppe |
|        Taro |
|        Fido |
|        Spot |
|       Rover |
|      Medusa |
| Zarathustra |
|    Zebediah |
|   Zephaniah |
|     Zenobia |
|        Zara |
|    Cherries |
|        Biff |
|  Tinkerbell |
|      George |
|      Cheech |
|        Spot |
|      Andrea |
|       Devoe |
|       Duran |
|      Jethro |
|     Tiffany |
|         Sue |
|      Alison |
|         Ben |
|    Cordelia |
|         Eli |
|        John |
|       Glenn |
|         Meg |
|         Mel |
|    Veronica |
|       Ricky |
|     Charlie |
|        Lucy |
|       Patty |
|   Woodstock |
|     Francis |
|       Bacon |
|        Raja |
|        Ratu |
|      Putera |
|       Gajah |
|       Singa |
|     Kambing |
|       Chris |
|       Sandy |
|         Pat |
|        Mary |
|      Martha |
|        John |
|         Mal |
|         Zoe |
|       River |
|       Inara |
|       Simon |
|      Morgan |
|      Laylah |
|    Bertrand |
|     Hypatia |
|        Emmy |
|        Jack |
|         Mac |
|       Slack |
|         Pac |
|       Track |
|       Owuru |
|     Ekwensu |
|       Imaha |
|      Adiaha |
|     Obi Ike |
+-------------+

```

## Operadores e comparações

Selecionando todas as colunas de animais que sejam da espécie lhama e que tenham
nascido entre 01/01/1995 e até 31/12/1998

```
select * from animals where species = 'llama' and (birthdate >= '1995-01-01') and (birthdate <= '1998-12-31')
```

## Declarações 

### Select
A forma mais básica de declaração select é a seleção de um só valor escalar:

```
select 2 + 2 ;
```
Também podemos selecionar uma ou mais colunas de uma tabela, o que é mais útil. 
Sem restrições, isso retornará todas as linhas da tabela:
```
select name, species from animals ;
```

As colunas são separadas por vírgulas, use * para selecionar todas as colunas das tabelas:
```
select * from animals;
```

Muito frequentemente, não queremos todos os dados de uma tabela. Podemos restringir as linhas usando diversas cláusulas de seleção, listadas abaixo. Há, também, diversas funções que podem ser aplicadas a colunas, incluindo funções de agregação que operam nos valores de diversas linhas, como max e count.

### `where`

A cláusula where expressa restrições — filtrando uma tabela por linhas que seguem uma regra em particular. where dá suporte a igualdades, desigualdades e operadores booleanos (dentre outras coisas):
- where species = 'gorilla' — retorna apenas linhas que têm 'gorilla' como o valor da coluna species.
- where name >= 'George' — retorna apenas linhas cujo valor da coluna nomes vem alfabeticamente depois de 'George'.
- where species != 'gorilla' and name != 'George' — retorna apenas linhas onde a espécie não é 'gorilla' e o nome não é 'George'.

### `limit / offset`

A cláusula `limit` define uma quantidade máxima de linhas que devem constar na tabela de resultados. 

A cláusula opcional `offset` diz quantas linhas devem ser ignoradas antes do primeiro resultado. Assim, `limit 10 offset 100` retornará 10 resultados começando com o 101°.

### `order by`

A cláusula `order by` informa ao banco de dados como classificar os resultados — geralmente de acordo com uma ou mais colunas. Então `order by species, name` diz para classificar os resultados primeiro pela coluna de espécies, e então por nome dentro de cada espécie.


A ordenação acontece antes do `limite/offset`, então você pode usá-los juntos para extrair páginas de resultados em ordem alfabética (pense nas páginas de um dicionário).

O modificador opcional `desc` diz ao banco de dados para ordenar os resultados em ordem descendente — como de números grandes a pequenos, ou de Z a A.

### `group by`

A cláusula `group by` só é usada com agregações, como `max` ou `sum`. Sem uma cláusula `group by`, uma declaração select com uma agregação vai agregar todas as linhas selecionadas, retornando apenas uma linha. Com a cláusula `group by`, ela retornará uma linha para cada valor distinto da coluna ou expressão na cláusula `group by`.

Selecionando espécies apartir da tabelas animais, fazendo agrupamento por espécies e ordenando de forma decrescente.

```
select count(*) as num, species from animals group by species order by num desc

+-----+------------+
| num |    species |
+=====+============+
|   9 |    gorilla |
|   9 |      llama |
|   6 |  orangutan |
|   5 |     alpaca |
|   5 |     ferret |
|   5 |     jackal |
|   5 |   sea lion |
|   5 |        yak |
|   5 |      zebra |
|   4 |     iguana |
|   4 |      moose |
|   3 | brown bear |
|   3 |      camel |
|   3 |      dingo |
|   3 |      hyena |
|   3 |   platypus |
|   3 |    raccoon |
|   3 |    warthog |
|   2 |    narwhal |
|   2 |    unicorn |
|   1 |    echidna |
|   1 |   mongoose |
+-----+------------+
```

### Having
A cláusula `having` funciona como a cláusula `where`, mas é aplicada depois que as 
agregações `group by` acontecem. Segue um exemplo:

```
select col1, sum(col2) as total
    from table
    group by col1
    having total > 500 ;
```

Geralmente, pelo menos uma das colunas será uma função agregada, como count, max ou sum, em uma das colunas das tabelas. A fim de aplicar having a uma coluna agregada, você dará um nome a ela, usando `as`.

Por exemplo, se você tiver uma tabela com os itens vendidos em uma loja e quiser saber quais itens tiveram mais de cinco unidades vendidas, pode usar:

```
select name, count(*) as num from sales having num > 5;
```

Você pode ter uma declaração select que usa somente where, ou somente group by, ou group by e having, ou where e group by, ou todas as três! Porém, geralmente, não faz sentido se usado sem group by.

Se você usar tanto `where` como `having`, a condição `where` filtrará as linhas que estão entrando na agregação, e a condição having filtrará as linhas que estão saindo dela.


### Join
Para jutar uma tabela a outra usamos o operador `join` e passamos as tabelas. E apartir do operador
`on` passamos as regras dessa junção

```
select * foo join bar on baz
```


Abaixo, estamos juntando as tabelas animais e espécies selecionando apenas as espécies que comem peixe

```
select * from animals, diet where animals.species = diet.species and diet.food = 'fish'

+---------+------------+------------+------------+------+
|    name |    species |  birthdate |    species | food |
+=========+============+============+============+======+
|    Fred | brown bear | 1993-05-02 | brown bear | fish |
|  George | brown bear | 1997-06-24 | brown bear | fish |
|   Molly | brown bear | 1981-10-17 | brown bear | fish |
|   Bacon |    narwhal | 1975-02-07 |    narwhal | fish |
| Francis |    narwhal | 1996-04-27 |    narwhal | fish |
|   Inara |   sea lion | 2001-08-18 |   sea lion | fish |
|     Mal |   sea lion | 1987-04-29 |   sea lion | fish |
|   River |   sea lion | 2004-07-08 |   sea lion | fish |
|   Simon |   sea lion | 2000-12-16 |   sea lion | fish |
|     Zoe |   sea lion | 1991-05-19 |   sea lion | fish |
+---------+------------+------------+------------+------+
```

## Inserção
Para inserimos um valor na tabela, basta utilizar a seguinte sintaxe e respeitar
a ordem dos argumentos segundo a ordem das colunas.

```
insert into tablename ( col1, col2, ... ) values ( val1, val2, ... );
```

Se os valores estão na mesma ordem que as colunas da tabela (começando pela primeira coluna), você não precisa especificar as colunas na declaração insert:

```
insert into tablename values ( val1, val2, ... );
```

Por exemplo, se uma tabela possui três colunas (a, b, c) e você deseja inserir em a e b, pode deixar de fora os nomes das colunas da declaração insert. Mas se você quiser inserir em b e c,ou a e c, você tem de especificar as colunas.

Normalmente, uma única declaração insert pode inserir algo somente em uma tabela (diferentemente da declaração select, que pode retirar dados de várias tabelas usando uma join).

## Algumas querys

Selecionando todos os animais onde as espécies tem que possuir o valor de gorila e 
são ordenadas pela data de nascimento
```
select * from animals where species = 'gorilla' order by birthdate limit 10;
```

Selecionando todos os animais colocando em ordem de nome e paginando de  10 em 10
```
select * from animals order by name limit 10 offset 0;
```

Selecionando todas as espécies e realizando a contagem transformando em um outro
agrupamento ordenado em ordem decrescente.
```
select species, count(*) as total from animals group by species order by total desc;
```
