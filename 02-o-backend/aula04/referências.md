# Referência — Aprofundando-se em SQL
Esta é uma referência ao material abordado na aula "Aprofundando-se em SQL".

### A declaração create table
A sintaxe completa da declaração create table é bastante complexa. Leia a [documentação de create table de PostgreSQL](http://www.postgresql.org/docs/9.4/static/sql-createtable.html) para ver tudo. Aqui está a sintaxe do formulário que estamos vendo nesta aula:

```
create table table ( column type [restriction] , ... ) [rowrestriction] ;
```

Há muitas restrições que podem ser colocadas em uma coluna ou linha. primary key e references são apenas duas delas. Veja a seção "Examples" da documentação de create table documentation= para saber muito mais.

### Regras para tabelas normalizadas:
Em um banco de dados normalizado, as relações entre as tabelas estão de acordo com as relações que realmente estão entre os dados. Os exemplos aqui referem-se às tabelas das aulas 2 e 4.


1. Cada linha tem o mesmo número de colunas.
Na prática, o sistema de banco de dados não nos deixa literalmente ter diferentes números de colunas em diferentes linhas. Mas se temos colunas que são algumas vezes vazias (null) e algumas vezes não, ou se colocamos múltiplos valores em um único campo, estamos quebrando esta regra.

O exemplo para termos em mente é a tabela de dietas do banco de dados zoológico. Em vez de tentar colocar várias comidas para uma espécia em uma única linha daquela espécie, nós as separamos. Isto torna muito mais fácil fazer agregações e comparações.

2. Há uma única chave e tudo na linha diz algo a respeito da chave.
A chave pode ser uma coluna ou mais de uma. Talvez seja até a linha inteira, como na tabela diet. Mas não temos linhas duplicadas em uma tabela.

Mais importante que isso, se você estiver guardando fatores que não são únicos — como os nomes de pessoas — nós os distinguimos usando um identificados único, como um número serial. Isso garante que não combinemos as notas de duas pessoas ou suas multas de estacionamento só porque ambas possuem o mesmo nome.

3. Fatos que não se relacionam com a chave pertencem a diferentes tabelas.
O exemplo aqui foi a tabela items, que possui itens, suas respectivas localizações, e os endereços (ruas) de suas localizações. O endereço não é um fato sobre o item; é um fato sobre a localização. Mover isso para uma tabela separada salva espaço e reduz ambiguidade, e podemos sempre reconstituir a tabela original usando um a join.

4. Tabelas não devem implicar relações que não existem.
O exemplo aqui foi a tabela job_skills, onde uma única linha listava uma das habilidades de tecnologia de uma pessoa (como o 'Linux') e uma de suas habilidades em línguas (como 'french', francês). Isso fez parecer que conhecimento de Linux da pessoa era específico para o francês, ou vice-versa... quando esse não é o caso no mundo real. Normalizar isso envolvia separar as habilidades técnicas e habilidades de trabalho (job skills) em tabelas separadas.

### O tipo serial
Para obter mais detalhes sobre o type serial, dê uma olhada na última seção [desta página do manual PostgreSQL](https://www.postgresql.org/docs/9.4/datatype-numeric.html).

### Outras subqueries
Aqui estão algumas seções na documentação do PostgreSQL que discutem outras formas de subqueries, além das que foram discutidas nesta aula:

[Subqueries escalares](https://www.postgresql.org/docs/9.4/sql-expressions.html#SQL-SYNTAX-SCALAR-SUBQUERIES)
[Expressões de subqueries](https://www.postgresql.org/docs/9.4/functions-subquery.html)
[Cláusula FROM](https://www.postgresql.org/docs/9.4/sql-select.html#SQL-FROM)
z