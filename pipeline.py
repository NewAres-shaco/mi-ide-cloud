

from ingestion.lectura_csv import leer_datos_csv
from ingestion.batch_datos import leer_datos_batch
from ingestion.fuente_realtime import leer_clima_tiempo_real
from transformacion import transformar_libros, transformar_titanic, transformar_clima
import time
import pandas as pd

def run_orchestator():
    almacen_datos={}
    total_lecturas = []

    print("---lectura de csv---")
    almacen_datos['Titanic']=leer_datos_csv()

    print("---Lectura de titulos libros")
    almacen_datos['Libros']=leer_datos_batch('scifi')

    print("---Lectura del clima en tiempo real---")
    for i in range(5):
        print(f"  > instantanea {i+1}...")
        df_snap = leer_clima_tiempo_real()
        if not df_snap.empty:
            total_lecturas.append(df_snap)

    if total_lecturas:
        almacen_datos['clima'] = pd.concat(total_lecturas, ignore_index=True)
    else:
        almacen_datos['clima'] = pd.DataFrame()

    print("--- Resumen de datos sin transformar")

    for elemento, df in almacen_datos.items():
        print(f"\n📍 FUENTE: {elemento}")
        if not df.empty:
            print(f"Rows: {len(df)} | Columns: {list(df.columns)}")
            print(df.head(2))
        else:
            print("Empty Table (Check connection)")

    # Aplicar transformaciones
    if 'Libros' in almacen_datos:
        almacen_datos['Libros'] = transformar_libros(almacen_datos['Libros'])
        print("Transformación aplicada a Libros: columna 'unique key' agregada.")

    if 'Titanic' in almacen_datos:
        almacen_datos['Titanic'] = transformar_titanic(almacen_datos['Titanic'])
        print("Transformación aplicada a Titanic: filas de menores de 10 años eliminadas y análisis de sobrevivientes realizado.")

    if 'clima' in almacen_datos:
        almacen_datos['resumen_clima'] = transformar_clima(almacen_datos['clima'])
        print("Transformación aplicada a Clima: promedio de temperatura calculado.")

    # Mostrar resumen de todas las entradas
    print("\n---Resumen de entradas en almacen_datos---")
    for key, value in almacen_datos.items():
        if isinstance(value, pd.DataFrame):
            print(f"{key}: {value.shape[0]} filas, {value.shape[1]} columnas")
        else:
            print(f"{key}: {type(value)}")
        
    return almacen_datos


if __name__ == "__main__":
    datos = run_orchestator()  


