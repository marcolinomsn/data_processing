# Análise de Dados e Boas Práticas em Ciência de Dados

Este repositório contém um projeto de MVP (Minimum Viable Product) desenvolvido como parte de um MBA em Ciência de Dados, focado na análise de dados históricos de estações meteorológicas do INMET (Instituto Nacional de Meteorologia) no Brasil.

## Objetivo do Projeto

O principal objetivo deste MVP é explorar e analisar a rede de estações meteorológicas do INMET, com foco em:

*   **Inventário da Rede:** Compreender a distribuição geográfica, o status operacional e o histórico de instalação das estações.
*   **Qualidade e Consistência dos Dados:** Avaliar a confiabilidade e a completude dos dados históricos de variáveis meteorológicas, como precipitação.
*   **Climatologia Sazonal:** Analisar padrões sazonais de variáveis climáticas, especialmente a chuva, em diferentes localidades do Brasil.

## Estrutura do Repositório

*   `Análise_de_Dados_e_Boas_Práticas_(40530010055_20250_01).ipynb`: O notebook principal do projeto, contendo o código Python para a coleta, limpeza, análise e visualização dos dados.
*   `dataset/`: (Opcional) Diretório para armazenar os dados brutos e processados do INMET.
*   `download_inmet.py/`: Script auxiliar para download do dataset.
*   `filtra_dataset.py/`: Script auxiliar para filtragem dos dados.

## Tecnologias Utilizadas

*   Python 3.11
*   Pandas (para manipulação e análise de dados)
*   NumPy (para operações numéricas)
*   Matplotlib/Seaborn (para visualização de dados)
*   Jupyter Notebook / Google Colab

## Como Executar o Projeto

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```
2.  **Instale as Dependências:**
    ```bash
    pip install pandas numpy matplotlib seaborn
    ```
3.  **Obtenha os Dados do INMET:**
    Os dados históricos do INMET podem ser obtidos diretamente em: https://www.kaggle.com/datasets/gregoryoliveira/brazil-weather-information-by-inmet

4.  **Execute o Notebook:**
    Abra o arquivo `Análise_de_Dados_e_Boas_Práticas_(40530010055_20250_01).ipynb` em um ambiente Jupyter (Jupyter Lab, Jupyter Notebook, Google Colab) e execute as células sequencialmente.
