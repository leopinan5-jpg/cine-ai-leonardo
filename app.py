import streamlit as st

st.title("IA de Cine")

idea = st.text_area("Escribe tu idea de escena")

if st.button("Generar"):
    st.write("Idea recibida:")
    st.write(idea)
