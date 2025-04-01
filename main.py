import streamlit as st
import requests
from datetime import datetime
import re
from streamlit_card import card

# Configuración
 # Cambiar por tu URL real
st.set_page_config(
    page_title="Sistema de Pagos Reales",
    page_icon="💳",
    layout="wide"
)



def show_premios():
    card(
        title="Vegas 365 Games",
        text="CONTACTA A UN CAJERO",
        image="https://png.pngtree.com/png-clipart/20190516/original/pngtree-whatsapp-icon-png-image_3584844.jpg",
        url= 'http://wa.link/fv17jl',
        styles={
            "card": {
                "width": "100%",
                "height": "200px",
                "border-radius": "60px",
                "box-shadow": "0 0 50px rgba(255, 215, 0, 1)",
                "margin-bottom": "0px"
            },
            "filter": {
                "background-color": "rgba(0, 0, 0, 0)"  # <- make the image not dimmed anymore
            },
            'text': {
                'color': 'black'
            },
            'title': {
                'color': 'black'
            }
        }
    )

show_premios()