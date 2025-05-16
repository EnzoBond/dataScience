import streamlit as st
import dados
import exclui

st.title("Filmes")

nome = st.text_input("Nome do filme: ")
ano = st.number_input("Ano do filme: ", min_value=1990, max_value=2024)
nota = st.slider("Nota do filme: ", min_value=0.0, max_value=10.0)

if st.button("Adicionar"):
    dados.insere_dados(nome, ano, nota)
    st.success("Filme adicionado com sucesso!")

if st.button("Excluir Tabela"):
    exclui.excluir_dados()
    st.success("Filme excluido com sucesso!")

filmes = dados.obter_dados()
st.header("Lista de filmes:")
st.table(filmes)