"""
    Arquivo main do projeto, contendo toda a lógica de execução do programa, desde a extração dos dados das planilhas, transformação e verificação dos dados até a geração do arquivo de saída.
"""
# Importando bibliotecas necessárias
import pandas as pd
import os, sys, re

# Informações sobre o programa
__author__ = "Rafael Malcervelli"
__version__ = "1.0.0"
__email__ = "r.malcervelli@gmail.com"

def get_files():
    """
        Função para obter os arquivos de entrada do programa
    """
    files = []
    for file in os.listdir("files"):
        if file.endswith(".xlsx"):
            files.append(file)
    return files

# Função principal do programa
def main():
    files = get_files()
    a_list_car = files[0]
    b_list_cp  = files[1]

    # Lendo os arquivos de entrada
    df_a_list_car = pd.read_excel("files/" + a_list_car)
    df_b_list_cp  = pd.read_excel("files/" + b_list_cp)

    # Criando um dicionário para armazenar os dados
    dict_all = {"maker": [], "model": [], "year": [], "type": []}

    # Percorrendo a coluna "pasted" do arquivo e separando os dados
    for row in df_b_list_cp["pasted"]:
        try:
            row_list = row.split("$")
            for car in row_list:
                car = car.title()
                help_list = re.split(r' |@#', car)

                if len(help_list) == 4:
                    dict_all["maker"].append(help_list[0])
                    dict_all["model"].append(help_list[1])
                    dict_all["year"].append(help_list[2])
                    dict_all["type"].append(help_list[3])

                elif len(help_list) > 4:
                    count = 2
                    model = help_list[count]

                    while len(help_list[count]) != 4:
                        count += 1
                        model += " " + help_list[count]
                    
                    dict_all["maker"].append(help_list[0])
                    dict_all["model"].append(model)
                    dict_all["year"].append(help_list[count])
                    string_type = help_list[count+1:]
                    dict_all["type"].append(" ".join(string_type))
        except:
            dict_all["maker"].append("NaN")
            dict_all["model"].append("NaN")
            dict_all["year"].append("NaN")
            dict_all["type"].append("NaN")
    
    # Criando um dataframe com os dados finais
    # Salvando o dataframe em um arquivo csv, pois o formato excel não permite a criação de arquivos com mais de 1 milhão de linhas
    df_final = pd.DataFrame(dict_all)
    df_final.to_csv("./final.csv", index=False) 

if __name__ == "__main__":
    main()