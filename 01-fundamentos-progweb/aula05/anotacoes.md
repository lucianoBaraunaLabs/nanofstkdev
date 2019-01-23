# Aula 05 - Usando funções

### `os.listdir(r"./foo/)`
Lê todos os arquivos dentro da pasta e o 'r' significa para

### `os.getcwd()`
Pega o diretório atual.

### `os.chdir()`
Altera a referência do diretório no objeto `os`.

### `.translate()`
[https://www.programiz.com/python-programming/methods/string/translate](https://www.programiz.com/python-programming/methods/string/translate)
Resumindo altera valores de strings seguindo os valores estipulados.

```
file_name = '0124foo.txt'

print file_name.translate(None, "0123456789") # foo.txt

```