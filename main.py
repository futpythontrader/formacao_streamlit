import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Configuração Inicial do Aplicativo
st.set_page_config(
    page_title="Básico de Streamlit",
    page_icon="📊",
    layout="wide"
)

# Criação do Dataframe
def criar_dataframe():
    np.random.seed(42)
    n = 100
    dados = pd.DataFrame({
        'data': pd.date_range(start='2024-01-01', periods=n, freq='D'),
        'escola': np.random.choice(['Escola A','Escola B','Escola C','Escola D','Escola E'], n),
        'disciplina': np.random.choice(['Física','Matemática','Química','Biologia','Português'], n),
        'nota': np.random.normal(7, 1.5, n),
        'alunos': np.random.randint(20, 50, n)
    })
    dados['nota'] = dados['nota'].clip(0,10)
    dados['alunos'] = dados['alunos'].astype(int)

    return dados

df = criar_dataframe()


# Função Principal do Streamlit
def main():
    # Título
    st.title("📊 Fundamentos do Streamlit")
    # Descrição
    st.markdown("""
##### Este aplicativo demonstra conceitos básicos do Streamlit para a criação de Dashboards interativos.
                """)
    # Barra Lateral
    with st.sidebar:
        st.header("Configurações")

        # Criar Seleção Multipla para as Escolas
        escola_selecionada = st.multiselect(
            "Selecione as Escolas",
            ['Escola A','Escola B','Escola C','Escola D','Escola E'],
            default='Escola A'
        )

        # Criar Seleção Unica para a Disciplina
        disciplina_selecionada = st.selectbox(
            "Selecione a Disciplina",
            ['Física','Matemática','Química','Biologia','Português'],
        )

        # Criar Seleção da Data
        data_inicio = st.date_input(
            "Data Inicial",
            datetime(2024, 1, 1)
        )

        data_fim = st.date_input(
            "Data Final",
            datetime(2024, 12, 31)
        )

    # Filtrar o dataframe
    dados_filtrados = df[
        (df['escola'].isin(escola_selecionada)) &
        (df['disciplina'] == disciplina_selecionada) & 
        (df['data'].dt.date >= data_inicio) & 
        (df['data'].dt.date <= data_fim)
    ]

    st.dataframe(dados_filtrados)
    
    # Cria um layout em duas colunas para criar os graficos
    col1, col2 = st.columns(2)

    with col1:
        fig_line = px.line(
            dados_filtrados,
            x='data',
            y='nota',
            color='escola',
            title = "Evolução das Notas por Escolas"
        )
        st.plotly_chart(fig_line, use_container_width=True)

    with col2:
        # st.metric(
        #     "Média Geral",
        #     f"{dados_filtrados['nota'].mean():.2f}"
        # )
        # st.metric(
        #     "Total de Alunos",
        #     f"{dados_filtrados['alunos'].sum():.2f}"
        # )
        
        fig_box = px.box(
            dados_filtrados,
            x='escola',
            y='nota',
            title='Distribuição de Notas por Escola'
        )
        st.plotly_chart(fig_box, use_container_width=True)




















if __name__ == "__main__":
    main() 