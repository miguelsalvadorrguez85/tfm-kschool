<h1 style="text-align: center;">🔥FireForecast: Predictive Resource Allocation for Wildfire Management🔥</h1>

<h3><u>🎓 This is a master's final project for the Data Science master's program at KSchool</u></h3>

<h3>👥 Contributors</h3>

        Mónica Velasco de la Fuente - monicavelasco0@gmail.com
        Fernando García Abal - fergaabal@gmail.com
        Miguel Ángel Salvador Rodríguez - miguelsalvador.rguez@gmail.com

<h2>🚀 Introduction</h2>

FireForecast is a predictive analytics project aimed at optimizing the allocation of firefighting resources in the Comunidad Valenciana. The project leverages machine learning models to predict the necessary deployment of aerial and ground firefighting units, helping emergency response teams make informed decisions.

This repository contains all the data, scripts, and models used in the research, development, and deployment of the FireForecast application. The application is publicly available at: 🌍 [link](https://firecast.streamlit.app/)

***

<h2>📂 Repository Structure</h2>

<h3>1. 📁 app/</h3>

Contains files necessary for running the Firecast web application.

        📊 DataFrames: Used to display data in the app, including wildfire coordinates and similarity comparisons.

        📜 Notebooks: Simple models used for predictions, with final models accessible via the Notebooks menu.

        🧠 Pretrained Models (.pkl): Models for resource allocation and preprocessing.

        📌 Requirements.txt : Dependencies required for deploying the app on Streamlit.

        ▶️ app.py: Main entry point for the Streamlit application.

***

<h3>2. 📂 data/</h3>

Contains the datasets used for training and validation.


RAW:  

📝 df.csv: Original dataset from the Comunidad Valenciana.

📑 summary_variables.xlsx: Description of the dataset variables categorized into:

        🏔️ Terrain

        🌦️ Meteorological Conditions

        📍 Location and Date

        🚒 Resources (Potential Target Variables)

PROCESSED:

        🗺️ grid_20x20.csv: Grid coordinates.

        🔥 df_incendios_actualizado.csv: Updated dataset with added locations.

        📌 df_coordenadas.csv: Catastro dataset used to infer locations for missing coordinates.

        📊 df_con_grid.csv: Augmented dataset with inferred locations.

        🚒 df_con_grid_fire.csv: Final dataset for modeling, including feature engineering transformations.

***

<h3>3. 📂 Notebooks&scripts/</h3>

Contains Jupyter notebooks and Python scripts for data processing, modeling, and evaluation.

Notebooks:

        📊 01_EDA: Exploratory Data Analysis.

        🌍 01.1_mapeo_coordenadas_faltantes: Handling missing wildfire coordinates.

        🗺️ 01.2_grid.ipynb: Implementation of a spatial grid for smoothing meteorological and terrain variables.

        ⚙️ 02_Preprocesado: Data preprocessing, correlation analysis, and class balancing.

        🛠️ 03_featureengineering: Feature engineering and variable transformation.

        🌎 03.1_Acceso: Extraction of variables from Google Earth Engine (GEE).

        📏 03.2_Constantes: Collection of static variables from GEE.

        🤖 04_Modeling/

        🛩️ 04.1_Avion_anfibio: Models for amphibious aircraft resource prediction.

        🛬 04.2_Avion_Terrestre: Models for land-based aircraft resource prediction.

        🚁 04.3_Helicoptero: Helicopter resource prediction models.

        🚒 04.4_Autobomba: Fire truck resource prediction models.

        🚜 04.5_Bulldozer: Bulldozer resource prediction models.

***

<h3>4. 📂 reports/</h3>

Contains automated reports generated using pandas-profiling, providing insights into dataset characteristics and feature correlations.

***

<h3>🧠 Machine Learning Models</h3>

FireForecast employs the following machine learning algorithms:

        🌲 Random Forest

        📈 LightGBM (LGBM)

        🐱 CatBoost

        📊 Model Selection & Evaluation

Models were evaluated using:

        🔢 Classification Metrics: AUC, Precision, Recall, F1-score.

        📉 Regression Metrics: MAE, RMSE.

        💰 Economic Impact Analysis: To balance cost and efficiency in resource allocation.

<h3>🚀 Deployment</h3>

The app is publicly accessible at this [link](https://firecast.streamlit.app/).


***

<h3>🛠️ Installation & Usage</h3>

Running the Streamlit App Locally

        pip install -r app/requirements.txt
        streamlit run app/app.py


***

<h3>🔮 Future Work</h3>

        📍 Expansion to other wildfire-prone regions.

        🛰️ Integration with real-time satellite imagery.

        📊 Improved interpretability with SHAP and LIME analysis.

        📶 Apply our best models to the deployed visual tool Firecast.

<h3>👥 Contributors</h3>

        Mónica Velasco de la Fuente - monicavelasco0@gmail.com
        Fernando García Abal - fergaabal@gmail.com
        Miguel Ángel Salvador Rodríguez - miguelsalvador.rguez@gmail.com



<i>📖 For detailed methodology, findings, and future directions, refer to the Memoria_TFM_Predicion_Medios_Incendios.pdf included in this repository.</i>

