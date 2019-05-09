# Aula 08 - Desenvolvendo com frameworks
O framework utilizado será o flask.

Ao rodar o python uma variavel especial name define o aplicativo e as importações utilizadas

```
from flask import Flask 
app = Flask(__name__) 
```

Para criarmos as rotas utilizamos os método :

[Explicação sobre o operador `@`](https://www.programiz.com/python-programming/decorator)

```
@app.route('/hello')
```

Em python quando importamos um arquivo ele possui um nome
que fica registrado na variável `__name__`.

E quando não importamos esse arquivo o valor dessa variável é `__main__` e caso esse arquivo seja importado
ele recebe o nome do arquivo.

Ex: Se temos um arquivo `project` e estamos importando ele
o nome de dele será `project`. Caso estejamos executando
ele o nome será `__main__`

[Link para explicação mais detalhada](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)

```
# Se não for importado execute o bloco.
if __name__ == '__main__': 
    foo()
```

# Configurações e métodos do flask

- `app.debug = True` - Habilita depuração no navegador e reload sempre que tem alguma alteração
- `app.run(host='0.0.0.0', port = 5000)`  - Configuração do server.