# README

## Introducción
Este proyecto analiza un reporte de transacciones financieras a partir de un archivo CSV. Su propósito es calcular el balance final, encontrar la transacción con el monto más alto y contar la cantidad de transacciones de tipo "Crédito" y "Débito".

## Instrucciones de Ejecución
### Instalación de Dependencias
Asegúrate de tener Python instalado en tu sistema. Este proyecto usa la librería `pandas`, que puedes instalar con el siguiente comando:
```sh
pip install pandas
```

### Ejecución del Programa
Guarda el archivo de transacciones en formato CSV y ejecuta el script de Python con:
```sh
python script.py
```
Donde `script.py` es el nombre del archivo que contiene el código.

## Enfoque y Solución
El código sigue estos pasos:

1. Carga los datos desde un archivo CSV en un `DataFrame` de Pandas.
2. Calcula el balance final sumando los montos de transacciones tipo "Crédito" y restando las de tipo "Débito".
3. Encuentra la transacción con el monto máximo, extrayendo su `id` y `monto`.
4. Cuenta cuántas transacciones son de tipo "Crédito" y cuántas de tipo "Débito".
5. Imprime los resultados de cada uno de los cálculos.

## Estructura del Proyecto
```sh
/reporte.csv        # Archivo CSV con los datos de las transacciones
/script.py          # Script en Python que realiza el análisis
/README.md         # Documentación del proyecto
```
### Descripción de Archivos

`reporte.csv`: Archivo de entrada con la lista de transacciones.
`script.py`: Contiene la lógica de análisis de transacciones.
`README.md`: Documento con instrucciones sobre el uso del proyecto.
