// Cargar el archivo CSV con las coordenadas, fecha y hora
var csvFile = ee.FeatureCollection('projects/kschool2024fajas/assets/coordenadas');

// Cargar los datasets de Google Earth Engine
var srtm = ee.Image('USGS/SRTMGL1_003');  // Datos de elevación
var landCover = ee.ImageCollection('ESA/WorldCover/v100').first();  // Clasificación 2020

// Calcular pendiente (slope)
var slope = ee.Terrain.slope(srtm).rename('Slope');

// Función para calcular el índice de dificultad de acceso
function calcularDificultadAcceso(feature) {
  var lon = feature.get('Longitude');
  var lat = feature.get('Latitude');
  var point = ee.Geometry.Point([lon, lat]);

  // Calcular pendiente
  var slopeValue = slope.reduceRegion({
    reducer: ee.Reducer.mean(),
    geometry: point,
    scale: 1000
  }).get('Slope');

  // Calcular elevación
  var elevationValue = srtm.reduceRegion({
    reducer: ee.Reducer.mean(),
    geometry: point,
    scale: 1000
  }).get('elevation');

  // Calcular cobertura de suelo
  var landCoverValue = landCover.reduceRegion({
    reducer: ee.Reducer.mode(),
    geometry: point,
    scale: 1000
  }).get('Map');

  // Omitir la parte de distancia a carreteras si no tienes acceso a esa información
  var distanceToRoad = ee.Number(0); // Valor predeterminado en 0 si no tenemos la distancia a carreteras

  // Asignar valores predeterminados si algún valor es null
  slopeValue = ee.Algorithms.If(ee.Algorithms.IsEqual(slopeValue, null), 0, slopeValue);
  elevationValue = ee.Algorithms.If(ee.Algorithms.IsEqual(elevationValue, null), 0, elevationValue);
  landCoverValue = ee.Algorithms.If(ee.Algorithms.IsEqual(landCoverValue, null), 0, landCoverValue);

  // Crear un índice de dificultad de acceso (ejemplo simple)
  var difficultyIndex = ee.Number(slopeValue)
    .multiply(0.4) // Mayor pendiente, mayor dificultad
    .add(ee.Number(elevationValue).multiply(0.3)) // Mayor altitud, mayor dificultad
    .add(ee.Number(landCoverValue).multiply(0.2)) // Cobertura de suelo (bosque = más difícil)
    .subtract(distanceToRoad.multiply(0.1)); // Más cerca de carreteras, más fácil

  return feature.set({
    DifficultyIndex: difficultyIndex
  });
}

// Aplicar la función a cada fila del archivo CSV
var resultados = csvFile.map(calcularDificultadAcceso);

// Exportar los resultados como un nuevo archivo CSV
Export.table.toDrive({
  collection: resultados,
  description: 'DificultadDeAcceso_Valencia',
  fileFormat: 'CSV'
});

