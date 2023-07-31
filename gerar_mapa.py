import os
import pandas as pd
import folium


def gerar_mapa_por_rubrica(dados):
    # Criar o diretório 'mapa_Localização' se não existir
    os.makedirs('mapa_Localização', exist_ok=True)
    # Remover espaços indesejados antes do caractere "-" na coluna 'RUBRICA'
    dados['RUBRICA'] = dados['RUBRICA'].str.strip()

    for categoria, grupo in dados.groupby('CATEGORIA_RUBRICA'):
        # Verificar se as colunas 'LATITUDE' e 'LONGITUDE' estão presentes
        if 'LATITUDE' in grupo.columns and 'LONGITUDE' in grupo.columns:
            mapa = folium.Map(location=[-23.550520, -46.633308], zoom_start=12)
            for index, row in grupo.iterrows():
                if not pd.isna(row['LATITUDE']) and not pd.isna(row['LONGITUDE']):
                    periodo_rubrica = f"{row['PERIODOOCORRENCIA']} - {row['RUBRICA']}"
                    latitude = row['LATITUDE']
                    longitude = row['LONGITUDE']
                    folium.Marker([latitude, longitude], popup=periodo_rubrica).add_to(mapa)

            # Obter o caminho para salvar o arquivo HTML
            categoria_limpa = "".join(c for c in categoria if c.isalnum())  # Remover caracteres inválidos
            path = f"mapa_Localização/mapa_{categoria_limpa}.html"
            mapa.save(path)
