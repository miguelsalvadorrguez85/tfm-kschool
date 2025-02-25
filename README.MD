🔥 FireForecast: Predictive Resource Allocation for Wildfire Management

🚀 Introduction

FireForecast is a predictive analytics project aimed at optimizing the allocation of firefighting resources in the Comunidad Valenciana. The project leverages machine learning models to predict the necessary deployment of aerial and ground firefighting units, helping emergency response teams make informed decisions.

This repository contains all the data, scripts, and models used in the research, development, and deployment of the FireForecast application. The application is publicly available at: 🌍 FireForecast Streamlit App.

***

📂 Repository Structure

1. 📁 app/

Contains files necessary for running the FireForecast web application.

📊 DataFrames: Used to display data in the app, including wildfire coordinates and similarity comparisons.

📜 Notebooks: Simple models used for predictions, with final models accessible via the Notebooks menu.

🧠 Pretrained Models (``): Models for resource allocation and preprocessing.

📌 Requirements.txt : Dependencies required for deploying the app on Streamlit.

▶️ app.py: Main entry point for the Streamlit application.

***

2. 📂 data/

Contains the datasets used for training and validation.



📝 df.csv: Original dataset from the Comunidad Valenciana.

📑 summary_variables.xlsx: Description of the dataset variables categorized into:

🏔️ Terrain

🌦️ Meteorological Conditions

📍 Location and Date

🚒 Resources (Potential Target Variables)

``

🗺️ grid_20x20.csv: Grid coordinates.

🔥 df_incendios_actualizado.csv: Updated dataset with added locations.

📌 df_coordenadas.csv: Catastro dataset used to infer locations for missing coordinates.

📊 df_con_grid.csv: Augmented dataset with inferred locations.

🚒 df_con_grid_fire.csv: Final dataset for modeling, including feature engineering transformations.

***

3. 📂 Notebooks&scripts/

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

4. 📂 reports/

Contains automated reports generated using pandas-profiling, providing insights into dataset characteristics and feature correlations.

***

🧠 Machine Learning Models

FireForecast employs the following machine learning algorithms:

🌲 Random Forest

📈 LightGBM (LGBM)

🐱 CatBoost

📊 Model Selection & Evaluation

Models were evaluated using:

🔢 Classification Metrics: AUC, Precision, Recall, F1-score.

📉 Regression Metrics: MAE, RMSE.

💰 Economic Impact Analysis: To balance cost and efficiency in resource allocation.

🚀 Deployment

Models are stored in .pkl format for streamlined inference.

The Streamlit app loads the best-performing models to provide real-time resource predictions.

***

🛠️ Installation & Usage

Running the Streamlit App Locally

pip install -r app/requirements.txt
streamlit run app/app.py

Running Jupyter Notebooks

pip install jupyter
jupyter notebook

***

🔮 Future Work

📍 Expansion to other wildfire-prone regions.

🛰️ Integration with real-time satellite imagery.

📊 Improved interpretability with SHAP and LIME analysis.

👥 Contributors

📝 [Your Name]

🎓 [Your Institution]

📩 Contact: [Your Email]

📖 For detailed methodology, findings, and future directions, refer to the Memoria_TFM_Predicion_Medios_Incendios.pdf included in this repository.

