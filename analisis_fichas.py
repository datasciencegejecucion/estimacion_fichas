import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import os
import estimacion_fichas
import requests
import json
import xlsxwriter


# Menú lateral
with st.sidebar:
    selected = option_menu(
        menu_title="Menú Principal",
        options=['Inicio','Estimación Fichas']
    )

# Sección de Inicio
if selected == 'Inicio':
    st.title(f"Herramientas de Estimación de fichas y programas de formacion a ofertar")
    
    st.write("""
        Esta aplicación ofrece diversas un modulo para el análisis de datos históricos de fichas y estimar el numero
        de cupos que de deberian ofertar por programa de formación en los diferentes centros de formación
        mediante el uso de mineria de datos y estadisticas respecto al comportamiento que tienen los programas en los años anteriores.
        Es importante mencionar que dicha aplicación es de uso exclusivo para la estimación de fichas del SENA,
        y los resultados los resultados estan destinados al mismo.
        """)
    
    st.write("""
        - **Generar Indicativo de fichas**: Genera el indicativo anual de grupos por centro de formación.
    """)

if selected == 'Estimación Fichas':
    estimacion_fichas.mostrar_estimacion_fichas()  # Llama a la función del archivo estimacion_fichas
else:
    st.title("Bienvenido a la aplicación")
    st.write("Selecciona la pestaña de estimación de fichas para comenzar.")
