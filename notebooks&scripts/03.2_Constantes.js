// Cargar el archivo CSV con las coordenadas, fecha y hora
var csvFile = ee.FeatureCollection('projects/kschool2024fajas/assets/coordenadas');

// Cargar los datasets de Google Earth Engine
var temperature = ee.ImageCollection('ECMWF/ERA5_LAND/HOURLY').select('temperature_2m');
var windSpeed = ee.ImageCollection('ECMWF/ERA5_LAND/HOURLY').select('u_component_of_wind_10m', 'v_component_of_wind_10m');
var humidity = ee.ImageCollection('ECMWF/ERA5_LAND/HOURLY').select('dewpoint_temperature_2m');
var srtm = ee.Image('USGS/SRTMGL1_003');  // Datos de elevación (altitud)

// Función para calcular pendiente (derivada de altitud)
var slope = ee.Terrain.slope(srtm).rename('Slope');

// Cargar datos de cobertura terrestre
var landCover = ee.ImageCollection('ESA/WorldCover/v100').first();  // Clasificación 2020

// Variables relacionadas con el contenido de agua en el suelo
var soilWater = ee.ImageCollection('ECMWF/ERA5_LAND/HOURLY').select('volumetric_soil_water_layer_1'); // Agua en el suelo

// Función para obtener los datos de cada fila del CSV
function obtenerDatos(feature) {
  var lon = feature.get('Longitude');
  var lat = feature.get('Latitude');
  var fechaHora = ee.Date(feature.get('DateTime')); // Usar la columna combinada 'DateTime'

  // Crear un punto a partir de las coordenadas
  var point = ee.Geometry.Point([lon, lat]);

  // Filtrar las colecciones por fecha/hora
  var tempImage = temperature.filterBounds(point).filterDate(fechaHora, fechaHora.advance(1, 'hour')).mean();
  var windImage = windSpeed.filterBounds(point).filterDate(fechaHora, fechaHora.advance(1, 'hour')).mean();
  var humidityImage = humidity.filterBounds(point).filterDate(fechaHora, fechaHora.advance(1, 'hour')).mean();

  // Reducir datos al punto
  var temp_value = tempImage.reduceRegion({
    reducer: ee.Reducer.mean(),
    geometry: point,
    scale: 1000
  });

  var wind_value = windImage.reduceRegion({
    reducer: ee.Reducer.mean(),
    geometry: point,
    scale: 1000
  });

  var humidity_value = humidityImage.reduceRegion({
    reducer: ee.Reducer.mean(),
    geometry: point,
    scale: 1000
  });

  var elevation_value = srtm.reduceRegion({
    reducer: ee.Reducer.mean(),
    geometry: point,
    scale: 1000
  });

  var slope_value = slope.reduceRegion({
    reducer: ee.Reducer.mean(),
    geometry: point,
    scale: 1000
  });

  var soilWaterValue = soilWater.filterBounds(point).filterDate(fechaHora, fechaHora.advance(1, 'hour')).mean();
  var landCover_value = landCover.reduceRegion({
    reducer: ee.Reducer.mode(),
    geometry: point,
    scale: 20
  });

  // Calcular Fuel Load Index (puedes combinar otros índices relacionados)
  var fuelLoadIndex = landCover_value.get('Map');  // Puedes calcularlo de forma diferente si tienes otro índice

  var soilWaterContent = ee.Algorithms.If(
    soilWaterValue, 
    soilWaterValue, 
    -9999
  );

  var pendiente = ee.Algorithms.If(
    slope_value.get('Slope'), 
    slope_value.get('Slope'), 
    -9999
  );

  // Agregar datos al feature
  return feature.set({
    Temperature: temp_value.get('temperature_2m'),
    WindSpeed_U: wind_value.get('u_component_of_wind_10m'),
    WindSpeed_V: wind_value.get('v_component_of_wind_10m'),
    Humidity: humidity_value.get('dewpoint_temperature_2m'),
    Elevation: elevation_value.get('elevation'),
    Slope: pendiente, // Agregar la pendiente
    SoilWaterContent: soilWaterContent,
    LandCover: landCover_value.get('Map'),
    FuelLoadIndex: fuelLoadIndex
  });
}

// Aplicar la función a cada fila del archivo CSV
var resultados = csvFile.map(obtenerDatos);

// Exportar los resultados como un nuevo archivo CSV
Export.table.toDrive({
  collection: resultados,
  description: 'DatosSinDroughtCode_LandCover_FuelLoad_Rugosidad_Suelo',
  fileFormat: 'CSV'
});