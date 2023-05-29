# Automato Finito Determinístico

Este projeto foi resultado de uma atividade proposta da disciplina de Linguagens Formais e Autômatos.
Um "Automato Finito Determinístico", denotado na implementação por AFD é uma 5-tupla que tem cinco atributos:

  - Alfabeto;
  - Conjunto de estados;
  - Função de transição;
  - Estado inicial;
  - Conjunto de estados finais. 

A Função de transição de estendida é o método que permite a execução do autômato, tendo recebido uma palavra qualquer.

Para fins de melhor visualização, foi implementado também um método que permite o "plot" da estrutura do autômato. A biblioteca utilizada para esse fim é a Graphviz.

## Requisitos
* graphviz==0.20.1
* Python3 (>= 3.6)

## Onde começar
1. Crie um arquivo no nível de `main.py`
2. Importe a biblioteca com
```python
# importar o menu
from lib import Menu

# importar apenas o AFD
from lib import AFD
```

## Documentação (Menu e AFD)

A classe AFD é uma classe interna múltipla, haja vista que sua implementação exige a existência de estados e transições, mas os estados e transições não podem existir sem ser em um AFD (não incluso aqui a ideia de que existam outros automatos).

### Menu com Plot
```python
from lib import Menu

# Você pode acessar os métodos do automato através de menu.afd (ex: menu.afd.add_state("q0", is_initial=True))
menu = Menu()

# Inicia o menu
menu.run()
```
