# Proyecto Python - Análisis de Películas

Este proyecto tiene como objetivo aplicar los conocimientos adquiridos en el módulo 3 de **Fundamentos de Python**. El programa se centrará en procesar y analizar información de un archivo CSV con datos sobre películas. El trabajo será realizado en parejas, pero la defensa del proyecto será individual, donde el profesor seleccionará a un estudiante para que explique cada parte del desarrollo.

## Estructura de Archivos

- `central.py`: Archivo principal del programa donde se realizarán todas las modificaciones necesarias.
- `movies.csv`: Archivo que contiene información sobre diversas películas en el siguiente formato:
  - `titulo`: Nombre de la película.
  - `popularidad`: Popularidad de la película (valor numérico).
  - `voto_promedio`: Puntaje promedio de la película.
  - `cantidad_votos`: Número de votos que ha recibido la película.
  - `generos`: Lista de géneros de la película separados por punto y coma.

## Tareas a Realizar

### 1. Cargar Datos

Debes completar la función `cargar_datos(lineas_archivo)` en el archivo `central.py` para procesar las líneas del archivo `movies.csv` y generar las siguientes estructuras:

- `generos_peliculas`: Lista de todos los géneros distintos presentes en las películas. Asegúrate de no repetir géneros.
- `peliculas_por_genero`: Lista de tuplas donde el primer elemento es el nombre del género y el segundo es una lista de películas que pertenecen a dicho género.
- `info_peliculas`: Lista de tuplas con el formato `(titulo, popularidad, voto_promedio, cantidad_votos, [generos])`, donde `[generos]` es una lista con los géneros de la película.

Al finalizar, la función debe retornar una tupla con los tres elementos: `generos_peliculas`, `peliculas_por_genero`, `info_peliculas`.

### 2. Completar las Consultas

Debes completar las siguientes funciones para permitir consultas sobre los datos procesados:

#### **obtener_puntaje_y_votos(nombre_pelicula)**
- Entrada: El nombre de una película.
- Salida: Una tupla `(voto_promedio, cantidad_votos)`.

#### **filtrar_y_ordenar(genero_pelicula)**
- Entrada: El nombre de un género de película.
- Salida: Una lista de nombres de películas pertenecientes a ese género, ordenada alfabéticamente en orden inverso.

#### **obtener_estadisticas(genero_pelicula, criterio)**
- Entrada: Un género de película y un criterio que puede ser "popularidad", "voto promedio" o "cantidad votos".
- Salida: Una lista con el formato `[max, min, promedio]`, donde:
  - `max`: El valor máximo del criterio.
  - `min`: El valor mínimo del criterio.
  - `promedio`: El promedio de los valores del criterio para las películas de ese género.

### Consideraciones

- Para procesar los datos de las películas, utiliza el método `split()` de Python para dividir la información del CSV.
- Asegúrate de que las estructuras de datos se usen correctamente para responder a las consultas.
  
## Ejecución del Proyecto

1. Clona el repositorio.
2. Modifica el archivo `central.py` según los lineamientos descritos.
3. Asegúrate de que el archivo `movies.csv` esté en la misma carpeta que `central.py`.
4. Ejecuta el programa para realizar las consultas desde la línea de comandos.

## Evaluación

La defensa del proyecto se realizará individualmente, y se evaluará el entendimiento de cada parte del código.

