# -*- coding: utf-8 -*-
import os

def rename_files():
    #(1) Pegar todos os nomes dos arquivos na pasta
    # os.listdir(r"./prank/) - lê todos os arquivos dentro da pasta e o 'r' significa para
    # pegar o caminho como está sem alterar de nenhuma forma
    file_list = os.listdir("/home/luciano/Documentos/dev/github/estudos/nanofstkdev/01-fundamentos-progweb/aula05/mensagem-secreta/prank")
    saved_path = os.getcwd()
    print 'Diretório atual ---> ' + saved_path
    os.chdir("/home/luciano/Documentos/dev/github/estudos/nanofstkdev/01-fundamentos-progweb/aula05/mensagem-secreta/prank")
    #(2) renomear cada arquivo
    for file_name in file_list:
        # file_name.translate(None, "0123456789") renomeia o arquivo removendo os valores estipulados
        print 'old name file ---> ' + file_name
        print 'new name file ---> ' + file_name.translate(None, "0123456789")
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print file_name
    # os.chdir(saved_path)
    # print 'Diretório atual para salvar ---> ' + saved_path

rename_files()