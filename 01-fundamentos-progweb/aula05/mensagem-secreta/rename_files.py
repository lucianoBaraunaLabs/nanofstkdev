# -*- coding: utf-8 -*-
import os

def rename_files():
    #(1) Pegar todos os nomes dos arquivos na pasta
    # pegar o caminho como está sem alterar de nenhuma forma
    file_list = os.listdir("/home/luciano/Documentos/dev/github/estudos/nanofstkdev/01-fundamentos-progweb/aula05/mensagem-secreta/prank")
    os.chdir("/home/luciano/Documentos/dev/github/estudos/nanofstkdev/01-fundamentos-progweb/aula05/mensagem-secreta/prank")
    #(2) renomear cada arquivo
    for file_name in file_list:
        print 'old name file ---> ' + file_name
        print 'new name file ---> ' + file_name.translate(None, "0123456789")
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print file_name

rename_files()