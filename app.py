import streamlit as st

st.title("IA de Cine")

idea = st.text_area("Escribe tu idea de escena")

if st.button("Generar"):
    st.write("Idea recibida:")
    st.write(idea)
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

SYSTEM_PROMPT = """
Eres un asistente especializado en cine, dramaturgia cinematográfica,
dirección de fotografía, planificación de rodaje y análisis semiótico.

Debes pensar como:

director de cine
dramaturgo
director de fotografía
primer asistente de dirección
analista visual

Referencias estéticas:

Andrei Tarkovsky → poesía visual, simbolismo, tiempo contemplativo
Wong Kar-wai → atmósfera emocional, color expresivo
Lars von Trier → crudeza emocional, cámara cercana

Reglas:

máximo 4 planos abiertos
máximo 7 planos totales
priorizar metáfora visual
usar recursos filmables
evitar diálogo innecesario
"""

st.title("IA de Dirección Cinematográfica")

st.write("Desarrolla escenas, ideas visuales y planificación de rodaje.")

modo = st.selectbox(
    "Modo de trabajo",
    [
        "ficción",
        "experimental",
        "cineminuto",
        "videoarte",
        "planificación de rodaje",
        "iluminación",
        "storyboard"
    ]
)

idea = st.text_area("Describe tu idea o escena")

if st.button("Generar escena"):

    prompt = f"""
Modo seleccionado: {modo}

Idea del usuario:
{idea}

Generar respuesta con:

1 Concepto dramático
2 Arquetipo dramático
3 Semiótica visual
4 Metáfora visual
5 Atmósfera
6 Diseño de planos
7 Blocking
8 Storyboard textual
9 Lentes
10 Esquema de iluminación
11 Shooting list
12 Plan de rodaje
13 Montaje
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"user","content":prompt}
        ],
        temperature=0.9
    )

    resultado = response.choices[0].message.content

    st.markdown(resultado)
