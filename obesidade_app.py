
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
df["ref_principais"] = pd.to_numeric(df["ref_principais"], errors="coerce")
df["entre_ref"] = pd.to_numeric(df["entre_ref"], errors="coerce")
df["vegetais"] = pd.to_numeric(df["vegetais"], errors="coerce")
df["atv_fisica"] = pd.to_numeric(df["atv_fisica"], errors="coerce")
df["atv_eletronica"] = pd.to_numeric(df["atv_eletronica"], errors="coerce")
df["agua"] = pd.to_numeric(df["agua"], errors="coerce")
df["alcool"] = pd.to_numeric(df["alcool"], errors="coerce")

st.title("Estudo sobre Obesidade")

st.markdown("Este painel analisa hábitos alimentares, atividades e gênero em relação aos diferentes níveis de obesidade.")

# Pizza: Distribuição de obesidade
st.subheader("Distribuição percentual dos níveis de obesidade")
st.markdown("Mostra a proporção geral da população analisada em cada grupo de peso.")
fig1, ax1 = plt.subplots()
df["categoria_obesidade"].value_counts(normalize=True).plot.pie(autopct="%1.1f%%", startangle=90, ax=ax1)
ax1.set_ylabel("")
st.pyplot(fig1)

# Barras por gênero
st.subheader("Distribuição da obesidade por gênero")
st.markdown("Mostra a quantidade de homens e mulheres presentes em cada categoria de obesidade.")
genero_data = df.groupby(["categoria_obesidade", "feminino"]).size().unstack().fillna(0)
genero_data.columns = ["Masculino", "Feminino"]
fig2, ax2 = plt.subplots()
genero_data.plot(kind="bar", ax=ax2)
ax2.set_xlabel("Categoria de Obesidade")
ax2.set_ylabel("Número de Pessoas")
plt.xticks(rotation=0)
st.pyplot(fig2)

# Boxplot: refeições principais
st.subheader("Refeições principais por categoria de obesidade")
st.markdown("Boxplot da quantidade de refeições principais consumidas por dia, segmentadas por categoria de obesidade.")
fig3, ax3 = plt.subplots()
sns.boxplot(x="categoria_obesidade", y="ref_principais", data=df, ax=ax3, palette="Blues")
ax3.set_xlabel("Categoria de Obesidade")
ax3.set_ylabel("Refeições Principais por Dia")
st.pyplot(fig3)

# Stacked bar: entre refeições
st.subheader("Pessoas que comem entre as refeições por categoria de obesidade")
st.markdown("Gráfico empilhado com o número de pessoas que consomem alimentos entre as refeições por categoria de obesidade.")
entre_ref_data = df.groupby("categoria_obesidade")["entre_ref"].value_counts().unstack().fillna(0)
entre_ref_data.columns = ["Não come entre refeições", "Come entre refeições"]
fig4, ax4 = plt.subplots()
entre_ref_data.plot(kind="bar", stacked=True, ax=ax4, colormap="Paired")
ax4.set_xlabel("Categoria de Obesidade")
ax4.set_ylabel("Número de Pessoas")
plt.xticks(rotation=0)
st.pyplot(fig4)

# Comparação: vegetais
st.subheader("Consumo de vegetais por categoria de obesidade")
st.markdown("Consumo médio de vegetais por faixa de obesidade. Escala de 0 (baixo) a 3 (alto).")
fig5, ax5 = plt.subplots()
df.groupby("categoria_obesidade")["vegetais"].mean().plot(kind="bar", ax=ax5, color="green")
ax5.set_xlabel("Categoria de Obesidade")
ax5.set_ylabel("Consumo Médio de Vegetais")
st.pyplot(fig5)

# Comparação: atividade física vs. eletrônica
st.subheader("Atividade física e tempo em eletrônicos por obesidade")
st.markdown("Comparação entre prática de exercícios e uso de dispositivos eletrônicos nas categorias de obesidade.")
atv_data = df.groupby("categoria_obesidade")[["atv_fisica", "atv_eletronica"]].mean()
fig6, ax6 = plt.subplots()
atv_data.plot(kind="bar", ax=ax6)
ax6.set_xlabel("Categoria de Obesidade")
ax6.set_ylabel("Média por Escala (0–3)")
st.pyplot(fig6)

# Comparação: Consumo de água
st.subheader("Consumo de água por categoria de obesidade")
st.markdown("Média de ingestão de água (escala de 0 a 3) por grupo de peso.")
fig7, ax7 = plt.subplots()
df.groupby("categoria_obesidade")["agua"].mean().plot(kind="bar", ax=ax7, color="skyblue")
ax7.set_xlabel("Categoria de Obesidade")
ax7.set_ylabel("Consumo Médio de Água")
st.pyplot(fig7)

# Comparação: Consumo de álcool
st.subheader("Consumo de álcool por categoria de obesidade")
st.markdown("Proporção de pessoas que consomem álcool por nível de obesidade.")
alcool_data = df.groupby("categoria_obesidade")["alcool"].mean()
fig8, ax8 = plt.subplots()
alcool_data.plot(kind="bar", ax=ax8, color="red")
ax8.set_xlabel("Categoria de Obesidade")
ax8.set_ylabel("Proporção de Pessoas que Consomem Álcool")
st.pyplot(fig8)
