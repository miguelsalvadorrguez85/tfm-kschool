

---

# README - Descripción de Archivos y Carpetas

Este repositorio contiene diferentes scripts utilizados en el procesamiento, análisis y modelado de datos. A continuación se describe el propósito y el contenido de cada carpeta y archivo.

## 01_EDA Análisis exploratorio de datos
Se realiza un análisis para entender el contexto de nuestro problema de negocio desglosado por variables temporales, meteorológicas, de recursos y sociales. 

## 01.1_mapeo_coordenadas_faltantes
En gran parte de nuestro dataset las coordenadas para longitud ('X') y latitud ('Y') son 0 por lo que no tenemos localización de estos incendios. Encontramos la manera de cruzarlo con otro dataset del catastro para que, en filas donde no tenemos localización, colocamos unas coordenadas fijas en el mismo municipio y así poder buscar variables de terreno y meteorológicas en GEE.

## 01.2_grid.ipynb
Añadimos un grid encima del terreno de la Comunidad Valenciana por si nos pudiera ser útil para suavizar features meteorológicas y de terreno.

## 02_Preprocesado
En esta carpeta se realiza un filtro de los datos según las coordenadas que son de interés. Además, se analizan las correlaciones entre las variables y se lleva a cabo un proceso de balanceo de clases, especialmente para aquellas clases muy desbalanceadas, utilizando técnicas de ajuste.

## 02.1_coordenadas
Aquí se transforma el formato de las coordenadas geográficas a latitud y longitud. Las coordenadas también se adaptan al formato requerido por Google Earth Engine (GEE), lo que permite la extracción eficiente de variables de la plataforma.

## 03_featureengineering
En este archivo se realiza un proceso de ingeniería de características. Se transforman variables numéricas continuas en categorías binarias (0, 1) y se crean nuevos índices a partir de variables existentes. También se realizan modificaciones adicionales sobre las variables de entrada para mejorar el desempeño de los modelos.

## 03.1_Acceso
Este archivo se encarga de la extracción de variables desde Google Earth Engine (GEE), obteniendo información relevante para los modelos de predicción.

## 03.2_Constantes
En este archivo también se realiza la extracción de variables desde GEE, pero se centra en la obtención de variables constantes que son necesarias para la interpretación y el análisis de los modelos.

## 04.1_Avion_anfibio
Esta carpeta contiene los modelos de clasificación y regresión utilizados para la predicción de la variable de interés relacionada con el **avión anfibio**. Se implementan los siguientes modelos:
- **CatBoost**
- **LGBM (Light Gradient Boosting Machine)**
- **Random Forest**
  
Además, se incluyen estudios económicos y análisis de umbrales para la variable específica que se está modelando.

## 04.2_Avion_Terrestre
Esta carpeta es similar a la anterior, pero centrada en el **avión terrestre**. Incluye modelos de clasificación y regresión:
- **CatBoost**
- **LGBM**
- **Random Forest**
  
También se incluyen los estudios económicos y análisis de umbrales.

## 04.3_Helicoptero
Aquí se modela el comportamiento de la variable específica relacionada con el **helicóptero**, con los mismos modelos de clasificación y regresión mencionados:
- **CatBoost**
- **LGBM**
- **Random Forest**

Al igual que en las carpetas anteriores, se llevan a cabo estudios económicos y análisis de umbrales.

## 04.4_Autobomba
Esta carpeta se enfoca en el modelo para la **autobomba**, usando los mismos enfoques de modelado:
- **CatBoost**
- **LGBM**
- **Random Forest**
  
Además de los modelos, también se encuentran los estudios económicos y los análisis de umbrales.

## 04.5_Buldozzer
Finalmente, en esta carpeta se realiza la clasificación y regresión para el **bulldozer**, utilizando los modelos:
- **CatBoost**
- **LGBM**
- **Random Forest**

Igual que en los otros casos, se incluyen los estudios económicos y los análisis de umbrales.

## All models

Muestra todo lo anterior junto, menos los formato javaScript ya que son los usados dentro de GEE y el de coordenadas que es un procesado previo

---

