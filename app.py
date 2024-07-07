import streamlit as st
import plotly.express as px
import pandas as pd
# import plotly.figure_factory as ff
# import os
# import matplotlib
# import scipy.stats
# import time

# Title
st.set_page_config(page_title="Store Car!", page_icon=":bar_chart:", layout="wide")
st.header(" :car: Sample Store Car")
#Esta función en Streamlit permite renderizar contenido en formato Markdown
st.markdown('''
    <style>
        div.block-container {
            padding-top: 1rem;
            margin-top: 2rem;
            background-color: #67C9EB;
        }
        h1 {
            color: #5B7BEB;
        }
        .custom-class {
            font-size: 1.5rem;
            color: blue;
        }
    </style>
''', unsafe_allow_html=True)

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

# Estilos CSS para el botón
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #6783EB;
        color: #ffffff;
        border: none;
        color: white;
        padding: 10px 25px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 14px;
        margin: 2px 1px;
        cursor: pointer;
        border-radius: 20px;
    }
    .stButton>button:hover {
        background-color: #ffffff;
        color: #6783EB;
        border: solid 1px #6783EB;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------- LIMPIEZA DE DATOS --------------
# Eliminar filas con valores NaN en las columnas relevantes
car_data = car_data.dropna(subset=['model_year', 'price', 'odometer'])


# ---------------- CONSTRUCCIÓN DE GRÁFICOS ---------------------

# Crear el botón con estilo personalizado
hist_button = st.button('Construir histograma') # crear un botón
scatter_button = st.button('Construir gráfico de dispersión')
        
# Cargar los datos solo si se presiona el botón
if hist_button:
    try:
        # Mensaje informativo
        st.write('### Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
        st.write(' Este histograma muestra la distribución del kilometraje de los coches en venta.')

        # Crear un histograma mejorado
        fig = px.histogram(
            car_data, 
            x="odometer",
            title="Distribución del Kilometraje de los Coches en Venta",
            labels={"odometer": "Kilometraje (millas)"},
            nbins=200,  # Número de bins
            template="plotly_dark"  # Se ajusta el tema
        )
        
        # Personalizar el diseño del gráfico
        fig.update_layout(
            xaxis_title="Kilometraje (millas)",
            yaxis_title="Frecuencia",
            bargap=0.2,  # Ajustar el espacio entre las barras
            title_font_size=20,
            xaxis_title_font_size=16,
            yaxis_title_font_size=16,
            showlegend=False
        )
        
        # Mostrar el gráfico interactivo
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"Ocurrió un error al cargar los datos: {e}")


# Funcionalidad del botón de gráfico de dispersión
if scatter_button:
    st.write('### Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    st.write('Este gráfico de dispersión muestra la relación entre el precio y el kilometraje.')

    # Crear un gráfico de dispersión mejorado
    fig2 = px.scatter(
        car_data, 
        x="price", 
        y="odometer", 
        size="model_year",
        title="Relación entre Precio y Kilometraje",
        labels={"price": "Precio", "odometer": "Kilometraje (millas)"},
        template="plotly_dark"
    )

    # Personalizar el diseño del gráfico
    fig2.update_layout(
        title_font_size=20,
        xaxis_title_font_size=16,
        yaxis_title_font_size=16
    )

    # Mostrar el gráfico interactivo
    st.plotly_chart(fig2, use_container_width=True)





# El resto de código para abajo son practicas que esta realizando con otros datos

# #Los usuarios pueden subir archivos de ciertos tipos especificados 
# fl = st.file_uploader(":file_folder: Upload a file", type=(["csv","txt","xlxs","xls"]))
# if fl is not None:
#     filename = fl.name
#     st.write(filename)
#     df = pd.read_csv(filename, encoding="ISO-8859-1")
# else:
#     os.chdir(r"D:\AnalisisdeDatos\AppWeb-Streamlit")
#     df = pd.read_csv("Superstore.csv", encoding="ISO-8859-1")

# # Se constuye un filtro de fechas para observar los datos
# col1, col2 = st.columns((2))
# df["Order Date"] = pd.to_datetime(df["Order Date"])

# # Obtener la mínima y máxima fecha
# startDate = pd.to_datetime(df["Order Date"]).min()
# endDate = pd.to_datetime(df["Order Date"]).max()

# #Crear un selector de fechas con la etiqueta "Start Date" y "End Date"
# with col1:
#     date1 = pd.to_datetime(st.date_input("Start Date", startDate))

# with col2:
#     date2 = pd.to_datetime(st.date_input("End Date", endDate))

# #Crea una copia del DataFrame resultante del filtrado de fechas 
# df = df[(df["Order Date"] >= date1) & (df["Order Date"] <= date2)].copy()

# #Crear un menu lateral para filtar el dataframe por Region y estado
# #Filtrar por Region
# st.sidebar.header("Choose your filter: ")
# region = st.sidebar.multiselect("Pick your Region", df["Region"].unique())
# if not region: 
#     df2 = df.copy()
# else:
#     df2 = df[df["Region"].isin(region)]

# #Filtrar por Estado
# state = st.sidebar.multiselect("Pick the State", df2["State"].unique())
# if not state:
#     df3 = df2.copy()
# else:
#     df3 = df2[df2["State"].isin(state)]

# #Filtrar por ciudad
# city = st.sidebar.multiselect("Pick the City", df3["City"].unique())

# if not region and not state and not city:
#     filtered_df = df
# elif not state and not city:
#     filtered_df = df[df["Region"].isin(region)]
# elif not region and not city:
#     filtered_df = df[df["State"].isin(state)]
# elif state and city:
#     filtered_df = df3[df3["State"].isin(state) & df3["City"].isin(city)]
# elif region and city:
#     filtered_df = df3[df3["Region"].isin(region) & df3["City"].isin(city)]
# elif region and state:
#     filtered_df = df3[df3["Region"].isin(region) & df3["State"].isin(state)]
# elif city:
#     filtered_df = df3[df3["City"].isin(city)]
# else:
#     filtered_df = df3[df3["Region"].isin(region) & df3["State"].isin(state) & df3["City"].isin(city)]

# # Se agrupa el Dataframe por la columna Category y se calcula la suma de "Sales" de cada grupo   
# category_df = filtered_df.groupby(by = ["Category"], as_index = False)["Sales"].sum()

# #Se genera una gráfia de barras para visualizar las ventas con un formato de moneda en cada valor.  
# with col1:
#     st.subheader("Category wise Sales")
#     fig = px.bar(category_df, x = "Category", y = "Sales", text = ['${:,.2f}'.format(x) for x in category_df["Sales"]],
#                 template = "seaborn")
#     st.plotly_chart(fig, use_container_width=True, height = 200)

# #Se genera una gráfica de dona para visualizar las ventas por región
# with col2:
#     st.subheader("Region wise Sales")
#     fig = px.pie(filtered_df, values = "Sales", names = "Region", hole = 0.5)
#     fig.update_traces(text = filtered_df["Region"], textposition = "outside")
#     st.plotly_chart(fig, use_container_width=True)

# #Dos columnas en la interfaz
# cl1, cl2 = st.columns(2)
# # Filtrar el dataframe en base a la categoria y proporciona un botón para descargar los datos
# with cl1:
#     with st.expander("Category_ViewData"):
#         st.write(category_df.style.background_gradient(cmap="Blues"))
#         csv = category_df.to_csv(index = False).encode('utf-8')
#         st.download_button("Download Data", data = csv, file_name= "Category.csv", mime = "text/csv",
#                         help = 'Click here to download the data as a CSV file')

# # Filtrar el dataframe en base a la region y proporciona un botón para descargar los datos
# with cl2:
#     with st.expander("Region_ViewData"):
#         region = filtered_df.groupby(by = "Region", as_index = False)["Sales"].sum()
#         st.write(region.style.background_gradient(cmap="Oranges"))
#         csv = region.to_csv(index = False).encode('utf-8')
#         st.download_button("Download Data", data = csv, file_name = "Region.csv", mime = "text/csv",
#                         help = 'Click here to download the data as a CSV file')

# #Agrupa las ventas mensuales, se crea un gráfico de líneas con esos datos y muestra el gráfico
# filtered_df["month_year"] = filtered_df["Order Date"].dt.to_period("M")
# st.subheader('Time Series Analysis')

# linechart = pd.DataFrame(filtered_df.groupby(filtered_df["month_year"].dt.strftime("%Y : %b"))["Sales"].sum()).reset_index()
# fig2 = px.line(linechart, x = "month_year", y="Sales", labels = {"Sales": "Amount"}, height=500, width=1000, template="gridon")
# st.plotly_chart(fig2, use_container_width=True)

# # Botón para descargar el csv de TimeSeries
# with st.expander("View Data of TimeSeries:"):
#     st.write(linechart.T.style.background_gradient(cmap="Blues"))
#     csv = linechart.to_csv(index=False).encode("utf-8")
#     st.download_button('Download Data', data = csv, file_name= "TimeSeries.csv", mime='text/csv')

# # Crear y mostrar un TreeMap que visualiza las ventas jerárquicamente basadas en la región, 
# # la categoría y la subcategoría de los productos.
# st.subheader("Hierarchical view of Sales using TreeMap")
# fig3 = px.treemap(filtered_df, path = ["Region", "Category", "Sub-Category"], values = "Sales", hover_data= ["Sales"],
#                 color = "Sub-Category")
# fig3.update_layout(width = 800, height = 650)
# st.plotly_chart(fig3, use_container_width=True)

# # Dos gráficos de pastel, uno para mostrar las ventas por segmento en la primera columna 
# # y otro para mostrar las ventas por categoría en la segunda columna.
# chart1, chart2 = st.columns((2))
# with chart1:
#     st.subheader('Segment wise Sales')
#     fig = px.pie(filtered_df, values = "Sales", names = "Segment", template = "plotly_dark")
#     fig.update_traces(text = filtered_df["Segment"], textposition = "inside")
#     st.plotly_chart(fig, use_container_width=True)

# with chart2:
#     st.subheader('Category wise Sales')
#     fig = px.pie(filtered_df, values = "Sales", names = "Category", template = "gridon")
#     fig.update_traces(text = filtered_df["Category"], textposition = "inside")
#     st.plotly_chart(fig, use_container_width=True)

# # Este bloque de código muestra un subtítulo seguido de una tabla de resumen de las ventas por subcategoría
# st.subheader(":point_right: Month wise Sub-Category Sales Summary")
# with st.expander("Summary_Table"):
#     df_sample = df[0:5][["Region","State","City","Category","Sales","Profit","Quantity"]] #nuevo DataFrame df_sample que contiene las primeras cinco filas del DataFrame original
#     fig = ff.create_table(df_sample, colorscale="Cividis")
#     st.plotly_chart(fig, use_container_width=True)

#     #Crea una tabla pivotada que muestra las ventas por subcategoría desglosadas por mes.
#     st.markdown("Month wise sub-Category Table")
#     filtered_df["month"] = filtered_df["Order Date"].dt.month_name()
#     sub_category_Year = pd.pivot_table(data = filtered_df, values = "Sales", index = ["Sub-Category"], columns="month")
#     st.write(sub_category_Year.style.background_gradient(cmap="Blues"))

# # Crea y configura un gráfico de dispersión para mostrar la relación entre ventas y ganancias, con el tamaño de los puntos basado en la cantidad.
# data1 = px.scatter(filtered_df, x = "Sales", y = "Profit", size = "Quantity")
# data1['layout'].update(title="Relationship between Sales and Profits using Scatter Plot.",
#                     titlefont = dict(size=20), xaxis = dict(title="Sales", titlefont=dict(size=19)),
#                     yaxis = dict(title = "Profit", titlefont = dict(size=19)))
# st.plotly_chart(data1, use_container_width=True)

# # Se selecciona una porción del DataFrame filtered_df.
# # :500 las primeras 500 filas.
# # 1:20:2 selecciona columnas desde la segunda hasta la vigésima, de dos en dos.
# with st.expander("View Data"):
#     st.write(filtered_df.iloc[:500,1:20:2].style.background_gradient(cmap="Oranges"))

# #Download original DataSet
# csv = df.to_csv(index = False).encode('utf-8')
# st.download_button('Download Data', data = csv, file_name= "Data.csv", mime = "text/csv")
