import pandas as pd

def criar_arquivo_modificado(arquivo_origem, arquivo_destino):
    # Ler os dados do arquivo original
    df = pd.read_excel(arquivo_origem)

    # Realizar as modificações na coluna 'RUBRICA'
    df['RUBRICA'] = df['RUBRICA'].str.strip()
    df['RUBRICA'] = df['RUBRICA'].str.replace('Roubo (art. 157)                                                                 - VEICULO', 'ROUBO - VEICULO')
    df['RUBRICA'] = df['RUBRICA'].str.replace('Roubo (art. 157)                                                                 - INTERIOR DE VEICULO', 'ROUBO - OUTROS')
    df['RUBRICA'] = df['RUBRICA'].str.replace('Roubo (art. 157)                                                                 - TRANSEUNTE', 'ROUBO - OUTROS')
    df['RUBRICA'] = df['RUBRICA'].str.replace('Roubo (art. 157)                                                                 - OUTROS', 'ROUBO - OUTROS')
    df['RUBRICA'] = df['RUBRICA'].str.replace('Roubo (art. 157)                                                                 - ESTABELECIMENTO COMERCIAL', 'ROUBO - OUTROS')
    df['RUBRICA'] = df['RUBRICA'].str.replace('Furto (art. 155)                                                                 - VEICULO', 'FURTO - VEICULO')
    df['RUBRICA'] = df['RUBRICA'].str.replace('Furto (art. 155)                                                                 - INTERIOR DE VEICULO', 'FURTO - OUTROS')
    df['RUBRICA'] = df['RUBRICA'].str.replace('Furto (art. 155)                                                                 - TRANSEUNTE', 'FURTO - OUTROS')
    df['RUBRICA'] = df['RUBRICA'].str.replace('Furto (art. 155)                                                                 - OUTROS', 'FURTO - OUTROS')
    df['RUBRICA'] = df['RUBRICA'].str.replace('Furto (art. 155)                                                                 - ESTABELECIMENTO COMERCIAL', 'FURTO - OUTROS')
    df['RUBRICA'] = df['RUBRICA'].str.replace('Furto (art. 155)                                                                 - INTERIOR TRANSPORTE COLETIVO', 'FURTO - OUTROS')
    df['RUBRICA'] = df['RUBRICA'].str.replace('Furto (art. 155)                                                                 - INTERIOR ESTABELECIMENTO', 'FURTO - OUTROS')
    df['RUBRICA'] = df['RUBRICA'].str.replace('Furto (art. 155)                                                                 - ESTABELECIMENTO-OUTROS', 'FURTO - OUTROS')
    df['RUBRICA'] = df['RUBRICA'].str.replace('Furto (art. 155)                                                                 - ESTABELECIMENTO ENSINO', 'FURTO - OUTROS')
    df['RUBRICA'] = df['RUBRICA'].str.replace('A.I.-Furto (art. 155)                                                            - OUTROS', 'FURTO - OUTROS')
    df['RUBRICA'] = df['RUBRICA'].str.replace('A.I.-Furto (art. 155)                                                            - VEICULO', 'FURTO - OUTROS')



    # Salvar o novo arquivo com as modificações
    df.to_excel(arquivo_destino, index=False)

    print("Novo arquivo gerado com sucesso:", arquivo_destino)

def ler_dados_excel(arquivo_excel):
    df = pd.read_excel(arquivo_excel, usecols=['NUM_BO', 'PERIODOOCORRENCIA', 'LATITUDE', 'LONGITUDE', 'LOGRADOURO', 'RUBRICA', 'PLACA_VEICULO', 'DESCR_TIPO_VEICULO', 'DESCR_MARCA_VEICULO'])

    # Realizar as modificações na coluna 'RUBRICA'
    df['RUBRICA'] = df['RUBRICA'].str.strip()

    return df

def remover_duplicatas_num_bo(dados):
    dados = dados.drop_duplicates(subset=['NUM_BO'])
    return dados

def converter_logradouros_maiuscula(dados):
    dados['LOGRADOURO'] = dados['LOGRADOURO'].str.upper()

    if dados['LATITUDE'].dtype == 'O':
        dados['LATITUDE'] = dados['LATITUDE'].str.replace(',', '.').astype(float)
        dados['LATITUDE'] = pd.to_numeric(dados['LATITUDE'], errors='coerce')

    if dados['LONGITUDE'].dtype == 'O':
        dados['LONGITUDE'] = dados['LONGITUDE'].str.replace(',', '.').astype(float)
        dados['LONGITUDE'] = pd.to_numeric(dados['LONGITUDE'], errors='coerce')

    return dados

def contar_ocorrencias_por_periodo(dados):
    contagem_periodo = dados['PERIODOOCORRENCIA'].value_counts()
    return contagem_periodo

def contar_ocorrencias_por_tipo_veiculo(dados):
    dados_deduplicated = dados.drop_duplicates(subset=['PLACA_VEICULO', 'DESCR_TIPO_VEICULO', 'RUBRICA'])
    contagem_tipo_veiculo = dados_deduplicated.groupby(['RUBRICA', 'DESCR_TIPO_VEICULO']).size()
    return contagem_tipo_veiculo


def contar_ocorrencias_por_marca_veiculo(dados):
    # Filtra os dados apenas com as Rubricas "Roubo - VEICULO" e "Furto - VEICULO"
    dados_filtered = dados[(dados['RUBRICA'] == 'ROUBO - VEICULO') | (dados['RUBRICA'] == 'FURTO - VEICULO')]

    # Conta as ocorrências de cada marca de veículo separadamente para cada rubrica
    contagem_marca_veiculo = dados_filtered.groupby(['RUBRICA', 'DESCR_MARCA_VEICULO']).size()

    return contagem_marca_veiculo


def contar_ocorrencias_por_rubrica(dados):
    dados['RUBRICA'] = dados['RUBRICA'].str.strip()
    contagem_rubrica = dados['RUBRICA'].value_counts()
    return contagem_rubrica

def contar_logradouros_por_rubrica(dados):
    contagem_logradouro_por_rubrica = {}
    for rubrica, grupo in dados.groupby('RUBRICA'):
        if rubrica == 'ROUBO - VEICULO':
            contagem_logradouro_por_rubrica[rubrica] = grupo['LOGRADOURO'].value_counts()
        else:
            contagem_logradouro_por_rubrica[rubrica] = grupo.drop_duplicates(subset=['NUM_BO'])['LOGRADOURO'].value_counts()
    return contagem_logradouro_por_rubrica
