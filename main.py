from funcoes import *

if __name__ == "__main__":
    # Substitua 'caminho/do/arquivo.xlsx' pelo caminho do seu arquivo Excel
    arquivo_excel_original = r'C:\Users\julio\PycharmProjects\auxiliaRac2-master\ExportCompleto.xlsx'
    arquivo_excel_modificado = r'C:\Users\julio\PycharmProjects\auxiliaRac2-master\ExportCompleto_Modificado.xlsx'

    # Criar o arquivo modificado, substituindo as rubricas no arquivo original
    criar_arquivo_modificado(arquivo_excel_original, arquivo_excel_modificado)

    # Ler os dados do arquivo modificado
    dados = ler_dados_excel(arquivo_excel_modificado)

    # Remover duplicatas da coluna 'NUM_BO'
    dados = remover_duplicatas_num_bo(dados)

    # Converter todas as entradas da coluna 'LOGRADOURO' para letras minúsculas
    dados = converter_logradouros_minuscula(dados)

    # Realizar as contagens
    contagem_periodo = contar_ocorrencias_por_periodo(dados)
    contagem_tipo_veiculo = contar_ocorrencias_por_tipo_veiculo(dados)
    contagem_marca_veiculo = contar_ocorrencias_por_marca_veiculo(dados)
    contagem_rubrica = contar_ocorrencias_por_rubrica(dados)
    contagem_logradouro_por_rubrica = contar_logradouros_por_rubrica(dados)

    # Imprimir a contagem de ocorrências por rubrica e período
    print("Contagem de ocorrências por rubrica e período:")
    for rubrica, grupo in dados.groupby('RUBRICA'):
        print(f"\nRubrica: {rubrica}")
        print(grupo['PERIODOOCORRENCIA'].value_counts())

    # Imprimir a contagem de ocorrências por tipo de veículo (ignorando placas iguais)
    print("\nContagem de ocorrências por tipo de veículo:")
    print(contagem_tipo_veiculo)

    # Imprimir a contagem de ocorrências por marca de veículo (ignorando placas iguais)
    print("\nContagem de ocorrências por marca de veículo:")
    print(contagem_marca_veiculo)

    # Imprimir a contagem de ocorrências por rubrica
    print("\nContagem de ocorrências por rubrica:")
    print(contagem_rubrica)

    # Imprimir a contagem de logradouros por rubrica
    print("\nContagem de logradouros por rubrica:")
    for rubrica, contagem_logradouro in contagem_logradouro_por_rubrica.items():
        print(f"\nRubrica: {rubrica}")
        print(contagem_logradouro)

    # Imprimir a soma total de ocorrências por período
    print("\nSoma total de ocorrências por período:")
    print(contagem_periodo.sum())

    # Imprimir a soma total de ocorrências por tipo de veículo
    print("\nSoma total de ocorrências por tipo de veículo:")
    print(contagem_tipo_veiculo.sum())

    # Imprimir a soma total de ocorrências por marca de veículo
    print("\nSoma total de ocorrências por marca de veículo:")
    print(contagem_marca_veiculo.sum())

    # Imprimir a soma total de ocorrências por rubrica
    print("\nSoma total de ocorrências por rubrica:")
    print(contagem_rubrica.sum())

    # Imprimir a contagem de ocorrências por rubrica e período apenas para 'Roubo - VEICULO'
    print("Contagem de ocorrências por rubrica e período (Roubo - VEICULO):")
    print(dados[dados['RUBRICA'] == 'ROUBO - VEICULO']['PERIODOOCORRENCIA'].value_counts())

    # Imprimir a contagem de logradouros por rubrica apenas para 'Roubo - VEICULO'
    print("\nContagem de logradouros por rubrica (Roubo - VEICULO):")
    print(contagem_logradouro_por_rubrica['ROUBO - VEICULO'])

    # Antes de contar os logradouros por rubrica, normalizar as strings para letras maiúsculas
    dados['RUBRICA'] = dados['RUBRICA'].str.upper()

    # Em seguida, chame a função contar_logradouros_por_rubrica
    contagem_logradouro_por_rubrica = contar_logradouros_por_rubrica(dados)

    # Agora você pode imprimir a contagem de logradouros para a rubrica "Roubo - VEICULO"
    print("\nContagem de logradouros por rubrica (Roubo - VEICULO):")
    print(contagem_logradouro_por_rubrica['ROUBO - VEICULO'])
