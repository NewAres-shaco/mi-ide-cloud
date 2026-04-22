import pandas as pd

def transformar_libros(df):
    """
    Agrega una columna 'unique key' basada en la parte derecha de 'key' después del '/'.
    """
    df['unique key'] = df['key'].str.split('/').str[-1]
    return df

def transformar_titanic(df):
    """
    Filtra filas donde Age < 10 y realiza análisis de sobrevivientes.
    """
    # Filtrar menores de 10 años
    df = df[df['Age'] >= 10]
    # Análisis de sobrevivientes
    sobrevivientes = df.groupby('2urvived').size()
    print("Número de pasajeros que sobrevivieron y no sobrevivieron (después de filtrar menores de 10 años):")
    print(sobrevivientes)
    return df

def transformar_clima(df):
    """
    Calcula el promedio de la temperatura y devuelve un DataFrame resumen.
    """
    promedio_temp = df['temperature'].mean()
    resumen = pd.DataFrame({'promedio_temperatura': [promedio_temp]})
    return resumen