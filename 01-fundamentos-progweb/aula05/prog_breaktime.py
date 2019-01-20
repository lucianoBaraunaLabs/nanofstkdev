# -*- coding: utf-8 -*-

import webbrowser # abre o navegador
import time # Função que estipula um tempo para executar próximo passo

total_breaks = 1
break_count = 0

print ('Esse programa iniciou em ' + time.ctime())
while(break_count < total_breaks):
    time.sleep(3)
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    break_count = break_count + 1
