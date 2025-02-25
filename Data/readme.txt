Esta carpeta contiene los datos utilizados en este projecto subdividido en dos carpetas: 


- Raw
    - Contiene el dataset original de la Comunidad Valenciana (df.csv) y un resumen de las variables que se encuentran en ellas organizadas por cuatro tipos:
        - Terreno
	- Condiciones meteorológicas
	- Localización y fecha
	- Recursos (posibles variables objetivo)

- Processed:
	- grid_20x20.csv: para las coordenadas superior izquierda y inferior derecha de cada una de las cuadrículas del grid
	- df_incendios_actualizado.csv: df transformado a partir del dataset orginal y que tiene localización para todas las filas
	- df_coordenadas: dataset del catastro que nos sirve de medio para situar incendios en municipios cuando no tienen localización. Se coge un punto fijo del     	ayuntamiento donde ha ocurrido el fuego
	- df_con_grid: df original al que se le añaden coordenadas para incendios sin localización y localización de cada incendio en el grid creado
	- df_con_grid_fire: df final que sirve para alimentar nuestros modelos con transformaciones y data engineering	
     