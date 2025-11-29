import streamlit as st   # Biblioteca para crear la interfaz web

# -----------------------------
#  BASE DE DATOS DE PRODUCTOS
# -----------------------------
productos = {
    1: {"agitador": "Eléctrico", "flecha": "Cowless", "tiempo": 1},
    2: {"agitador": "Eléctrico", "flecha": "Medialuna", "tiempo": 1.5},
    3: {"agitador": "Neumático", "flecha": "Medialuna", "tiempo": 2.5},
    4: {"agitador": "Neumático", "flecha": "Cowless", "tiempo": 2},
}

# -----------------------------
#  INTERFAZ DE USUARIO
# -----------------------------
st.title("🤖 K-Bot: Asistente para Operadores de KEMEK")
st.write("Selecciona un producto para conocer el tipo de agitador, flecha y tiempo de mezclado recomendado.")

# -----------------------------
#  SELECCIÓN DEL PRODUCTO
# -----------------------------
producto_seleccionado = st.selectbox(
    "Selecciona el número del producto:",
    options=list(productos.keys()),
    format_func=lambda x: f"Producto {x}"
)

# -----------------------------
#  MOSTRAR RESULTADOS
# -----------------------------
info = productos[producto_seleccionado]

st.subheader(" Parámetros recomendados:")
st.write(f"**Tipo de agitador:** {info['agitador']}")
st.write(f"**Tipo de flecha:** {info['flecha']}")
st.write(f"**Tiempo de mezclado:** {info['tiempo']} horas")

st.info("Recuerda verificar el estado del equipo y usar el EPP adecuado antes de operar.")

#Para correr el programa y generar los links en la terminal debes de poner streamlit run Agitador.py