
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

# Conversões numéricas
cols = ["ref_principais", "entre_ref", "vegetais", "atv_fisica", "atv_eletronica", "agua", "alcool", "historico"]
for col in cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

st.title("Estudo sobre Obesidade")

st.markdown("Este painel analisa hábitos alimentares, atividades e histórico familiar em relação aos diferentes níveis de obesidade.")

# Gráfico 1: Distribuição de obesidade
st.subheader("Distribuição percentual dos níveis de obesidade")
st.markdown("Mostra a proporção geral da população analisada em cada grupo de peso.")
fig1, ax1 = plt.subplots()
df["categoria_obesidade"].value_counts(normalize=True).plot.pie(autopct="%1.1f%%", startangle=90, ax=ax1, colors=sns.color_palette("Blues"))
ax1.set_ylabel("")
st.pyplot(fig1)

# Gráfico 2: Barras por gênero
st.subheader("Distribuição da obesidade por gênero")
st.markdown("Mostra a quantidade de homens e mulheres presentes em cada categoria de obesidade.")
genero_data = df.groupby(["categoria_obesidade", "feminino"]).size().unstack().fillna(0)
genero_data.columns = ["Masculino", "Feminino"]
fig2, ax2 = plt.subplots()
genero_data.plot(kind="bar", ax=ax2, color=sns.color_palette("Blues")[:2])
ax2.set_xlabel("Categoria de Obesidade")
ax2.set_ylabel("Número de Pessoas")
plt.xticks(rotation=0)
st.pyplot(fig2)

# Gráfico 3: Refeições principais por categoria (barplot com erro padrão)
st.subheader("Refeições principais por categoria de obesidade")
st.markdown("Média de refeições principais consumidas por dia, com barras de erro.")
fig3, ax3 = plt.subplots()
sns.barplot(x="categoria_obesidade", y="ref_principais", data=df, ax=ax3, palette="Blues", ci="sd")
ax3.set_xlabel("Categoria de Obesidade")
ax3.set_ylabel("Média de Refeições Principais")
st.pyplot(fig3)

# Gráfico 4: Entre refeições
st.subheader("Pessoas que comem entre as refeições por categoria de obesidade")
st.markdown("Número de pessoas que consomem alimentos entre refeições por nível de obesidade.")
entre_ref_data = df.groupby("categoria_obesidade")["entre_ref"].value_counts().unstack().fillna(0)
entre_ref_data.columns = ["Não come entre refeições", "Come entre refeições"]
fig4, ax4 = plt.subplots()
entre_ref_data.plot(kind="bar", stacked=True, ax=ax4, color=sns.color_palette("Blues")[1:3])
ax4.set_xlabel("Categoria de Obesidade")
ax4.set_ylabel("Número de Pessoas")
plt.xticks(rotation=0)
st.pyplot(fig4)

# Gráfico 5: Consumo de vegetais
st.subheader("Consumo de vegetais por categoria de obesidade")
st.markdown("Consumo médio de vegetais por faixa de obesidade. Escala de 0 (baixo) a 3 (alto).")
fig5, ax5 = plt.subplots()
df.groupby("categoria_obesidade")["vegetais"].mean().plot(kind="bar", ax=ax5, color=sns.color_palette("Blues")[2])
ax5.set_xlabel("Categoria de Obesidade")
ax5.set_ylabel("Consumo Médio de Vegetais")
st.pyplot(fig5)

# Gráfico 6: Atividade física vs. eletrônica
st.subheader("Atividade Física e Atividade Eletrônica por categoria de obesidade")
st.markdown("Comparação entre prática de exercícios físicos e uso de eletrônicos por grupo de peso.")
atividade_data = df.groupby("categoria_obesidade")[["atv_fisica", "atv_eletronica"]].mean()
atividade_data.columns = ["Atividade Física", "Atividade Eletrônica"]
fig6, ax6 = plt.subplots()
atividade_data.plot(kind="bar", ax=ax6, color=sns.color_palette("Blues")[0:2])
ax6.set_xlabel("Categoria de Obesidade")
ax6.set_ylabel("Média (Escala 0–3)")
st.pyplot(fig6)

# Gráfico 7: Consumo de água
st.subheader("Consumo de água por categoria de obesidade")
st.markdown("Média de ingestão de água por grupo de obesidade (escala de 0 a 3).")
fig7, ax7 = plt.subplots()
df.groupby("categoria_obesidade")["agua"].mean().plot(kind="bar", ax=ax7, color=sns.color_palette("Blues")[3])
ax7.set_xlabel("Categoria de Obesidade")
ax7.set_ylabel("Consumo Médio de Água")
st.pyplot(fig7)

# Gráfico 8: Consumo de álcool
st.subheader("Consumo de álcool por categoria de obesidade")
st.markdown("Proporção de pessoas que consomem álcool em cada grupo de obesidade.")
fig8, ax8 = plt.subplots()
df.groupby("categoria_obesidade")["alcool"].mean().plot(kind="bar", ax=ax8, color=sns.color_palette("Blues")[4])
ax8.set_xlabel("Categoria de Obesidade")
ax8.set_ylabel("Proporção Média de Consumo de Álcool")
st.pyplot(fig8)

# Gráfico 9: Histórico familiar
st.subheader("Histórico familiar por categoria de obesidade")
st.markdown("Proporção de pessoas com histórico familiar positivo (1) em cada grupo de obesidade.")
fig9, ax9 = plt.subplots()
df.groupby("categoria_obesidade")["historico"].mean().plot(kind="bar", ax=ax9, color=sns.color_palette("Blues")[1])
ax9.set_xlabel("Categoria de Obesidade")
ax9.set_ylabel("Proporção com Histórico Familiar Positivo")
st.pyplot(fig9)
