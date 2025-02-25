import streamlit as st
import joblib
import numpy as np
import pandas as pd
import pyproj  # Para transformar de UTM a lat/lon

# ------------------------------------------------------------------------------
# 1. Cargar modelos y preprocesador
# ------------------------------------------------------------------------------
model_aviones = joblib.load("modelo_incendios_aviones_descarga.pkl")
model_helicopteros = joblib.load("modelo_incendios_helicopteros_transporte.pkl")
model_bulldozers = joblib.load("modelo_incendios_bulldozer.pkl")
model_aviones_terrestres = joblib.load("modelo_incendios_aviones_terrestres.pkl")
model_autobombas = joblib.load("modelo_incendios_autobombas.pkl")
knn_model = joblib.load("knn_model.pkl")
preprocessor = joblib.load("preprocessor_knn.pkl")

# ------------------------------------------------------------------------------
# 2. Cargar dataset histórico para el KNN
# ------------------------------------------------------------------------------
df_fires = pd.read_csv("df_con_grid.csv")

# ------------------------------------------------------------------------------
# 3. Definir transformación UTM -> lat/lon
# ------------------------------------------------------------------------------
transformer = pyproj.Transformer.from_crs("EPSG:32630", "EPSG:4326", always_xy=True)
def utm_to_latlon(x_utm, y_utm):
    lon, lat = transformer.transform(x_utm, y_utm)
    return lat, lon

# ------------------------------------------------------------------------------
# 4. Columnas predictoras y categorías
# ------------------------------------------------------------------------------
predictors = ["D_VIENTO", "V_VIENTO", "IND_PE_TXT", "H_RELAT", "DULLUVIA", "X", "Y", "ESTACION"]

# Extraer categorías del preprocesador
cat_transformer = preprocessor.named_transformers_['cat']
ind_pe_txt_categories = cat_transformer.categories_[0]
estacion_categories   = cat_transformer.categories_[1]

# ------------------------------------------------------------------------------
# 5. Título y entrada de datos en la barra lateral
# ------------------------------------------------------------------------------
st.markdown(
    """
    <h1 style="text-align: center;">
        🔥 Firecast 🔥
    </h1>
    """,
    unsafe_allow_html=True
)

st.sidebar.header("Datos de Incendio")
d_viento = st.sidebar.number_input("Dirección del viento (°)", value=230)
v_viento = st.sidebar.number_input("Velocidad del viento (km/h)", value=20)
ind_pe_txt = st.sidebar.selectbox("Índice de peligro (categoría)", ind_pe_txt_categories)
h_relat = st.sidebar.number_input("Humedad relativa (%)", value=30)
d_lluvia = st.sidebar.number_input("Días sin lluvia", value=5)
x_utm = st.sidebar.number_input("Coordenada X (UTM)", value=690455.0)
y_utm = st.sidebar.number_input("Coordenada Y (UTM)", value=4403401.0)
estacion = st.sidebar.selectbox("Estación del año", estacion_categories)

# Crear DataFrame con los datos ingresados
df_nuevo_incendio = pd.DataFrame([{
    "D_VIENTO": d_viento,
    "V_VIENTO": v_viento,
    "IND_PE_TXT": ind_pe_txt,
    "H_RELAT": h_relat,
    "DULLUVIA": d_lluvia,
    "X": x_utm,
    "Y": y_utm,
    "ESTACION": estacion
}])

# ------------------------------------------------------------------------------
# 6. Crear pestañas para la Predicción y los Incendios Similares
# ------------------------------------------------------------------------------
tab_pred, tab_sim = st.tabs(["Predicción", "Incendios Similares"])

# Pestaña de Predicción
with tab_pred:
    st.header("Predicción de Recurso")
    # Selección del recurso a predecir (simulando las pestañas)
    resource = st.radio("Selecciona el recurso a predecir", 
                         ("Aviones", "Helicópteros", "Bulldozers", "Aviones Terrestres", "Autobombas"))
    
    # Definir el texto del botón según el recurso seleccionado
    if resource == "Aviones":
        button_label = "Predecir si se necesitan aviones"
    elif resource == "Helicópteros":
        button_label = "Predecir si se necesitan helicópteros"
    elif resource == "Bulldozers":
        button_label = "Predecir si se necesitan bulldozers"
    elif resource == "Aviones Terrestres":
        button_label = "Predecir si se necesitan aviones terrestres"
    elif resource == "Autobombas":
        button_label = "Predecir si se necesitan autobombas"
    
    if st.button(button_label):
        # Preprocesar los datos
        X_pre = preprocessor.transform(df_nuevo_incendio[predictors])
        
        # Realizar la predicción según el recurso seleccionado
        if resource == "Aviones":
            prediction = model_aviones.predict(X_pre)[0]
            if prediction == 1:
                st.error("🚨 ¡Se necesitan aviones para combatir el incendio!")
            else:
                st.success("✅ No es necesario enviar aviones en este momento.")
        elif resource == "Helicópteros":
            prediction = model_helicopteros.predict(X_pre)[0]
            if prediction == 1:
                st.error("🚨 ¡Se necesitan helicópteros para el transporte!")
            else:
                st.success("✅ No es necesario enviar helicópteros en este momento.")
        elif resource == "Bulldozers":
            prediction = model_bulldozers.predict(X_pre)[0]
            if prediction == 1:
                st.error("🚨 ¡Se necesitan bulldozers para combatir el incendio!")
            else:
                st.success("✅ No es necesario enviar bulldozers en este momento.")
        elif resource == "Aviones Terrestres":
            prediction = model_aviones_terrestres.predict(X_pre)[0]
            if prediction == 1:
                st.error("🚨 ¡Se necesitan aviones terrestres para combatir el incendio!")
            else:
                st.success("✅ No es necesario enviar aviones terrestres en este momento.")
        elif resource == "Autobombas":
            prediction = model_autobombas.predict(X_pre)[0]
            if prediction == 1:
                st.error("🚨 ¡Se necesitan autobombas para combatir el incendio!")
            else:
                st.success("✅ No es necesario enviar autobombas en este momento.")
        
        # Mostrar el mapa con el punto ingresado
        lat, lon = utm_to_latlon(x_utm, y_utm)
        st.map(pd.DataFrame({"lat": [lat], "lon": [lon]}))

# Pestaña de Incendios Similares
with tab_sim:
    st.header("Incendios Históricos Similares")
    if st.button("Buscar incendios similares"):
        X_pre_knn = preprocessor.transform(df_nuevo_incendio[predictors])
        distances, indices = knn_model.kneighbors(X_pre_knn, n_neighbors=5)
        nearest_fires = df_fires.iloc[indices[0]].copy()
        nearest_fires["Distancia"] = distances[0]
        
        columns = ["ET_ID", "NOM_MUN", "X", "Y", "AVIANFNUM", "HELTRANUM", "BULDOZZER", "AVICARNUM", "AUTOBOMBA"]
        custom_names = ["ID Incendio", "Municipio", "Coordenada X", "Coordenada Y",
                        "Aviones descarga", "Helicópteros", "Bulldozers", "Aviones Terrestres", "Autobombas"]
        df_display = nearest_fires[columns].copy()
        df_display.columns = custom_names
        
        st.write("Los 5 incendios más similares encontrados:")
        st.dataframe(df_display)
        
        lat_list, lon_list = [], []
        for _, row in nearest_fires.iterrows():
            lat_i, lon_i = utm_to_latlon(row["X"], row["Y"])
            lat_list.append(lat_i)
            lon_list.append(lon_i)
        st.map(pd.DataFrame({"lat": lat_list, "lon": lon_list}))
