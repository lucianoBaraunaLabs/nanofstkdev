# Revisão CRUD

### Operações com SQLAlchemy
Nesta aula, realizaremos todas as nossas operações CRUD com SQLAlchemy em um banco de dados SQLite. Antes que realizemos qualquer operação, nós devemos primeiro importar as bibliotecas necessárias, conectar ao nosso restaurantMenu.db e criar uma sessão em interface com o banco de dados:

```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantMenu.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
```

### CREATE (criar)
Nós criamos um novo restaurante e o chamamos de Pizza Palace:
```
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
sesssion.commit()
```

Nós criamos um item de menu, uma pizza de queijo, e o adicionamos 
ao menu do Pizza Palace:

```
cheesepizza = menuItem(name="Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella", course="Entree", price="$8.99", restaurant=myFirstRestaurant)
session.add(cheesepizza)
session.commit()
```

### READ (ler)
Nós lemos informações em nosso banco de dados usando o método query em SQLAlchemy:
```
firstResult = session.query(Restaurant).first()
firstResult.name

items = session.query(MenuItem).all()
for item in items:
    print item.name
```

### UPDATE (atualizar)
Para atualizar uma entrada existente em nosso banco de dados, precisamos executar os seguintes comandos:

1. Encontrar entrada
2. Redefinir valor(es)
3. Adiciona à sessão
4. Executar session.commit()

Encontramos o veggie burger que pertencia ao restaurante Urban Burger 
executando a seguinte query:
 
```
veggieBurgers = session.query(MenuItem).filter_by(name= 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print veggieBurger.id
    print veggieBurger.price
    print veggieBurger.restaurant.name
    print "\n"
```
E, então, atualizamos o preço do veggie burger para US$ 2,99:
```
UrbanVeggieBurger = session.query(MenuItem).filter_by(id=8).one()
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit() 
```

### DELETE (deletar)
Para deletar um item de nosso banco de dados, devemos seguir os seguintes passos:

1. Encontrar entrada
2. Session.delete(Entry)
3. Session.commit()

Deletamos o spinach Ice Cream de nosso banco de dados de itens de menus com as seguintes operações:

```
spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
session.delete(spinach)
session.commit() 
```