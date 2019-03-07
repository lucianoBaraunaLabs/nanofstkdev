# Aula 06 - Operadores e comparações

Selecionando todas as colunas de animais que sejam da espécie lhama e que tenham
nascido entre 01/01/1995 e até 31/12/1998

```
select * from animals where species = 'llama' and (birthdate >= '1995-01-01') and (birthdate <= '1998-12-31')
```