import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Conexão com o banco (ajuste a senha se necessário)
engine = create_engine('postgresql://postgres:123456@localhost:5432/iot_db')

# Função para carregar dados (Como sugerido no roteiro do PDF)
def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

st.set_page_config(page_title="Dashboard IoT UniFECAF", layout="wide")
st.title('📊 Dashboard de Temperaturas IoT')

try:
    # 1. Gráfico de Média por Dispositivo (Barra)
    st.header('Média de Temperatura por Dispositivo')
    df_estatisticas = load_data('view_estatisticas')
    fig1 = px.bar(df_estatisticas, x='dispositivo', y='media_temp', 
                 color='media_temp', color_continuous_scale='Reds')
    st.plotly_chart(fig1, use_container_width=True)

    # 2. Gráfico de Leituras por Hora (Linha)
    st.header('Leituras por Hora do Dia')
    df_temporal = load_data('view_temporal')
    fig2 = px.line(df_temporal, x='hora', y='contagem', 
                  title='Volume de Ingestão de Dados')
    st.plotly_chart(fig2, use_container_width=True)

    # 3. Gráfico de Máximas e Mínimas
    st.header('Temperaturas Máximas e Mínimas por Dispositivo')
    # Transformando os dados para o gráfico de linhas duplas
    fig3 = px.line(df_estatisticas, x='dispositivo', y=['max_temp', 'min_temp'],
                  markers=True, title="Variação Térmica")
    st.plotly_chart(fig3, use_container_width=True)

    # 4. Tabela de Dados Brutos (Para auditoria do professor)
    st.markdown("---")
    with st.expander("🔍 Visualizar Tabela de Anomalias (Temperaturas Críticas)"):
        df_anomalias = load_data('view_anomalias')
        st.write(f"Total de alertas encontrados: {len(df_anomalias)}")
        st.dataframe(df_anomalias, use_container_width=True)

except Exception as e:
    st.error(f"Erro ao carregar o dashboard: {e}")
    st.info("Certifique-se de que o Docker está rodando e as Views foram criadas.")

