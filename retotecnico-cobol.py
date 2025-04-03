import pandas as pd #Aquí agregamos la librería Pandas que nos ayudará a leer Archivos CSV

nombre_archivo = 'reporte.csv' #Como opción coloqué para poder indicar el nombre de nuestro archivo a leer
Reporte_Transacciones = pd.read_csv(nombre_archivo)  #Aquí leemos el archivo y lo almacenamos en un DataFrame (Diccionario o Estructura de Datos)

print('Reporte de Transacciones')
print('------------------------------------------')
#Para encontrar el Balance Final, debemos de encontrar todas las transacciones que tengan como tipo igual a 'Crédito'
#posteriormente debemos sumar todos los valores de la columna 'monto', realizamos lo mismo para las transacciones de tipo 'Débito'
#y como nos indica el ejercicio restamos el total de Crédito menos el total de Débito para conseguir el balance total. Finalmente lo imprimimos.
print('Balance Final: ', Reporte_Transacciones[Reporte_Transacciones.tipo == 'Crédito'].monto.sum() - Reporte_Transacciones[Reporte_Transacciones.tipo == 'Débito'].monto.sum())
#Para obtener los datos de la transacción con el monto máximo primero encontramos el dato, posteriormente para imprimirlo, extraemos el id
#y también el monto, finalmente colocamos ambos en la línea de impresión
print('Transaccion de Mayor Monto: ID ', Reporte_Transacciones[Reporte_Transacciones.monto == Reporte_Transacciones.monto.max()].iloc[0]['id'], ' - ', Reporte_Transacciones[Reporte_Transacciones.monto == Reporte_Transacciones.monto.max()].iloc[0]['monto'])
#Para tener el total de transacciones de tipo crédito utilizamos la función len el cuál va a contar cuántos elementos tiene tanto el dataframe
#que contiene las transacciones de tipo 'Crédito' como el que tiene las transacciones de tipo 'Debito"
print('Conteo de Transacciones: Crédito =', len(Reporte_Transacciones[Reporte_Transacciones.tipo == 'Crédito']), '; Débito = ', len(Reporte_Transacciones[Reporte_Transacciones.tipo == 'Débito']))