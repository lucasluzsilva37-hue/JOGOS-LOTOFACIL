import streamlit as st
import pandas as pd
from collections import Counter
import random

st.title("Calculadora Lotofácil")

# Exemplo de dados históricos (substitua pelos seus dados reais)
historico = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    # Adicione mais resultados aqui...
]

todos_numeros = [num for jogo in historico for num in jogo]
frequencia = Counter(todos_numeros)

st.write("Frequência dos números nos últimos jogos:")
df_frequencia = pd.DataFrame.from_dict(frequencia, orient='index', columns=['Frequência'])
st.write(df_frequencia.sort_values(by='Frequência', ascending=False))

# Sugestão de números mais frequentes
mais_frequentes = [num for num, count in frequencia.most_common(10)]
st.write(f"Os 10 números mais frequentes são: {mais_frequentes}")

if st.button("Gerar Palpites"):
    st.write("Aqui estão 10 palpites sugeridos:")
    for i in range(1, 11):
        palpite = sorted(random.sample(mais_frequentes, 10) + random.sample(range(1, 26), 5))
        palpite = sorted(list(set(palpite[:15]))) # Garante 15 números únicos
        st.write(f"Palpite {i}: {palpite}")
