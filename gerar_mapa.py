import pandas as pd
import os
import folium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def gerar_mapa_por_rubrica(dados):
    # Criar o diretório 'mapa_Localizacao' se não existir
    os.makedirs('mapa_Localizacao', exist_ok=True)
    # Remover espaços indesejados antes do caractere "-" na coluna 'RUBRICA'
    dados['RUBRICA'] = dados['RUBRICA'].str.strip()

    for categoria, grupo in dados.groupby('RUBRICA'):
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
            html_path = f"mapa_Localizacao/mapa_{categoria_limpa}.html"
            png_path = f"mapa_Localizacao/mapa_{categoria_limpa}.png"

            mapa.save(html_path)

            # Capturar uma imagem do mapa renderizado e salvar como PNG
            chrome_options = Options()
            chrome_options.add_argument("--headless")  # Executar em modo headless (sem janela)
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(f"file://{os.path.abspath(html_path)}")
            driver.save_screenshot(png_path)
            driver.quit