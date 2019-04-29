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

# Criando o nome do restaurante.
myFirstRestaurant = Restaurant(name = "Pizza Palace")

# Adicionando as insercções de myFirstRestaurant ao banco
session.add(myFirstRestaurant)

# Fechando a sessão e salvando as alterações
session.commit()

# Pegando os valores do banco da tabela alvo.
print session.query(Restaurant).all()

# Adicionando valores a tabela item de menu.
cheessepizza =  Menuitem(name = 'Cheese Pizza', description = "Made with all natural ingredients and fresh mozzarella", course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)

session.add(cheessepizza)
session.commit()
session.query(Menuitem).all()