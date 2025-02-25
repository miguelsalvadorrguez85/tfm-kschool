---

# 📖 README - Files and Folders Description

This repository contains various scripts used for data processing, analysis, and modeling. Below is a description of the purpose and content of each folder and file.

## 📊 01_EDA - Exploratory Data Analysis
An analysis is conducted to understand the context of our business problem, broken down by temporal, meteorological, resource, and social variables.

## 🌍 01.1_Missing_Coordinates_Mapping
In a significant portion of our dataset, the longitude (`X`) and latitude (`Y`) coordinates are `0`, meaning we lack location data for these fires. We found a way to cross-reference it with a cadastre dataset so that, for rows without location data, we assign fixed coordinates within the same municipality. This allows us to retrieve terrain and meteorological variables from **Google Earth Engine (GEE).**

## 🗺 01.2_Grid.ipynb
A grid is added over the **Comunidad Valenciana** terrain to help smooth meteorological and terrain features.

## 🔄 02_Preprocessing
This folder contains data filtering based on relevant coordinates. Additionally, correlations between variables are analyzed, and class balancing is performed, particularly for highly imbalanced classes, using adjustment techniques.

## 📍 02.1_Coordinates
Here, the geographic coordinate format is transformed into latitude and longitude. The coordinates are also adapted to the format required by **Google Earth Engine (GEE)** for efficient variable extraction.

## ⚙ 03_FeatureEngineering
This file performs feature engineering. Continuous numerical variables are transformed into binary categories (`0,1`), and new indices are created based on existing variables. Additional modifications are also applied to the input variables to enhance model performance.

## 🌐 03.1_Access
This file is responsible for extracting variables from **Google Earth Engine (GEE)** to gather relevant information for prediction models.

## 📈 03.2_Constants
Similar to the previous file, but focused on extracting **constant variables** needed for model interpretation and analysis.

---

## 🚁 Resource Allocation Models

### ✈️ 04.1_Amphibious_Aircraft
This folder contains classification and regression models used to predict the target variable related to **amphibious aircraft**. The following models are implemented:
- **CatBoost**
- **LGBM (Light Gradient Boosting Machine)**
- **Random Forest**

Additionally, it includes economic studies and threshold analyses for this specific variable.

### ✈️ 04.2_Land_Aircraft
Similar to the previous folder but focused on **land aircraft**. It includes classification and regression models:
- **CatBoost**
- **LGBM**
- **Random Forest**

Economic studies and threshold analyses are also provided.

### 🚁 04.3_Helicopter
This folder models the behavior of the variable related to **helicopters**, using the same classification and regression models:
- **CatBoost**
- **LGBM**
- **Random Forest**

Economic studies and threshold analyses are conducted here as well.

### 🚒 04.4_Fire_Truck
This section focuses on modeling the **fire truck** variable, applying the same modeling techniques:
- **CatBoost**
- **LGBM**
- **Random Forest**

It also includes economic studies and threshold analyses.

### 🏗 04.5_Bulldozer
Finally, this folder contains classification and regression models for **bulldozers**, using:
- **CatBoost**
- **LGBM**
- **Random Forest**

Economic studies and threshold analyses are included here as well.

---

## 📦 All Models
This section consolidates all the models, except for JavaScript-based models used within **GEE** and the coordinate file, which is part of a previous processing step.

---
