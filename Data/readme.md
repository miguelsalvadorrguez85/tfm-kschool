## 📂 Datos del Proyecto

Esta carpeta contiene los datos utilizados en este proyecto, subdivididos en dos carpetas:

### 📁 Raw
Contiene el dataset original de la Comunidad Valenciana (`df.csv`) y un resumen de las variables que se encuentran en él, organizadas por cuatro tipos:

- 🌍 **Terreno**
- 🌦 **Condiciones meteorológicas**
- 📅 **Localización y fecha**
- 🚒 **Recursos** (posibles variables objetivo)

### 📁 Processed
- 🗺 **`grid_20x20.csv`**: Coordenadas de la esquina superior izquierda e inferior derecha de cada una de las cuadrículas del grid.
- 🔥 **`df_incendios_actualizado.csv`**: Dataset transformado a partir del original, con localización para todas las filas.
- 🏛 **`df_coordenadas.csv`**: Dataset del catastro que ayuda a situar incendios en municipios sin localización. Se usa un punto fijo del ayuntamiento donde ocurrió el fuego.
- 📌 **`df_con_grid.csv`**: Dataset original con coordenadas añadidas para incendios sin localización y su ubicación en el grid.
- 📊 **`df_con_grid_fire.csv`**: Dataset final con transformaciones y data engineering, utilizado para alimentar los modelos.
