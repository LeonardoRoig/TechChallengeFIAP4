
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

# Gráfico de porcentagem por categoria
st.subheader("Distribuição percentual dos níveis de obesidade")
fig1, ax1 = plt.subplots()
df["categoria_obesidade"].value_counts(normalize=True).plot.pie(autopct="%1.1f%%", startangle=90, ax=ax1)
ax1.set_ylabel("")
st.pyplot(fig1)

# Gráfico de barras por gênero
st.subheader("Distribuição da obesidade por gênero")
genero_data = df.groupby(["categoria_obesidade", "feminino"]).size().unstack().fillna(0)
genero_data.columns = ["Masculino", "Feminino"] if genero_data.shape[1] == 2 else genero_data.columns
fig2, ax2 = plt.subplots()
genero_data.plot(kind="bar", ax=ax2)
plt.xticks(rotation=0)
st.pyplot(fig2)

# Gráficos de refeição
st.subheader("Distribuição de número de refeições principais")
fig3, ax3 = plt.subplots()
df["ref_principais"] = pd.to_numeric(df["ref_principais"], errors="coerce")
df["ref_principais"].value_counts().sort_index().plot(kind="bar", ax=ax3)
st.pyplot(fig3)

st.subheader("Distribuição de consumo entre refeições")
fig4, ax4 = plt.subplots()
df["entre_ref"] = pd.to_numeric(df["entre_ref"], errors="coerce")
df["entre_ref"].value_counts().sort_index().plot(kind="bar", ax=ax4)
st.pyplot(fig4)
