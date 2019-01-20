# -*- coding: utf-8 -*-
import os

def rename_files():
    #(1) Pegar todos os nomes dos arquivos na pasta
    # os.listdir(r"./prank/) - lê todos os arquivos dentro da pasta e o 'r' significa para
    # pegar o caminho como está sem alterar de nenhuma forma
    file_list = os.listdir("./prank")
    print file_list
    #(2) renomear cada arquivo

rename_files()