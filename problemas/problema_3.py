# Problema 3: Identificação de Mutação em Genomas Virais
#
# Objetivo: acessar uma posição específica de cada sequência (indexação) para
# verificar se uma mutação está presente e gerar um relatório.
#
# Contexto: procurar a mutação A -> G na posição 1000 das sequências.
#
# Leia o enunciado completo em problemas/README.md
#
# Passos:
#   1) Use a função ler_fasta para ler o arquivo multiFASTA.
#   2) Para cada sequência, verifique a base na posição 1000.
#   3) Gere um relatório dizendo quais sequências têm a mutação e quais não.
#
# Dica de import:
#   from bio.ler_fasta import ler_fasta
#
# Dica: a sequência está em organismo["sequencia"] e você pode acessar uma
#       base por índice, ex: organismo["sequencia"][999]
#       (lembre-se que em Python a contagem começa no 0, então a posição
#        1000 é o índice 999!)
