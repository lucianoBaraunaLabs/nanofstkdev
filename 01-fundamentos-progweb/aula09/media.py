# -*- coding: utf-8 -*-
import webbrowser

class Movie():
    # Init é o construtor da classe.
    # O argumento self significa a própria classe o famoso this no JS.
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
