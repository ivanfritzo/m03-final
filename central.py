#se importa la libreria pandas para el manejo de archivos CSV
import pandas as pd
# Parte 1: Cargar Datos
def cargar_datos(lineas_archivos):
    df = pd.read_csv("movies.csv")
    # Crear un conjunto 
    generos_peliculas = set()
    # Recorrer cada fila en generos, los separa y añade al conjunto
    df['generos'].str.split(';').apply(generos_peliculas.update)

    # Crear un diccionario de películas por género
    peliculas_por_genero = {}
    #Este es un metodo de la libreria pandas que permite recorrer cada fila del DataFrame
    for index, row in df.iterrows():
        titulo = row["titulo"]
        generos = row["generos"].split(";")
        for genero in generos:
            if genero not in peliculas_por_genero:
                peliculas_por_genero[genero] = []
            peliculas_por_genero[genero].append(titulo)      


    # Crear una lista con el formato (titulo, popularidad, voto promedio, cant de votos y generos)
    info_peliculas = []
    for index, row in df.iterrows():
        titulo = row["titulo"]
        popularidad = row["popularidad"]
        voto_promedio = row["voto_promedio"]
        cantidad_votos = row["cantidad_votos"]
        generos = row["generos"].split(";")

        # Crea la tupla con el formato y agrega la informacion
        tupla_pelicula = (titulo, popularidad, voto_promedio, cantidad_votos, generos)
        info_peliculas.append(tupla_pelicula)

    return generos_peliculas, peliculas_por_genero, info_peliculas


# Parte 2: Completar las consultas
def obtener_puntaje_y_votos(nombre_pelicula):
    df = pd.read_csv("movies.csv")

    # Buscar la pelicula en el DataFrame con el mismo nombre sin importar mayusculas
    pelicula = df[df["titulo"].str.match(f"^{nombre_pelicula}$", case=False)]

    # Extrae el puntaje promedio y la cantidad de votos de la pelicula previamente escrita
    voto_promedio = pelicula["voto_promedio"].values[0]
    cantidad_votos = pelicula["cantidad_votos"].values[0]
    return voto_promedio, cantidad_votos


def filtrar_y_ordenar(genero_pelicula):
    df = pd.read_csv("movies.csv")

    # Filtra las peliculas del genero especificado
    peliculas_filtradas = df[df["generos"].str.contains(genero_pelicula, case=False)]
    
    # Ordenar las películas por nombre (Z-A)
    peliculas_ordenadas = peliculas_filtradas.sort_values(by="titulo", ascending=False)
    
    # Extraer los titulos de las peliculas
    nombres_peliculas = peliculas_ordenadas["titulo"].tolist()
    
    # Filtra, ordena y extrae los títulos en una sola línea
    #nombres_peliculas = df[df["generos"].str.contains(genero_pelicula, case=False)].sort_values(by="titulo", ascending=False)["titulo"].tolist()
    return nombres_peliculas



def obtener_estadisticas(genero_pelicula, criterio):
    df = pd.read_csv("movies.csv")

    # Filtra las peliculas del genero especificado
    peliculas_filtradas = df[df["generos"].str.contains(genero_pelicula, case=False)]
    
    # Extraer los valores del criterio
    valores_criterio = peliculas_filtradas[criterio]
    
    # Calcular el máximo, mínimo y promedio
    maximo = valores_criterio.max()
    minimo = valores_criterio.min()
    promedio = round(valores_criterio.mean(),2)
    
    return maximo, minimo, promedio

# NO ES NECESARIO MODIFICAR DESDE AQUI HACIA ABAJO

def solicitar_accion():
    print("\n¿Qué desea hacer?\n")
    print("[0] Revisar estructuras de datos")
    print("[1] Obtener puntaje y votos de una película")
    print("[2] Filtrar y ordenar películas")
    print("[3] Obtener estadísticas de películas")
    print("[4] Salir")

    eleccion = input("\nIndique su elección (0, 1, 2, 3, 4): ")
    while eleccion not in "01234":
        eleccion = input("\nElección no válida.\nIndique su elección (0, 1, 2, 3, 4): ")
    eleccion = int(eleccion)
    return eleccion


def leer_archivo():
    lineas_peliculas = []
    with open("movies.csv", "r", encoding="utf-8") as datos:
        for linea in datos.readlines()[1:]:
            lineas_peliculas.append(linea.strip())
    return lineas_peliculas


def revisar_estructuras(generos_peliculas, peliculas_por_genero, info_peliculas):
    print("\nGéneros de películas:")
    for genero in generos_peliculas:
        print(f"    - {genero}")

    print("\nTítulos de películas por genero:")
#========= se modificaron unos datos=========
    #for genero in peliculas_por_genero:
    #    print(f"    genero: {genero[0]}")
    #    for titulo in genero[1]:         
    for genero, peliculas in peliculas_por_genero.items():
        print(f"    genero: {genero}")
        for titulo in peliculas:
            print(f"        - {titulo}")

    print("\nInformación de cada película:")
    for pelicula in info_peliculas:
        print(f"      Nombre: {pelicula[0]}")
        print(f"        - Popularidad: {pelicula[1]}")
        print(f"        - Puntaje Promedio: {pelicula[2]}")
        print(f"        - Votos: {pelicula[3]}")
        print(f"        - Géneros: {pelicula[4]}")


def solicitar_nombre():
    nombre = input("\nIngrese el nombre de la película: ")
    return nombre


def solicitar_genero():
    genero = input("\nIndique el género de película: ")
    return genero


def solicitar_genero_y_criterio():
    genero = input("\nIndique el género de película: ")
    criterio = input(
        "\nIndique el criterio (popularidad, voto promedio, cantidad votos): "
    )
    return genero, criterio


def main():
    lineas_archivo = leer_archivo()
    datos_cargados = True
    try:
        generos_peliculas, peliculas_por_genero, info_peliculas = cargar_datos(
            lineas_archivo
        )
    except TypeError as error:
        if "cannot unpack non-iterable NoneType object" in repr(error):
            print(
                "\nTodavía no puedes ejecutar el programa ya que no has cargado los datos\n"
            )
            datos_cargados = False
    if datos_cargados:
        salir = False
        print("\n********** ¡Bienvenid@! **********")
        while not salir:
            accion = solicitar_accion()

            if accion == 0:
                revisar_estructuras(
                    generos_peliculas, peliculas_por_genero, info_peliculas
                )

            elif accion == 1:
                nombre_pelicula = solicitar_nombre()
                ptje, votos = obtener_puntaje_y_votos(nombre_pelicula)
                print(f"\nObteniendo puntaje promedio y votos de {nombre_pelicula}")
                print(f"    - Puntaje promedio: {ptje}")
                print(f"    - Votos: {votos}")

            elif accion == 2:
                genero = solicitar_genero()
                nombres_peliculas = filtrar_y_ordenar(genero)
                print(f"\nNombres de películas del género {genero} ordenados:")
                for nombre in nombres_peliculas:
                    print(f"    - {nombre}")

            elif accion == 3:
                genero, criterio = solicitar_genero_y_criterio()
                estadisticas = obtener_estadisticas(genero, criterio)
                print(f"\nEstadísticas de {criterio} de películas del género {genero}:")
                print(f"    - Máximo: {estadisticas[0]}")
                print(f"    - Mínimo: {estadisticas[1]}")
                print(f"    - Promedio: {estadisticas[2]}")

            else:
                salir = True
        print("\n********** ¡Adiós! **********\n")


if __name__ == "__main__":
    main()