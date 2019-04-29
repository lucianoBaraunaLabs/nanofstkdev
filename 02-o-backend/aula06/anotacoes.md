# Aula 06 - Trabalhando com CRUD

Para ajudar na manipulação dos dados em python nós podemos utilizar o ORM(SqlAlchemy)

### Definição básica de um ORM

ORM (Object Relational Mapper) é uma técnica de mapeamento objeto relacional que 
permite fazer uma relação dos objetos com os dados que os mesmos representam. 
Ultimamente tem sido muito utilizada e vem crescendo bastante nos últimos anos.

Existem dois mundos: o relacional e o orientado a objetos.

No mundo relacional prevalecem princípios matemáticos com a finalidade de 
armazenar e gerenciar corretamente os dados, de forma segura e se trabalha 
com a linguagem SQL que é utilizada para dizer o banco de dados “O QUE?” fazer e não como fazer.

Já no mundo orientado a objetos trabalhamos com classes e métodos, ou seja, 
trabalhamos fundamentados na engenharia de software e seus princípios que nos 
dizem “COMO” fazer. O ORM é justamente, a ponte entre estes dois mundos, ou seja, 
é ele quem vai permitir que você armazene os seus objetos no banco de dados.

### Criando um banco de dados com SQLAlchemy

Ao criarmos o banco dessa maneira precisamos passar por alguns processos.
- **Código de configuração** que é usado para importar todos os módulos necessários.
- **Class** são criadas para representar os dados no Python.
- **Tabela** são criadas para representar a tabela específica no banco de dados.
- **Mapper** que conecta as colunas de nossa tabela à classe.

### Criando uma tabela.

Quando criamos uma tabela com o SQLAlchemy nós precisamos criar uma classe para
cada tabela do banco e nela passarmos suas configurações.

### Atributos com SQLAlchemy.
- `String(250)` - Criando uma string de 250 caracteres
- `Integer` - Criando inteiro
- `relationship(Class)` - Criando uma relação com outra tabela
- `nullable = boolean` - Indica uma entrada de coluna que deve ter um valor para que a linha seja criada.
- `primary_key = True` - Valor true indica que identificamos exclusivamente cada linha da nossa tabela no banco
- `ForeignKey('some_table.id')` - Pegando um valor de outra tabela para ser chave estrangeira.

Após todos as configurações feitas, basta executarmos o arquivo pelo terminal

A configuração pode ser vista com detalhes no [database_setup.py](database_setup.py)

### Criando um registro no banco.
Processos documentados no arquivo: [crud_create.py](crud_create.py)

**Documentação sobre querys utilizando** - https://docs.sqlalchemy.org/en/13/orm/query.html

### Lendo dados do banco.
Temos algumas funções que ajudam na hora de lermos nosso banco.
- session.query(Restaurant).all() - Pega todos os dados da tabela restaurante.
- session.query(Restaurant).first() - Pega somente a primeira linha.

Aqui estamos lendo alguns dados.
```
veggieBurgers = session.query(Menuitem).filter_by(name = 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print veggieBurger.id
    print veggieBurger.price
    print veggieBurger.restaurant.name
    print "\n"
```

### Atualizando dados.

Para atualizarmos os dados precisamos primeiro ter ele em mãos.
**A função one() ajuda para garantir que aquele dado é realmente ele**

```
UrbanVeggieBurger = session.query(Menuitem).filter_by(id = 2).one()
print UrbanVeggieBurger.price
```
E em seguida atualizamos os valores e commitamos as modificações.
```
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit()
```
### Deletar coluna
Precisamos selecionar o elemento que queremos, passamos ele para a função delete
e depois confirmamos ação.
```
# Selecionando o elemento que queremos apagar.
spinach = session.query(Menuitem).filter_by(name='Spinach Ice Cream').one()
print spinach.restaurant.name

# Passamos ele para ser deletado
session.delete(spinach)

# Commitando a ação
session.commit()
```