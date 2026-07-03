# Problema 4: Montando uma tabela de análise com pandas
#
# Objetivo: praticar pandas — montar um DataFrame a partir dos dados do FASTA,
# criar colunas calculadas com suas funções, e então ordenar, filtrar e salvar.
#
# Leia o enunciado completo em problemas/README.md
#
# Passos:
#   1) Leia o arquivo multiFASTA e monte um DataFrame:
#        df = pd.DataFrame(organismos)   # cada organismo vira uma linha!
#   2) Crie colunas calculadas: tamanho, gc (e, se quiser, contagem de bases).
#   3) Ordene por gc e mostre as 10 maiores.
#   4) Filtre os organismos com gc > 0.5.
#   5) Salve o resultado em um arquivo .csv.
#
# Dicas de import:
#   import pandas as pd
#   from bio.ler_fasta import ler_fasta
#   from bio.sequencia import calcular_percentual, contar_bases
#
# Dica para criar colunas aplicando uma função a cada linha:
#   df["gc"] = df["sequencia"].apply(lambda s: calcular_percentual(s, ["G", "C"]))
#   df["tamanho"] = df["sequencia"].apply(len)
#
# Dica para salvar: df.to_csv("resultado.csv", index=False)
