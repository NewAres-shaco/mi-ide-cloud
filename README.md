# mi-ide-cloud
prueba ramo gestion IA

## Transformaciones Aplicadas

- **Libros**: Se agrega una columna `unique key` extraída de la parte derecha de la columna `key` después del `/`.
- **Titanic**: Se eliminan todas las filas de pasajeros menores de 10 años para limpiar el conjunto de datos, y luego se realiza un análisis de sobrevivientes agrupando por la columna `2urvived`.
- **Clima**: Se capturan 5 instantáneas de clima en tiempo real, se concatenan en un solo DataFrame y se calcula una tabla resumen con el promedio de temperatura.

## Flujo de ejecución

El orquestador lee las fuentes de datos (`Titanic.csv`, datos de libros por batch y clima en tiempo real), aplica las transformaciones definidas en `transformacion.py` y muestra un resumen de todas las entradas disponibles en `almacen_datos`. 