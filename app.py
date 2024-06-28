import streamlit as st
import pandas as pd
import plotly.express as px

# Listas para almacenar los datos
dates = []
products = []
quantities = []
prices = []

# Función para agregar datos a las listas
def add_data(date, product, quantity, price):
    dates.append(date)
    products.append(product)
    quantities.append(quantity)
    prices.append(price)

# Título de la aplicación
st.title('Aplicación de Ciencia de Datos para la Industria del Retail')

# Crear pestañas
tab1, tab2 = st.tabs(["Formulario", "Dashboard"])

with tab1:
    st.header("Formulario de Recopilación de Datos")

    # Campos del formulario
    date = st.date_input("Fecha")
    product = st.text_input("Producto")
    quantity = st.number_input("Cantidad", min_value=1)
    price = st.number_input("Precio", min_value=0.0, format="%.2f")

    # Botón para agregar datos
    if st.button("Agregar"):
        add_data(date, product, quantity, price)
        st.success("Datos agregados con éxito")

    # Mostrar datos recopilados
    if st.checkbox("Mostrar datos recopilados"):
        data = {'Fecha': dates, 'Producto': products, 'Cantidad': quantities, 'Precio': prices}
        df = pd.DataFrame(data)
        st.dataframe(df)

with tab2:
    st.header("Dashboard de Visualización")

    # Convertir listas a DataFrame
    if dates and products and quantities and prices:
        data = {'Fecha': dates, 'Producto': products, 'Cantidad': quantities, 'Precio': prices}
        df = pd.DataFrame(data)

        # Mostrar gráficos interactivos
        st.subheader("Ventas por Producto")
        fig1 = px.bar(df, x='Producto', y='Cantidad', color='Producto', title="Cantidad Vendida por Producto")
        st.plotly_chart(fig1)

        st.subheader("Ingresos por Producto")
        df['Ingresos'] = df['Cantidad'] * df['Precio']
        fig2 = px.pie(df, values='Ingresos', names='Producto', title="Distribución de Ingresos por Producto")
        st.plotly_chart(fig2)

        st.subheader("Tendencia de Ventas en el Tiempo")
        fig3 = px.line(df, x='Fecha', y='Cantidad', color='Producto', title="Tendencia de Cantidad Vendida en el Tiempo")
        st.plotly_chart(fig3)
    else:
        st.warning("No hay datos disponibles. Por favor, agrega datos en la pestaña de Formulario.")
