# Aula 09 - Criando classes site de filmes

Para iniciar uma classe no python precisamos iniciar com a palavra reservada 
`class` e logo em seguida colocar o nome com a primera letra em maiúsculo.

### __init__ e self
Dentro da class podemos definir um método chamado `__init__` . Esse método 
é inicializado quando criamos a instância da nossa class, nele podemos passar 
argumentos para serem usados dentro da `class`.

O método `__init__` tem como primeiro argumento `self` que significa 
a própria classe.

No exemplo abaixo estamos criando uma class, passando argumentos e atribuindo valores aos atributos dentro de init.

```
# -*- coding: utf-8 -*-
import webbrowser

class Movie():
   
    def __init__(self, movie_title, movie_storyline, poster_image, 
                trailer_youtube):
        # Passando os argumentos correspondentes 
        # para criar as instancias das variáveis.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    # Criando método da instância para mostrar o trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

$guerracivil = new Movie('Guerra Cívil', 'História da marvel', 'foo', youtube trailer aqui');

```