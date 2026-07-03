# Problemas

Agora que você criou suas funções em `bio/sequencia.py`, vamos usá-las para resolver
problemas reais de bioinformática! Cada problema tem um **Objetivo** (o que você vai
praticar), diz **quais funções usar** e descreve a **tarefa** (os passos).

Em todos eles você vai começar lendo o arquivo `arquivos/Flaviviridae-genomes.fasta` com a
função de apoio `ler_fasta`.

---------------------------

## Problema 1: Análise de Composição de Nucleotídeos

**Objetivo:** praticar percorrer uma lista de dados e aplicar suas próprias funções para
descrever a composição de cada sequência. O "conteúdo GC" (percentual de C + G) é uma medida
muito usada em biologia — ele influencia, por exemplo, a estabilidade do DNA.

**Funções que você vai usar:** `ler_fasta`, `calcular_percentual`.

**Tarefa:** escreva um script que:
1. Leia o arquivo multiFASTA com `ler_fasta`.
2. Para cada organismo, imprima o percentual de cada nucleotídeo (A, T, C, G) e o conteúdo
   GC (percentual de C + G).

Dica: `calcular_percentual(organismo["sequencia"], ["G", "C"])`.

---------------------------

## Problema 2: Tradução de Nucleotídeos para Proteínas

**Objetivo:** praticar a aplicação da função de tradução — o processo pelo qual a célula
"lê" o DNA de 3 em 3 bases e monta uma proteína. É um dos conceitos centrais da biologia
molecular.

**Funções que você vai usar:** `ler_fasta`, `traduzir`.

**Tarefa:** escreva um script que:
1. Leia o arquivo multiFASTA.
2. Traduza a sequência de cada organismo para a sua proteína correspondente.
3. Imprima as sequências de proteínas.

Dica: `traduzir(organismo["sequencia"])`.

---------------------------

## Problema 3: Identificação de Mutação em Genomas Virais

#### Contexto

Você está colaborando com uma equipe de virologistas que estuda mutações específicas em
genomas de vírus da família Flaviviridae. Eles identificaram uma mutação de interesse que
ocorre na **posição 1000** das sequências, onde o nucleotídeo `A` é substituído por `G`.
Seu trabalho é identificar se essa mutação está presente nas sequências fornecidas e gerar
um relatório. Esta análise é importante para entender a evolução dos vírus e suas possíveis
implicações na virulência e na resistência a tratamentos.

**Objetivo:** praticar acessar uma posição específica de uma string (indexação) e usar isso
para procurar uma mutação. Lembre-se: em Python a contagem começa no 0, então a "posição
1000" corresponde ao índice `999`.

**Funções que você vai usar:** `ler_fasta` (e indexação de string, ex: `sequencia[999]`).

**Tarefa:** escreva um script que:
1. Leia o arquivo multiFASTA com os genomas virais.
2. Verifique, para cada sequência, se a base na posição 1000 é a da mutação (`G`).
3. Gere um relatório indicando quais sequências possuem a mutação e quais não possuem.

---------------------------

## Problema 4: Montando uma tabela de análise com pandas

#### Contexto

Analisar as sequências uma por uma no terminal funciona, mas quando temos **muitos**
organismos (o nosso arquivo tem mais de 150!) fica difícil comparar. Cientistas costumam
organizar tudo em uma **tabela** para ordenar, filtrar e resumir os dados com facilidade.
É exatamente para isso que serve o pandas.

**Objetivo:** praticar pandas — montar um `DataFrame` a partir dos dados do FASTA, criar
colunas calculadas usando as funções que você escreveu, e então ordenar, filtrar e salvar
o resultado.

**Funções que você vai usar:** `ler_fasta`, `calcular_percentual`, `contar_bases` (e o
pandas: `import pandas as pd`).

**Tarefa:** escreva um script que:
1. Leia o arquivo multiFASTA com `ler_fasta` e monte um DataFrame:
   `df = pd.DataFrame(organismos)` (cada organismo vira uma linha!).
2. Crie novas colunas calculadas a partir da coluna `sequencia`:
   - `tamanho`: o número de bases da sequência.
   - `gc`: o conteúdo GC (use `calcular_percentual`).
   - (opcional) uma coluna para a contagem de cada base (use `contar_bases`).
3. **Ordene** a tabela pelo conteúdo GC e mostre as 10 sequências com maior GC.
4. **Filtre** a tabela para ver só os organismos com GC acima de 50% (`gc > 0.5`).
5. **Salve** o resultado em um arquivo `.csv`.

Dica para criar uma coluna aplicando uma função a cada linha:
```python
df["gc"] = df["sequencia"].apply(lambda s: calcular_percentual(s, ["G", "C"]))
df["tamanho"] = df["sequencia"].apply(len)
```
Dica para salvar: `df.to_csv("resultado.csv", index=False)`.
