# import streamlit as st
# import re
# from datetime import datetime

# # Função para validar a URL do jogo
# def validar_url(url):
#     pattern = r"https://store\.steampowered\.com/agecheck/app/\d+/?"
#     return bool(re.match(pattern, url))

# # Função para validar o formato da data
# def validar_data(data):
#     try:
#         datetime.strptime(data, '%d/%m/%Y')
#         return True
#     except ValueError:
#         return False

# # Função para exibir o formulário e validar os dados
# def inserir_dados():
#     st.header("Inserir Dados do Jogo")
    
#     url_jogo = st.text_input("URL do Jogo")
#     nome_jogo = st.text_input("Nome do Jogo")
#     review_jogo = st.text_area("Review do Jogo")
#     empresa_publicadora = st.text_input("Empresa que Publicou o Jogo")
#     tags_jogo = st.text_input("Tags do Jogo")
#     tipo_jogo = st.selectbox("Tipo de Jogo", ["Multiplayer", "Single Player"])
#     linguas = st.text_input("Linguagens do Jogo")
#     genero = st.text_input("Gênero do Jogo")
#     descricao = st.text_area("Descrição do Jogo")
#     preco = st.number_input("Preço do Jogo", format="%.2f")
#     desconto = st.number_input("Valor do Desconto", format="%.2f")
#     data_lancamento = st.text_input("Data de Lançamento (DD/MM/AAAA)")
#     total_conquistas = st.number_input("Total de Conquistas", format="%d")
#     empresa_desenvolvedora = st.text_input("Empresa Desenvolvedora")
#     avaliacao_geral = st.text_input("Avaliação Geral do Jogo")

#     if (url_jogo and validar_url(url_jogo) and nome_jogo and empresa_publicadora and
#             tags_jogo and tipo_jogo and linguas and genero and preco is not None and
#             desconto is not None and data_lancamento and validar_data(data_lancamento) and
#             isinstance(total_conquistas, int) and empresa_desenvolvedora and avaliacao_geral):
        
#         st.success("Dados válidos. Inserção permitida.")
#         # Aqui você pode inserir os dados em um banco de dados ou fazer o que desejar com eles
#     else:
#         st.error("Houve um erro nas informações. Por favor, verifique e insira novamente.")

# # Chamando a função para inserir os dados
# inserir_dados()

# import streamlit as st
# import re
# from datetime import datetime

# # Função para validar a URL do jogo
# def validar_url(url):
#     pattern = r"https://store\.steampowered\.com/agecheck/app/\d+/?"
#     return bool(re.match(pattern, url))

# # Função para validar o formato da data
# def validar_data(data):
#     try:
#         datetime.strptime(data, '%d/%m/%Y')
#         return True
#     except ValueError:
#         return False

# # Função para exibir o formulário e validar os dados
# def inserir_dados():
#     st.header("Inserir Dados do Jogo")
    
#     url_jogo = st.text_input("URL do Jogo")
#     nome_jogo = st.text_input("Nome do Jogo")
#     review_jogo = st.text_area("Review do Jogo")
#     empresa_publicadora = st.text_input("Empresa que Publicou o Jogo")
#     tags_jogo = st.text_input("Tags do Jogo")
#     tipo_jogo = st.selectbox("Tipo de Jogo", ["Multiplayer", "Single Player"])
#     linguas = st.text_input("Linguagens do Jogo")
#     genero = st.text_input("Gênero do Jogo")
#     descricao = st.text_area("Descrição do Jogo")
#     preco = st.number_input("Preço do Jogo", format="%.2f")
#     desconto = st.number_input("Valor do Desconto", format="%.2f")
#     data_lancamento = st.text_input("Data de Lançamento (DD/MM/AAAA)")
#     total_conquistas = st.number_input("Total de Conquistas", format="%d")
#     empresa_desenvolvedora = st.text_input("Empresa Desenvolvedora")
#     avaliacao_geral = st.text_input("Avaliação Geral do Jogo")
    
