# Problema 1: Análise de Composição de Nucleotídeos
#
# Objetivo: percorrer os organismos e usar suas funções para descrever a
# composição de cada sequência (percentual de A, T, C, G e conteúdo GC).
#
# Leia o enunciado completo em problemas/README.md
#
# Passos:
#   1) Use a função ler_fasta para ler arquivos/Flaviviridae-genomes.fasta
#   2) Para cada organismo, imprima o percentual de A, T, C, G
#      e o conteúdo GC (percentual de C + G).
#
# Dicas de import:
#   from bio.ler_fasta import ler_fasta
#   from bio.sequencia import calcular_percentual
#
# Dica: cada organismo é um dicionário, então a sequência está em
#       organismo["sequencia"]. Ex:
#       calcular_percentual(organismo["sequencia"], ["G", "C"])
