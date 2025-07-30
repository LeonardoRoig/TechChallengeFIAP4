
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados
df = pd.read_csv("Obesidade_BI.csv")

# Mapeamento dos níveis de obesidade
obesity_map = {
    0: "Abaixo do Peso",
    1: "Normal",
    2: "Sobrepeso",
    3: "Obeso"
}
df["obesidade"] = df["obesidade"].astype(int)
df["categoria_obesidade"] = df["obesidade"].map(obesity_map)

st.title("Estudo sobre Obesidade")

st.markdown("Este painel interativo tem como objetivo explorar os fatores associados aos diferentes níveis de obesidade com base em dados coletados. Os gráficos a seguir analisam distribuição de peso, gênero, hábitos alimentares e estilo de vida.")

# Gráfico de pizza por categoria
st.subheader("Distribuição percentual dos níveis de obesidade")
st.markdown("Abaixo vemos a distribuição geral da população da amostra de acordo com os níveis de obesidade.")
fig1, ax1 = plt.subplots()
df["categoria_obesidade"].value_counts(normalize=True).plot.pie(autopct="%1.1f%%", startangle=90, ax=ax1)
ax1.set_ylabel("")
st.pyplot(fig1)

# Gráfico de barras por gênero
st.subheader("Distribuição da obesidade por gênero")
st.markdown("Este gráfico mostra a relação entre gênero e obesidade. Podemos observar o número de indivíduos masculinos e femininos em cada faixa de peso.")
genero_data = df.groupby(["categoria_obesidade", "feminino"]).size().unstack().fillna(0)
genero_data.columns = ["Masculino", "Feminino"] if genero_data.shape[1] == 2 else genero_data.columns
fig2, ax2 = plt.subplots()
genero_data.plot(kind="bar", ax=ax2)
ax2.set_xlabel("Categoria de Obesidade")
ax2.set_ylabel("Número de Pessoas")
plt.xticks(rotation=0)
st.pyplot(fig2)

# Boxplot de refeições principais por obesidade
st.subheader("Refeições principais por categoria de obesidade")
st.markdown("Este boxplot mostra a distribuição do número de refeições principais por dia em cada categoria de obesidade.")
df["ref_principais"] = pd.to_numeric(df["ref_principais"], errors="coerce")
fig3, ax3 = plt.subplots()
sns.boxplot(x="categoria_obesidade", y="ref_principais", data=df, ax=ax3)
ax3.set_xlabel("Categoria de Obesidade")
ax3.set_ylabel("Refeições Principais por Dia")
st.pyplot(fig3)

# Gráfico empilhado de entre_ref
st.subheader("Pessoas que comem entre as refeições por categoria de obesidade")
st.markdown("Este gráfico mostra quantas pessoas relatam comer entre as refeições em cada nível de obesidade.")
df["entre_ref"] = pd.to_numeric(df["entre_ref"], errors="coerce")
entre_ref_data = df.groupby("categoria_obesidade")["entre_ref"].value_counts().unstack().fillna(0)
entre_ref_data.columns = ["Não come entre refeições", "Come entre refeições"] if 0 in entre_ref_data.columns else entre_ref_data.columns
fig4, ax4 = plt.subplots()
entre_ref_data.plot(kind="bar", stacked=True, ax=ax4)
ax4.set_xlabel("Categoria de Obesidade")
ax4.set_ylabel("Número de Pessoas")
plt.xticks(rotation=0)
st.pyplot(fig4)

# Novo gráfico: Consumo de vegetais por categoria
st.subheader("Consumo de vegetais por categoria de obesidade")
st.markdown("O gráfico abaixo mostra a média do consumo de vegetais em cada categoria de obesidade. Níveis mais altos podem indicar alimentação mais saudável.")
df["vegetais"] = pd.to_numeric(df["vegetais"], errors="coerce")
fig5, ax5 = plt.subplots()
df.groupby("categoria_obesidade")["vegetais"].mean().plot(kind="bar", ax=ax5)
ax5.set_xlabel("Categoria de Obesidade")
ax5.set_ylabel("Consumo Médio de Vegetais (Escala 0–3)")
plt.xticks(rotation=0)
st.pyplot(fig5)

# Novo gráfico: Atividade física por obesidade
st.subheader("Atividade física por categoria de obesidade")
st.markdown("O gráfico mostra a média de prática de atividade física nas diferentes faixas de obesidade.")
df["atv_fisica"] = pd.to_numeric(df["atv_fisica"], errors="coerce")
fig6, ax6 = plt.subplots()
df.groupby("categoria_obesidade")["atv_fisica"].mean().plot(kind="bar", ax=ax6)
ax6.set_xlabel("Categoria de Obesidade")
ax6.set_ylabel("Nível médio de atividade física (Escala 0–3)")
plt.xticks(rotation=0)
st.pyplot(fig6)
