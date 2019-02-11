# -*- coding: utf-8 -*-

class Parent():
    def __init__(self, last_name, eye_color):
        print('Parent Constructor called')
        self.last_name = last_name
        self.eye_color = eye_color
    
    def show_info(self):
        print('Last Name - ' + self.last_name)
        print('Eye Color - ' + self.eye_color)

# No argumento da class child passamos a class que queremos herdar.
class Child(Parent): 
    def __init__(self, last_name, eye_color, number_of_toys): 
        # Passamos também os argumento da class herdada que queremos utilizar
        print('Child Constructor Called')
        # Iniciamos aqui a class herdada junto dos argumentos 
        # que utilizaremos além de instanciar o self
        Parent.__init__(self, last_name, eye_color) 
        self.number_of_toys = number_of_toys
    
    def show_info(self):
        print('Last Name - ' + self.last_name)
        print('Eye Color - ' + self.eye_color)
        print("Number of toys - " + str(self.number_of_toys))

billy_cyrus = Parent('Cyrus', 'blue')
billy_cyrus.show_info()
# print(billy_cyrus.last_name)

miley_cyrus = Child('Cyrus', 'Blue', 5)
# print(miley_cyrus.last_name)
miley_cyrus.show_info()


