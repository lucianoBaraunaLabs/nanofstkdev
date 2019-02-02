# -*- coding: utf-8 -*-
import urllib

def read_text():
    quotes = open("/home/luciano/Documentos/dev/github/estudos/nanofstkdev/01-fundamentos-progweb/aula08/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check) # acessa o site
    output = connection.read() # abre a conexão
    # print(output)
    connection.close() # fecha a conexão
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could no scan the document properly.")
    

read_text()
