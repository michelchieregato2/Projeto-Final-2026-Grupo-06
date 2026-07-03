# Usando as suas funções

Depois de criar as funções em `bio/sequencia.py`, você tem **duas entregas** nesta pasta:

1. **`exercicios_funcoes.py`** — testar cada função isoladamente. Mostra que você domina o
   básico. (Veja a primeira seção abaixo.)
2. **`projeto.py`** — a investigação completa dos vírus da família Flaviviridae, montando uma
   tabela com pandas e tirando conclusões. É aqui que você mostra que sabe *aplicar* as
   funções num problema real. (Veja "O Projeto", mais abaixo.)

> **Preparação:** o projeto usa pandas. Se ainda não instalou, rode na raiz do projeto:
> `pip install -r requirements.txt`

=================================================================

# Entrega 1 — Exercícios das funções (`exercicios_funcoes.py`)

Confira que cada função que você criou funciona numa sequência pequena. Para cada uma,
escreva um `print` e veja se o resultado bate com o esperado:

- `complementar("ATCG")` -> `"TAGC"`
- `complementar_reversa("ATCG")` -> `"CGAT"`
- `transcrever("ATCG")` -> `"AUCG"`
- `encontrar_inicio("CCCATGGGGTAA")` -> `"ATGGGGTAA"` (começa no 1º `ATG`)
- `traduzir("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")` -> `"MAIVMGR*KGAR*"`
- `traduzir(..., parar=True)` -> deve parar no primeiro stop codon
- `calcular_percentual("ATCGAAAA", ["A"])` -> `0.5`
- `contar_bases("ATCGA")` -> `{"A": 2, "T": 1, "C": 1, "G": 1}`

O arquivo `exercicios_funcoes.py` já vem com os blocos prontos para você preencher.

=================================================================

# Entrega 2 — O Projeto: um panorama da família Flaviviridae (`projeto.py`)

O arquivo `arquivos/Flaviviridae-genomes.fasta` reúne os genomas de referência de **toda a
família viral _Flaviviridae_** — mais de 150 vírus diferentes, incluindo velhos conhecidos
como **Dengue, Zika, Febre Amarela e Hepatite C**. São vírus aparentados, mas de gêneros
distintos (Orthoflavivirus, Hepacivirus, Pestivirus, Pegivirus...).

Nossa meta é montar uma **tabela** (com pandas) descrevendo esses vírus e, a partir dela,
responder a duas perguntas:

1. O **conteúdo GC** dos genomas é distribuído ao acaso, ou vírus parecidos se parecem também nisso?
2. Esses vírus têm um genoma organizado de forma parecida? Quão grande é a **proteína** que cada um produz?

Vamos construir isso por partes. Cada função que você escreveu vai virar uma peça da análise.

---------------------------

## Parte 1 — Montando a tabela

**Objetivo:** transformar os dados do FASTA numa tabela do pandas, onde cada linha é um vírus.

1. Leia o arquivo com `ler_fasta` (ele devolve uma lista de dicionários).
2. Monte o DataFrame: `df = pd.DataFrame(organismos)`. Você deve ter as colunas
   `id`, `nome` e `sequencia`.
3. Crie a coluna `tamanho` com o número de bases de cada genoma.

Dicas:
```python
import pandas as pd
from bio.ler_fasta import ler_fasta

organismos = ler_fasta("arquivos/Flaviviridae-genomes.fasta")
df = pd.DataFrame(organismos)
df["tamanho"] = df["sequencia"].apply(len)
```

---------------------------

## Parte 2 — O conteúdo GC é aleatório?

**Objetivo:** usar a coluna de GC para investigar se vírus parecidos têm GC parecido.

O **conteúdo GC** é o percentual de bases C + G no genoma. Ele varia de vírus para vírus.
Vamos ver se essa variação diz alguma coisa.

1. Crie a coluna `gc` usando a sua função `calcular_percentual`.
2. **Ordene** a tabela por `gc` e mostre, **com o nome**, os 10 vírus de **maior** GC e os
   10 de **menor** GC.
3. **Conclusão (escreva num `print` ou comentário):** olhe os nomes dos dois extremos.
   Os vírus de GC mais alto parecem ser do mesmo tipo entre si? E os de GC mais baixo?
   Repare nas palavras que se repetem nos nomes. O GC parece aleatório ou não?

Dicas:
```python
df["gc"] = df["sequencia"].apply(lambda s: calcular_percentual(s, ["G", "C"]))
df.sort_values("gc", ascending=False)[["nome", "gc"]].head(10)   # maior GC
df.sort_values("gc")[["nome", "gc"]].head(10)                     # menor GC
```

---------------------------

## Parte 3 — Encontrando a proteína (a poliproteína viral)

**Objetivo:** usar `encontrar_inicio` + `traduzir` para descobrir o tamanho da proteína de
cada vírus, e ver o que isso revela sobre a organização do genoma.

Um detalhe importante de biologia: nos Flaviviridae, o genoma inteiro é traduzido como
**uma única proteína gigante** (chamada *poliproteína*), que depois a célula corta em
pedaços menores. Repare que os nomes no FASTA dizem "**polyprotein**"!

Mas atenção: a tradução do gene **não começa na primeira base** do genoma — há um trecho
inicial que não é traduzido. Por isso precisamos primeiro achar o **start codon** (`ATG`)
com a sua função `encontrar_inicio`, e só então traduzir.

1. Crie a coluna `proteina`: para cada sequência, ache o início com `encontrar_inicio` e
   traduza **parando no primeiro stop codon** (`parar=True`).
2. Crie a coluna `tamanho_proteina` com o número de aminoácidos dessa proteína.
3. Crie a coluna `cobertura`: quanto do genoma essa proteína ocupa. Como cada aminoácido
   vem de 3 bases, isso é `(tamanho_proteina * 3) / tamanho`.
4. **Conclusão (escreva num `print` ou comentário):** qual é a cobertura *típica* (use
   `df["cobertura"].median()`)? Para a maioria dos vírus, a proteína cobre uma parte grande
   do genoma? Isso combina com a ideia de que esses vírus têm **uma** poliproteína só?
   (Você também vai notar alguns casos com cobertura baixa — nesses, o primeiro `ATG` que
   achamos não era o começo certo do gene. Não tem problema, comente que isso acontece.)

Dicas:
```python
df["proteina"] = df["sequencia"].apply(lambda s: traduzir(encontrar_inicio(s), parar=True))
df["tamanho_proteina"] = df["proteina"].apply(len)
df["cobertura"] = (df["tamanho_proteina"] * 3) / df["tamanho"]
```

---------------------------

## Parte 4 — Salvando o resultado

**Objetivo:** guardar a sua tabela final para consulta.

1. **Filtre** a tabela para ver só os vírus com GC acima de 50% (`df["gc"] > 0.5`) —
   quantos são?
2. **Salve** a tabela completa num arquivo `.csv`.

Dica:
```python
df.to_csv("resultado.csv", index=False)
```

Pronto! Você partiu de um arquivo de texto com 150+ genomas e chegou a uma tabela que
revela padrões reais da biologia desses vírus. É exatamente assim que se começa uma análise
de bioinformática.
