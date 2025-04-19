# Exercício

O arquivo `worldcities.csv` é um conjunto de dados aberto com alguns dados de cidades de inumeros paises e usaremos esse conjunto de dados para alguns exerícios. Portanto, é necessário prepará-lo.

Faça as seguintes etapas:

### Pré-processar os dados
- Utilizando o arquivo `worldcities.csv`, filtre os dados para uma estrutura (tal como, Dataframe Pandas) apenas com cidades que sejam do estado do Paraná (Brasil)

### Modele os dados
- Selecionar aleatoriamente a quantidade de cidades vizinhas com estradas que as interligam (quantidade deve ser entre 2 ou 6 cidades)
- Calcular as n cidades mais próximas (n foi selecionado no item anterior) usando a formula de Haversine (sugestão, use o pacote haversine do Python)
- Fazer uma estrutura (utilizando dicionário) que represente as conexões (estradas) entre as cidades
  - Exemplo 1: 
  ```
  {
    'Curitiba': ['Londrina', 'Maringá', 'Ponta Grossa'],
    'Londrina': ['Curitiba', 'Maringá', 'Cambé, 'Ibiporã', 'Jataizinho'],
    'Ponta Grossa': ['Curitiba', 'Cascavel', 'Sabáudia']
  }
  ```
  - Exemplo 2:
  
  | No_1  | No_2 |
  | ----- | ----- |
  | Curitiba  | Londrina  |
  | Curitiba  | Maringá   |
  | Londrina  | Curitiba  |
  | Londrina  | Cambé     |
  | Ponta Grossa  | Curitiba  |
  | Ponta Grossa  | Cascavel  |

### Salve a estrutura

Salve os dados em um arquivo `JSON` (exemplo 1) ou `CSV` (exemplo 2) e submeta no classroom junto com o código utilizado para gerá-los.


### Considerações finais

É permitido utilizar a biblioteca [NetworkX](https://networkx.org/) ([Tutorial simples com exemplos de usos](https://diegomariano.com/networkx/)) ou outro pacote que possa auxiliar.