#     if st.button("Inserir"):
#         if (url_jogo and validar_url(url_jogo) and nome_jogo and empresa_publicadora and
#                 tags_jogo and tipo_jogo and linguas and genero and preco is not None and
#                 desconto is not None and data_lancamento and validar_data(data_lancamento) and
#                 isinstance(total_conquistas, int) and empresa_desenvolvedora and avaliacao_geral):
            
#             st.success("Dados válidos. Inserção permitida.")
#             # Aqui você pode inserir os dados em um banco de dados ou fazer o que desejar com eles
#         else:
#             st.error("Houve um erro nas informações. Por favor, verifique e insira novamente.")

# # Chamando a função para inserir os dados
# inserir_dados()


import streamlit as st
import pandas as pd
import re
from datetime import datetime

st.set_page_config(page_title="Inserção dos dados", page_icon="🎲", layout="wide")

# Função para validar a URL do jogo
def validar_url(url):
    pattern = r"https://store\.steampowered\.com/agecheck/app/\d+/?"
    return bool(re.match(pattern, url))

# Função para validar o formato da data
def validar_data(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False

# Carregar ou criar o DataFrame onde as URLs serão armazenadas
# Este é um exemplo simples, você pode carregar um DataFrame existente ou criar um novo
try:
    # Tentar carregar o DataFrame existente
    df = pd.read_csv('Steam_games_tratada.csv')  # Substitua pelo nome do seu arquivo CSV
except FileNotFoundError:
    # Se o arquivo não existir, cria um DataFrame vazio
    df = pd.DataFrame(columns=['url'])

# Função para verificar se a URL já existe no DataFrame
def verificar_existencia_url(url):
    return url in df['url'].values

# Função para exibir o formulário e validar os dados
def inserir_dados():
    st.header("Inserir Dados do Jogo")
    
    url_jogo = st.text_input("URL do Jogo")
    nome_jogo = st.text_input("Nome do Jogo")
    review_jogo = st.text_area("Review do Jogo")
    empresa_publicadora = st.text_input("Empresa que Publicou o Jogo")
    tags_jogo = st.text_input("Tags do Jogo")
    tipo_jogo = st.selectbox("Tipo de Jogo", ["Multiplayer", "Single Player"])
    linguas = st.text_input("Linguagens do Jogo")
    genero = st.text_input("Gênero do Jogo")
    descricao = st.text_area("Descrição do Jogo")
    preco = st.number_input("Preço do Jogo", format="%.2f")
    desconto = st.number_input("Valor do Desconto", format="%.2f")
    data_lancamento = st.text_input("Data de Lançamento (DD/MM/AAAA)")
    total_conquistas = st.number_input("Total de Conquistas", format="%d")
    empresa_desenvolvedora = st.text_input("Empresa Desenvolvedora")
    avaliacao_geral = st.text_input("Avaliação Geral do Jogo")

    if st.button("Inserir"):
        if (url_jogo and validar_url(url_jogo) and not verificar_existencia_url(url_jogo) and
                nome_jogo and empresa_publicadora and tags_jogo and tipo_jogo and linguas and
                genero and preco is not None and desconto is not None and data_lancamento and
                validar_data(data_lancamento) and isinstance(total_conquistas, int) and
                empresa_desenvolvedora and avaliacao_geral):
            
            st.success("Dados válidos. Inserção permitida.")
            # Aqui você pode inserir os dados no DataFrame e salvar no arquivo CSV
            # df = df.append({'URL do Jogo': url_jogo, 'Nome do Jogo': nome_jogo, ...}, ignore_index=True)
            # df.to_csv('dados_jogos.csv', index=False)  # Salvar o DataFrame no arquivo CSV
        elif verificar_existencia_url(url_jogo):
            st.error("Essa URL já existe no DataFrame.")
        else:
            st.error("Houve um erro nas informações. Por favor, verifique e insira novamente.")

# Chamando a função para inserir os dados
inserir_dados()
