import pandas as pd
import streamlit as st
import plotly.express as px


df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")

df_limpo = df.dropna()

st.set_page_config(
    page_title="Imersão Dados com Python | Alura",
    page_icon="📊",
    layout="wide",
)

with st.expander("🔍 Filtros", expanded=False):

    col1, col2 = st.columns(2)

    with col1:
        anos_selecionados = st.multiselect(
            "Ano",
            sorted(df_limpo['ano'].unique()),
            default=sorted(df_limpo['ano'].unique())
        )

        contratos_selecionados = st.multiselect(
            "Tipo de Contrato",
            sorted(df_limpo['contrato'].unique()),
            default=sorted(df_limpo['contrato'].unique())
        )

    with col2:
        senioridades_selecionadas = st.multiselect(
            "Senioridade",
            sorted(df_limpo['senioridade'].unique()),
            default=sorted(df_limpo['senioridade'].unique())
        )

        tamanhos_selecionados = st.multiselect(
            "Tamanho da Empresa",
            sorted(df_limpo['tamanho_empresa'].unique()),
            default=sorted(df_limpo['tamanho_empresa'].unique())
        )

df_filtrado = df_limpo[
    (df_limpo['ano'].isin(anos_selecionados)) &
    (df_limpo['senioridade'].isin(senioridades_selecionadas)) &
    (df_limpo['contrato'].isin(contratos_selecionados)) &
    (df_limpo['tamanho_empresa'].isin(tamanhos_selecionados))
]
st.title("🎲 Analisando - Área de Dados")
st.markdown("Aqui você pode explorar os salários na área de dados ao longo dos últimos anos, com base em dados do mundo todo.")
st.subheader("Métricas gerais (Salário anual em USD)")

if not df_filtrado.empty:
    salario_medio = df_filtrado['usd'].mean()
    salario_maximo = df_filtrado['usd'].max()
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado["cargo"].mode()[0]
else:
    salario_medio, salario_mediano, salario_maximo, total_registros, cargo_mais_comum = 0, 0, 0, ""

col1, col2, col3, col4 = st.columns(4)
col1.metric("Salário médio anual", f"${salario_medio:,.0f}")
col2.metric("Salário máximo anual", f"${salario_maximo:,.0f}")
col3.metric("Total de registros", f"{total_registros:,}")
col4.metric("Cargo mais frequente", cargo_mais_frequente)

st.markdown("---")

st.subheader("Gráficos")

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    if not df_filtrado.empty:
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        grafico_cargos = px.bar(
            top_cargos,
            x='usd',
            y='cargo',
            orientation='h',
            title="Top 10: Cargos / Salário médio",
            labels={'usd': 'Média salarial anual (USD)', 'cargo': ''},
            color_discrete_sequence=["#4B0202"]
        )
        grafico_cargos.update_layout(title_x=0.1, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de cargos.")

with col_graf2:
    if not df_filtrado.empty:
        grafico_hist = px.histogram(
            df_filtrado,
            x='usd',
            nbins=30,
            title="Distribuição de salários anuais",
            labels={'usd': 'Faixa salarial (USD)', 'count': 'Quantidade'},
            color_discrete_sequence=["#4B0202"]
        )
        grafico_hist.update_traces(
        marker_line_color='black', 
        marker_line_width=1
        )
        grafico_hist.update_layout(title_x=0.1)
        st.plotly_chart(grafico_hist, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de distribuição.")

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtrado.empty:
        remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
        grafico_remoto = px.pie(
            remoto_contagem,
            names='tipo_trabalho',
            values='quantidade',
            title='Modelos de trabalho',
            hole=0.2,
            color_discrete_sequence=px.colors.sequential.Reds_r,
            labels={
                'presencial': 'Presencial',
                'remoto': 'Remoto',
                'hibrido': 'Híbrido'
            }
        )
        grafico_remoto.update_traces(
            textinfo='percent+label',
            marker=dict(line=dict(color='#000000', width=1))
        )
        grafico_remoto.update_traces(textinfo='percent+label')
        grafico_remoto.update_layout(title_x=0.1)
        st.plotly_chart(grafico_remoto, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho.")

with col_graf4:
    if not df_filtrado.empty:
        df_media_salarial = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index()

        fig = px.bar(df_media_salarial,
             x='senioridade',
             y='usd',
             title='Média Salarial Anual por Nível de Experiência (USD)',
             labels={
                'senioridade': 'Nível de Experiência',
                'usd': 'Média Salarial Anual (USD)',
                'executivo': 'Executivo',
                'senior': 'Senior',
                'pleno': 'Pleno',
                'junior': 'Junior'},
             template='plotly_white',
             color_discrete_sequence=["#4B0202"]
            ) 
        fig.update_layout(title_x=0.1)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de países.")

st.subheader("Dados Detalhados")
st.dataframe(df_filtrado)