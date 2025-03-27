import streamlit as st
import pandas as pd
import os
import requests
from funciones_ganamos import login_ganamos, nuevo_jugador, carga_ganamos, retirar_ganamos, guardar_usuario
from fastapi import FastAPI, Request
import mercadopago

csv_file = 'data.csv'

usuario = 'adminflamingo'
contrasenia = '1111aaaa'

ACCESS_TOKEN = "APP_USR-7399764412139422-042622-5c8000e5a8932bbbdae5e8d418480e65-89912040"
mp = mercadopago.SDK(ACCESS_TOKEN)

st.set_page_config(page_title='TEST PAGE', page_icon='assets/ico.ico', layout='wide')

tab1 = st.tabs(['CREAR USUARIO', 'CARGAR SALDO', 'RETIRAR SALDO'])

with tab1[0]:
    st.subheader("Crear Usuario")
    new_user = st.text_input('Nombre de Usuario', key='name_usuario')
    pass_user = st.text_input('Contraseña', key='contra_usuario', type='password')
    
    if st.button('Crear Usuario'):
        guardar_usuario(usuario=new_user, contraseña=pass_user)

with tab1[1]:
    st.subheader("Cargar Saldo")
   
    def cargar_saldo():
        """Función para generar un pago en MercadoPago"""
        st.title("Cargar saldo a tu cuenta en Juegos Online")

        alias = st.text_input("Ingresa tu usuario de Ganamos")
        monto = st.number_input("Selecciona el monto a cargar (ARS)", min_value=1, step=1)

        if monto > 0:
            if st.button("Proceder al pago"):
                preference_data = {
                    "items": [
                        {
                            "title": "Carga de saldo para juegos online",
                            "quantity": 1,
                            "unit_price": float(monto),
                            "currency_id": "ARS"
                        }
                    ],
                    "back_urls": {
                        "success": "http://localhost:8501/?status=success",  # URL local
                        "failure": "http://localhost:8501/?status=failure",
                    },
                    "auto_return": "approved"
                }

                preference = mp.preference().create(preference_data)

                if "response" in preference and "init_point" in preference["response"]:
                    url_pago = preference["response"]["init_point"]
                    st.markdown(f"[Pagar con MercadoPago]({url_pago})", unsafe_allow_html=True)
                else:
                    st.error("Error al generar el enlace de pago.")
                    st.write("Respuesta de MercadoPago:", preference)

    def verificar_pago():
        """Verifica si el pago fue exitoso y carga el saldo en Ganamos"""
        st.title("Confirmación de Pago")

        query_params = st.query_params
        st.write("Parámetros recibidos:", query_params)  # DEBUG: Ver qué llega de MercadoPago

        estado_pago = query_params.get("collection_status", [""])[0]
        alias = st.session_state.get("alias")
        monto = st.session_state.get("monto")

        if estado_pago == "approved":
            st.success("¡Pago aprobado! Cargando saldo...")
            
            if alias and monto:
                exito, balance = carga_ganamos(alias, monto, usuario, contrasenia)
                if exito:
                    st.success(f"Saldo de {monto} ARS cargado correctamente en la cuenta {alias}.")
                else:
                    st.error("Error al cargar saldo en Ganamos.")
            else:
                st.error("No se encontraron los datos del usuario para cargar saldo.")
        
        elif estado_pago == "pending":
            st.warning("El pago está pendiente. Por favor, espera la confirmación.")
        
        else:
            st.error("El pago fue rechazado o falló. Intenta nuevamente.")

    # Determinar qué función ejecutar según el estado del pago
    query_params = st.query_params
    status = query_params.get("status", [""])[0]

    if status == "success":
        verificar_pago()
    else:
        cargar_saldo()

with tab1[2]:
    st.subheader("Retirar Saldo")
    if st.button('Retirar Saldo'):
        st.warning("Función de retiro") 




