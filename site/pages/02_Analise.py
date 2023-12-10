import streamlit as st

st.set_page_config(page_title="Analise", page_icon="‍💻", layout="wide")


# URL de incorporação do Power BI (substitua pelo seu URL de incorporação)
url_power_bi = "https://app.powerbi.com/view?r=eyJrIjoiYTUxMDg4ZjctMjFlNy00NTRkLWI2MmUtNzRiNWNkZDg4NzVlIiwidCI6IjlmMDY3ZGZhLWIxNWYtNDViZC1iNDllLTRjMTQ3ZTUwYTRlZCJ9"

# Exibir o relatório do Power BI no Streamlit usando um iframe
st.markdown(f'<iframe width="800" height="600" src="{url_power_bi}" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)