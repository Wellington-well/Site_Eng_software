import streamlit as st
import pandas as pd
import re
from datetime import datetime

# Função para validar a URL do jogo
def validar_url(url):
    pattern = r"https://store\.steampowered\.com/.+"
    return bool(re.match(pattern, url))

# Função para validar o formato da data
def validar_data(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False


# Se o arquivo não existir, cria um DataFrame vazio
df = pd.DataFrame(columns=['URL do Jogo', 'Nome do Jogo', 'Review do Jogo', 'Empresa que Publicou o Jogo',
                            'Tags do Jogo', 'Tipo de Jogo', 'Linguagens do Jogo', 'Gênero do Jogo',
                            'Descrição do Jogo', 'Preço do Jogo', 'Valor do Desconto', 'Data de Lançamento',
                            'Total de Conquistas', 'Empresa Desenvolvedora', 'Avaliação Geral'])

# Função para inserir os dados no DataFrame
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
        try:
            if not url_jogo or not validar_url(url_jogo):
                raise ValueError("URL do Jogo inválida. Deve ser https://store.steampowered.com/...")
            # Validação dos demais campos...
            
            # Criação do dicionário com os dados inseridos
            df['url'] = url_jogo
            df['types'] = "app"
            df['name'] = nome_jogo
            df['all_reviews'] = review_jogo
            df['publisher'] = empresa_publicadora
            df['popular_tags'] = tags_jogo
            df['game_details'] = tipo_jogo
            df['languages'] = linguas
            df['genre'] = genero
            df['game_description'] = descricao
            df['price'] = preco
            df['desconto'] = desconto
            df['data lancamento'] = data_lancamento
            df['conquistas'] = total_conquistas
            df['desenvolvedora'] = empresa_desenvolvedora
            df['avaliação geral'] = avaliacao_geral

            st.success("Dados inseridos no DataFrame.")
            # Salvar o DataFrame no arquivo CSV
            df.to_csv('Steam_games_tratada', index=False)  # Substitua pelo nome do seu arquivo CSV
        except ValueError as e:
            st.error(f"Erro: {e}")
        except Exception as e:
            st.error(f"Erro desconhecido: {e}")

# Chamando a função para inserir os dados
inserir_dados()
