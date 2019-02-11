# Aula 10 - Criando classes tópicos avançados

Quando criamos uma classe nós conseguimos colocar variáveis internas dentro delas. Para acessarmos o seu valor basta escrever a instancia da class ou a pŕopria class e o nome da variável interna. Ex:

```
class Movie():
    """ This class provides a way to strore movie related information """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"] #Criamos variáveis que pertencem a instância
    
    def __init__(self, movie_title, movie_storyline, poster_image, 
                trailer_youtube):
                
media = Movie(foo)

print media.Movie.VALID_RATINGS  # => ["G", "PG", "PG-13", "R"]
```

### __doc__

No python tem algumas variáveis de `class` já existentes como `__doc__`.

Com ela nós conseguimos retornar o comentário de documentação da `class`

```
print (media.Movie.__doc__) # """ This class provides a way to strore movie related information """
```

### Herança
Para termos uma herança da `OOP` precisamos passar a `class` como argumento da 
`class` alvo e instanciamos ela dentro do `construtor` utilizando `__init__` passando
`self` e os argumentos utilizado pela mesma.

Tudo que estiver em parent como método ou variáveis sera acessado pela aquele que herda.

```
class Parent():
    def __init__(self, last_name, eye_color):
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print('Last Name - ' + self.last_name)
        print('Eye Color - ' + self.eye_color)

class Child(Parent): # Passando a class que queremos herdar.

    def __init__(self, last_name, eye_color, number_of_toys): # Passando os argumentos
    que serão utilizados tanto na class Child quando na Parent

        Parent.__init__(self, last_name, eye_color) # Iniciamos aqui a class herdada  passando os argumentos de Child para ela.
        self.number_of_toys = number_of_toys


billy_cyrus = Parent('Cyrus', 'blue')
billy_cyrus.show_info()

miley_cyrus = Child('Cyrus', 'Blue', 5)
miley_cyrus.show_info()

```

### Method Override ou Sobrescrever método.
Podemos sobrescrever os métodos da `class` pai. Isso é uma característica de `class`
que herdam.

Para realizar essa técnica basta escrever o mesmo nome do método da `class` 
herdada na `class` filha.

```
class Parent():
    def __init__(self, last_name, eye_color):
        self.last_name = last_name
        self.eye_color = eye_color
    
    def show_info(self):
        print('Last Name - ' + self.last_name)
        print('Eye Color - ' + self.eye_color)


class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        Parent.__init__(self, last_name, eye_color) 
        self.number_of_toys = number_of_toys
    
    def show_info(self):
        print('Last Name - ' + self.last_name)
        print('Eye Color - ' + self.eye_color)
        print("Number of toys - " + str(self.number_of_toys))

billy_cyrus = Parent('Cyrus', 'blue')
billy_cyrus.show_info() # Aqui mostra o sobrenome e cor dos olhos

miley_cyrus = Child('Cyrus', 'Blue', 5)
miley_cyrus.show_info() # Aqui sobrescreve o método do pai e mostra sobrenome e cor dos olhos e número de brinquedos.


```