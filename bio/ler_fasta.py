# Função de apoio: JÁ ESTÁ PRONTA para você usar!
#
# Ela lê um arquivo FASTA e devolve uma LISTA DE DICIONÁRIOS, onde cada
# dicionário representa um organismo com as chaves "id", "nome" e "sequencia".
#
# Ex de retorno:
#   [
#     {"id": "NC_074786.1", "nome": "Guereza hepacivirus...", "sequencia": "CACTCC..."},
#     {"id": "NC_074787.1", "nome": "Hepatitis GB virus A...", "sequencia": "ATGGCA..."},
#     ...
#   ]
#
# Esse formato (lista de dicionários) é bem prático: dá para percorrer com um
# for e, no exercício de pandas, vira uma tabela com pd.DataFrame(organismos).


def ler_fasta(caminho_do_arquivo):
    organismos = []

    with open(caminho_do_arquivo) as file:
        for line in file:
            if line.startswith(">"):
                id_organismo, nome = line[1:].rstrip().split("|")
                organismos.append({
                    "id": id_organismo.strip(),
                    "nome": nome.strip(),
                    "sequencia": "",
                })
            else:
                organismos[-1]["sequencia"] += line.rstrip()

    return organismos
