# Funções de manipulação de sequências de DNA.
#
# Nossa "mini BioPython"! Aqui cada função recebe uma sequência como uma
# STRING (ex: "ATCG") e devolve um resultado (outra string, um número, etc.).
# Não usamos classes: é tudo função + string, como você já está acostumado.
#
# IMPORTANTE: implemente cada função abaixo. Apague o
# "raise NotImplementedError(...)" quando for resolver.

# Você vai precisar destas constantes na função traduzir():
# from bio.constantes import DNA_PARA_AMINOACIDO, DNA_STOP_CODONS


def complementar(sequencia):
    """
    Retorna uma NOVA string com a sequência complementar.

    Lembre-se do pareamento das bases: A<->T e C<->G.
    Ex: complementar("ATCG") -> "TAGC"

    Dica: percorra cada base da sequência e vá montando (concatenando)
    a sequência complementar numa nova string.
    """
    raise NotImplementedError("Implemente a função complementar")


def complementar_reversa(sequencia):
    """
    Retorna uma NOVA string com a sequência complementar reversa.

    Ex: complementar_reversa("ATCG") -> "CGAT"

    Dica: é o complementar "de trás para frente". Você pode reaproveitar
    a função complementar() que acabou de escrever e depois inverter o
    resultado (lembre-se do truque de fatiamento [::-1]).
    """
    raise NotImplementedError("Implemente a função complementar_reversa")


def transcrever(sequencia):
    """
    Retorna uma NOVA string com o resultado da transcrição (DNA -> RNA).

    Ex: transcrever("ATCG") -> "AUCG"

    Dica: na transcrição, a base T (timina) vira U (uracila).
    """
    raise NotImplementedError("Implemente a função transcrever")


def traduzir(sequencia, parar=False):
    """
    Retorna uma STRING com a tradução da sequência para uma proteína.

    Ex: traduzir("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG") -> "MAIVMGR*KGAR*"

    Regras:
    - Leia a sequência de 3 em 3 bases (cada trinca é um "códon").
    - Use o dicionário DNA_PARA_AMINOACIDO (em bio/constantes.py) para
      descobrir qual aminoácido cada códon representa.
    - Se o códon for um stop codon (veja a lista DNA_STOP_CODONS), o
      aminoácido é "*".
    - Se a trinca NÃO estiver no dicionário (base indefinida, como "N"),
      use "X" para indicar que não dá para saber.
    - Se parar=True, a tradução deve PARAR no primeiro stop codon.
      Se parar=False, continue até o fim, marcando os stops como "*".

    Dica: importe o dicionário no topo do arquivo:
        from bio.constantes import DNA_PARA_AMINOACIDO, DNA_STOP_CODONS
    Dica: para pegar as trincas, o passo do range pode ser 3 -> range(0, len, 3).
    """
    raise NotImplementedError("Implemente a função traduzir")


def calcular_percentual(sequencia, bases):
    """
    Recebe uma LISTA de bases e retorna o percentual dessas bases na sequência.

    Ex: calcular_percentual("ATCGAAA", ["A"]) -> 0.5   (4 As em 8 bases... veja abaixo)
    Ex: calcular_percentual("ATCGCC", ["C", "G"]) -> ~0.66  (4 Cs/Gs em 6 bases)

    Dica: conte quantas bases da sequência estão dentro da lista "bases" e
    divida pelo tamanho total da sequência.
    """
    raise NotImplementedError("Implemente a função calcular_percentual")


def contar_bases(sequencia):
    """
    Retorna um DICIONÁRIO com a contagem de cada base na sequência.

    Ex: contar_bases("ATCGA") -> {"A": 2, "T": 1, "C": 1, "G": 1}

    Dica: crie um dicionário começando as contagens em 0 e vá somando 1
    conforme percorre cada base da sequência. (Isso vai ser bem útil no
    exercício de pandas!)
    """
    raise NotImplementedError("Implemente a função contar_bases")


def distancia_hamming(sequencia_a, sequencia_b):
    """
    Compara duas sequências do mesmo tamanho e retorna em quantas posições
    elas são DIFERENTES (a chamada "distância de Hamming").

    Ex: distancia_hamming("ATCG", "ATGG") -> 1   (diferem só na 3a base)

    É uma forma simples de medir o quão "parecidas" são duas sequências:
    quanto maior a distância, mais mutações há entre elas.

    Dica: percorra as duas sequências ao mesmo tempo, posição por posição,
    e conte as posições em que as bases não batem.
    """
    raise NotImplementedError("Implemente a função distancia_hamming")
