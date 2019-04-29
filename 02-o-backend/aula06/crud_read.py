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

# Pegando a primeira linha da tabela.
firstResult = session.query(Restaurant).first()

# Exibindo o valor de nome
print firstResult.name

# Pegando todos os resultados. 
items = session.query(Menuitem).all()

#Exibindo eles.
for item in items:
    print item.name