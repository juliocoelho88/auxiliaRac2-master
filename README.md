**README**

# Projeto auxiliaRac

O projeto auxiliaRac é uma aplicação Python desenvolvida para auxiliar na análise e visualização de dados de ocorrências de roubo no município de São Paulo. O objetivo principal é fornecer ferramentas para processar os dados de ocorrências, realizar contagens e gerar visualizações em mapas interativos, facilitando a identificação de padrões e insights relevantes.

## Funcionalidades

O projeto possui as seguintes funcionalidades:

1. **ler_dados_excel**: Essa função é responsável por ler os dados de ocorrências de roubo a partir de um arquivo Excel. Os dados são carregados em um DataFrame do Pandas, e algumas etapas de pré-processamento são realizadas para limpar e organizar os dados.

2. **remover_duplicatas_num_bo**: Essa função remove as duplicatas do DataFrame com base na coluna 'NUM_BO' (Número do Boletim de Ocorrência), garantindo que cada ocorrência seja contabilizada apenas uma vez.

3. **converter_logradouros_minuscula**: Essa função converte todas as entradas da coluna 'LOGRADOURO' para letras minúsculas, padronizando a formatação dos endereços.

4. **contar_ocorrencias_por_periodo**: Essa função realiza a contagem de ocorrências de roubo por período de ocorrência (data e hora).

5. **contar_ocorrencias_por_tipo_veiculo**: Essa função conta as ocorrências de roubo por tipo de veículo envolvido, ignorando placas iguais para evitar duplicações.

6. **contar_ocorrencias_por_marca_veiculo**: Essa função conta as ocorrências de roubo por marca de veículo envolvido, ignorando placas iguais para evitar duplicações.

7. **contar_ocorrencias_por_rubrica**: Essa função realiza a contagem de ocorrências de roubo por categoria de rubrica. As rubricas são agrupadas de acordo com um critério específico para simplificar a análise.

8. **contar_logradouros_por_rubrica**: Essa função realiza a contagem de logradouros únicos por categoria de rubrica, ajudando a identificar quais locais são mais propensos a ocorrências de roubo.

9. **gerar_mapa_por_rubrica**: Essa função gera mapas interativos com marcadores para visualizar as ocorrências de roubo por categoria de rubrica em diferentes áreas de São Paulo.

## Requisitos

Para executar o projeto, é necessário ter o Python instalado, juntamente com os seguintes pacotes:

- pandas: Biblioteca para manipulação e análise de dados.
- folium: Biblioteca para criação de mapas interativos.
- openpyxl: Biblioteca para leitura e escrita de arquivos Excel no formato .xlsx.

Você pode instalar os pacotes usando o comando `pip`:

```
pip install pandas folium openpyxl
```

## Como usar

1. Faça o clone do repositório para o seu ambiente local.

2. Certifique-se de que os requisitos estejam instalados.

3. Coloque o arquivo Excel contendo os dados de ocorrências no mesmo diretório do projeto ou forneça o caminho completo para o arquivo no script `main.py`.

4. Execute o script `main.py` para processar os dados e gerar os resultados.

5. Verifique os arquivos gerados no diretório 'mapa_Localização' para visualizar os mapas interativos.

## Contribuição

Se você quiser contribuir para o projeto, fique à vontade para abrir uma "Issue" ou enviar um "Pull Request" com as suas sugestões ou correções. Toda contribuição é bem-vinda!

## Licença

Este projeto é licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.

## Contato

Em caso de dúvidas ou problemas, você pode entrar em contato com o desenvolvedor:

Nome: [Julio Cesar Coelho]
E-mail: [julio.alemao8825@gmail]
