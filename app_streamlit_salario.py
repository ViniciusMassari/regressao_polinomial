import streamlit as st
import json
import requests

DISABLE = False
salario_em_reais = None

# Título da Aplicação
st.title("Modelo da Predição de Salário")

# Inputs
tempo_na_empresa = st.number_input("Quantos meses o profissional está na empresa ?", value=1, min_value=1)
nivel_na_empresa = st.number_input("Qual o nível do profissional na empresa ?", value=1, min_value=1, max_value=10)

# Preparar dados para a API
input_features = {'tempo_na_empresa': tempo_na_empresa, "nivel_na_empresa": nivel_na_empresa}



# Criar um botão e capturar um evento deste botão para disparad a API
if st.button("Estimar salário"):
    res = requests.post('http://127.0.0.1:8000/predict', data=json.dumps(input_features))
    res_json = json.loads(res.text)
    salario_em_reais = f"O salário estimado é de R$ {round(res_json['salario_em_reais'],2)}"
    st.subheader(salario_em_reais)


 


