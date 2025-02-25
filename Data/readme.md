## 📂 Project Data

This folder contains the data used in this project, subdivided into two folders:

### 📁 Raw
Contains the original dataset from the **Comunidad Valenciana** (`df.csv`) and a summary of the variables categorized into four types:

- 🌍 **Terrain**
- 🌦 **Weather conditions**
- 📅 **Location and date**
- 🚒 **Resources** (potential target variables)

### 📁 Processed
- 🗺 **`grid_20x20.csv`**: Coordinates of the top-left and bottom-right corners of each grid cell.
- 🔥 **`df_incendios_actualizado.csv`**: Transformed dataset based on the original one, with location available for all rows.
- 🏛 **`df_coordenadas.csv`**: Catastro dataset used to assign a location to fires in municipalities without precise coordinates. A fixed point at municipality is used for reference.
- 📌 **`df_con_grid.csv`**: Original dataset with added coordinates for fires without location and their assigned grid position.
- 📊 **`df_con_grid_fire.csv`**: Final dataset with transformations and data engineering, used to feed the models.
