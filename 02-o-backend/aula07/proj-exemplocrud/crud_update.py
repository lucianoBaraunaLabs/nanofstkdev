# -*- coding: utf-8 -*-

# Importando módulos necessários para a operação create
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Importando as tabelas do banco
from database_setup import Base, Restaurant, Menuitem

# A função create_engine permite que nosso programa saiba com qual mecanismo
# de banco de dados
engine = create_engine('sqlite:///restaurantmenu.db')

# Juntando as definições de classe com as tabelas do banco
Base.metadata.bind = engine

# Criando uma sessão de execução de código com o banco.
DBSession = sessionmaker(bind = engine)

# Abrindo uma sessão para executarmos os comandos no banco
session = DBSession()

# Quando utilizamos a função one() faz com que o sqlAlchemy retorne exatamente a
# linha específica.
# UrbanVeggieBurger = session.query(Menuitem).filter_by(id = 2).one()
# print UrbanVeggieBurger.price

# Atualizando valores 
# UrbanVeggieBurger.price = '$2.99'
# session.add(UrbanVeggieBurger)
# session.commit()

# Pegando um valores específico com o name
veggieBurgers = session.query(Menuitem).filter_by(name = 'Veggie Burger')
for veggieBurger in veggieBurgers:
    # Atualizando todos valores que são diferentes de 2.99
    if veggieBurger.price != '$2.99':
        veggieBurger.price = '$2.99'
        session.add(veggieBurger)
        session.commit()

    print veggieBurger.id
    print veggieBurger.price
    print veggieBurger.restaurant.name
    print "\n"

