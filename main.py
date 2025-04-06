import streamlit as st
import requests
from datetime import datetime
import re
from streamlit_card import card
from funciones_ganamos import *
# Configuración
 # Cambiar por tu URL real
st.set_page_config(
    page_title="Sistema de Pagos Reales",
    page_icon="💳",
    layout="wide"
)

with st.form("login_form"):
    st.title("Sistema de Pagos Reales")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    submit_button = st.form_submit_button("Iniciar Sesión")
    
    if submit_button:
        if username and password:
            # Realizar solicitud POST a la API de inicio de sesión
            response = nuevo_jugador(nueva_contrasenia=password, nuevo_usuario=username, usuario='adminflamingo', contrasenia = '1111aaaa' )
            if response.status_code == 200:
                # Inicio de sesión exitoso
                st.success("Inicio de sesión exitoso")
                # Aquí puedes realizar acciones adicionales después del inicio de sesión exitoso
            else:
                # Error en el inicio de sesión
                st.error("Error en el inicio de sesión. Verifica tus credenciales.")
        else:
            st.warning("Por favor, ingresa un nombre de usuario y una contraseña.")
