# -*- coding: utf-8 -*-

import os
import sys

# Utilizado para escrever o código do mapeador (mapper)
from sqlalchemy import Column, ForeignKey, Integer, String

# Código utilizado na configuração para criação da classe.
from sqlalchemy.ext.declarative import declarative_base

# Relação de chave estrangeira
from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

# Ajuda a pegar os comandos base do sqlalchemy para extendermos nas classes
Base = declarative_base()

# Criando as classes que correspondem as tabelas. 
class Restaurant(Base):
    # Variável de configuração extendida de base para criar nome da tabela.
    __tablename__ = 'restaurant' 
    
    # Criando uma coluna id que aceita somente valores inteiros 
    # e definiremos a chave primaira como verdadeira
    id = Column(
        Integer, 
        primary_key = True
    )
    
    # Criando uma coluna nome com espaço de 80 caracteres e como nullable é false
    # isso significa que se o nome deve ser enviado caso se não não criamos nada.
    name = Column(
        String(250),
        nullable = False
    )


class Menuitem(Base):
    __tablename__ = 'menu_item'

    # Criando uma coluna nome com espaço de 80 caracteres e como nullable é false
    # isso significa que se o nome deve ser enviado caso se não não criamos nada.
    name = Column(
        String(80), 
        nullable = False
    )

    # Criando uma coluna id que aceita somente valores inteiros 
    # e definiremos a chave primaira como verdadeira
    id = Column(
        Integer,
        primary_key = True
    )
    
    # course, description e price são strings.
    course = Column(String(250))

    description = Column(String(250))

    price = Column(String(8))

    # Criando uma coluna id que aceita somente valores inteiros 
    # e definiremos a chave estrangeira ligando ela a restaurant.id.
    # Isso vai dizer que sempre que criarmos um id de restaurante ele vai pegar o
    # is do restaurante na classe Restaurante
    restaurant_id = Column(
        Integer,
        ForeignKey('restaurant.id')
    )
    # E aqui estamos dizendo que existe uma relação entre meu variável resturante
    # a classe Restaurante
    restaurant = relationship(Restaurant)

    # We added this serialize function to be able to send JSON objects in a serializable format
    @property
    def serialize(self):
       return {
        'name'        : self.name,
        'description' : self.description,
        'id'          : self.id,
        'price'       : self.price,
        'course'      : self.course,
       }

# Configurações que correspondem ao banco de dados
#### insert at end of file ####
engine = create_engine(
    'sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)