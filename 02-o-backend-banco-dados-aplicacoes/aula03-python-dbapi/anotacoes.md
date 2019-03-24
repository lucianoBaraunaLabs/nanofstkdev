# Pyton DB-API

Para uma referência completa para a Python DB-API, veja a [a especificação](https://www.python.org/dev/peps/pep-0249/) e a documentação para módulos específicos de bancos de dados,[sqlite3](https://docs.python.org/2/library/sqlite3.html) e [psycopg2](http://initd.org/psycopg/docs/).

### module.connect(...)
Conecte a um banco de dados. O argumento para connect é diferente de módulo para módulo; veja  a documentação para detalhes. connect retorna um objeto Connection ou levanta uma exceção.

Para os métodos abaixo, perceba que você não chama literalmente (por exemplo) `Connection.cursor()` em seu código. Você faz um objeto `Connection`, salva-o em uma variável (talvez chamada db) e, então, chama `db.cursor()`.


### Connection.cursor()
Faz um objeto `Cursor` a partir de uma conexão. Cursores são usados para enviar declarações SQL ao banco de dados e busca resultados.


### Connection.commit()
Comete mudanças feitas na atual conexão. Você deve chamar `commit` antes de fechar a conexão se quiser que mudanças (como inserts, atualizações ou deleções) sejam salvas. Mudanças não cometidas serão visíveis a partir de sua conexão atual, mas não das outras.

### Connection.rollback()
Retorna (desfaz) mudanças feitas na conexão atual. Você deve retornar se obter uma exceção se quiser continuar usando a mesma conexão.

### Connection.close()
Fecha a conexão. Conexões são sempre fechadas implicitamente quando seu programa fecha, mas é uma boa ideia fechá-las manualmente, especialmente se seu código possa ser executado em loop.

### Cursor.execute(statement), Cursor.execute(statement, tuple)
Executa uma declaração SQL no banco de dados. Se você quiser substituir variáveis na declaração SQL, use o segundo formulário — veja a [documentação](http://initd.org/psycopg/docs/usage.html#query-parameters) para detalhes.

Se sua declaração não faz sentido (por exemplo, se pede por uma coluna que não está ali) ou pede que o banco de dados faça algo que não pode fazer (como remover uma linha de uma tabela que é referenciada por outras linhas de outras tabelas), você terá uma exceção.

## Referência rápida - psql
A ferramenta de linha de comando psql é realmente poderosa. Há uma referência completa a ela na [documentação do PostgreSQL](http://www.postgresql.org/docs/9.4/static/app-psql.html).

Para conectar psql a um banco de dados rodando na mesma máquina (como sua VM), tudo o que você precisa fornecer é o nome do banco de dados. Por exemplo, o comando psql forum irá conectar ao banco de dados forum.

De dentro do psql, você pode executar qualquer declaração SQL usando tabelas no banco de dados conectado. Certifique-se de terminar declarações SQL com um ponto e vírgula, o que não é sempre necessário em Python.

Você também pode usar um número de comandos especiais psql para obter informações sobre o banco de dados e fazer modificações na configuração. O comando `\d` posts mostrado no vídeo é um exemplo — isso exibe as colunas da tabela posts.

Outras coisas que você pode fazer:

- `\dt` — lista todas as tabelas no banco de dados.

- `\dt+` — lista tabelas e informação adicional (notavelmente, o quão grande cada tabela é no disco).

- `\H` — alterna entre imprimir tabelas e texto simples vs. HTML.

### Documentação para Bleach
Leia a documentação para Bleach aqui: http://bleach.readthedocs.org/en/latest/


### Declarações uptade e delete
A sintaxe das declarações update e delete:

`update table set column = value where restriction ;`
`delete from table where restriction ;`

A restrição where em ambas as declarações funciona da mesma forma em que select e suporta o mesmo conjunto de operadores nos valores de coluna. Em ambos os casos, se você deixar de lado a restrição where, a atualização ou deleção será aplicada a all.rows (todas as colunas) na tabela, o que, geralmente, não é o que você quer.

### operador like

O operador like suporta uma forma simples de texto que combina padrões. Tudo o que está no lado esquerdo do operador (geralmente o nome de uma coluna de texto) será combinado com o padrão no lado direito. O padrão é uma string de texto SQL (então, está entre 'aspas simples') e pode usar o símbolo % para combinar qualquer substring, incluindo a string vazia.

Se você tiver familiaridade com expressões regulares, pense no % em padrões like como a regex .* (dot star/ponto asterisco).

Se você tem mais familiaridade com os padrões de nome de arquivo no shell do Unix ou do prompt de comando do Windows, % aqui é muito parecido com * (star/asterisco) nesses sistemas.

Por exemplo, para a linha da tabela onde a coluna fish tem o valor 'salmon', todas essas restrições seriam verdadeiras:
```
fish like 'salmon'
fish like 'salmon%'
fish like 'sal%'
fish like '%n'
fish like 's%n'
fish like '%al%'
fish like '%'
fish like '%%%'
```

E todos estes seriam falsos:
```
fish like 'carp'
fish like 'salmonella'
fish like '%b%'
fish like 'b%'
fish like ''
```

Aqui estamos atualizando a coluna content mas somente os conteúdos que tenha a
palavra spam
```
update posts set content = 'cheese' where content like '%spam%';
```