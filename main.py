import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Ver tipos de datos de las columnas
print(df.dtypes)

# Convertir la columna 'Datetime' a tipo datetime
df['Datetime'] = pd.to_datetime(df['Datetime'])
# Establecer la columna 'Datetime' como índice del DataFrame
df.set_index('Datetime', inplace=True)

# Función para convertir de grados Kelvin a Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Copiar el DataFrame original y nombrarlo df_celsius
df_celsius = df.copy()

# Convertir las columnas numéricas (temperaturas en Kelvin) a Celsius usando la función creada
numeric_cols = df_celsius.select_dtypes(include=['number']).columns
df_celsius[numeric_cols] = df_celsius[numeric_cols].applymap(kelvin_to_celsius)

# Redondear las columnas numéricas a 2 decimales para mostrar/guardar
df_celsius[numeric_cols] = df_celsius[numeric_cols].round(2)

# Análisis sobre Phoenix
if 'Phoenix' in df_celsius.columns:
    phoenix = df_celsius['Phoenix']

    # Día y hora con temperatura mínima en Phoenix
    fecha_min = phoenix.idxmin()
    temp_min = phoenix.min()
    if pd.notnull(fecha_min):
        print(f"El día con la temperatura mínima en Phoenix fue: {fecha_min.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("No se pudo determinar la fecha de la temperatura mínima en Phoenix.")
    print(f"La temperatura mínima registrada en Phoenix fue de: {temp_min:.2f} °C")

    # Día y hora con temperatura máxima en Phoenix
    fecha_max = phoenix.idxmax()
    temp_max = phoenix.max()
    if pd.notnull(fecha_max):
        print(f"El día con la temperatura máxima en Phoenix fue: {fecha_max.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("No se pudo determinar la fecha de la temperatura máxima en Phoenix.")
    print(f"La temperatura máxima registrada en Phoenix fue de: {temp_max:.2f} °C")

    # Temperatura promedio en Phoenix durante el año 2016
    phoenix_2016 = phoenix[phoenix.index.year == 2016]
    if not phoenix_2016.empty:
        temp_prom_2016 = phoenix_2016.mean()
        print(f"La temperatura promedio durante 2016 en Phoenix fue de: {temp_prom_2016:.2f} °C")
    else:
        print("No hay datos de Phoenix para el año 2016 en el DataFrame.")
else:
    print("La columna 'Phoenix' no existe en el DataFrame.")

# Graficar la temperatura de Phoenix durante el año 2016
plt.figure(figsize=(20, 10))
if 'Phoenix' in df_celsius.columns:
    phoenix_2016 = df_celsius[df_celsius.index.year == 2016]
    if not phoenix_2016.empty:
        # Usar datos redondeados a 2 decimales en la gráfica
        plt.scatter(phoenix_2016.index, phoenix_2016['Phoenix'].round(2), label='Phoenix')
    else:
        # Si no hay datos de 2016, graficar todo el rango disponible (redondeado)
        plt.scatter(df_celsius.index, df_celsius['Phoenix'].round(2), label='Phoenix')
else:
    # Si no existe Phoenix, intentar graficar la primera columna numérica encontrada
    if len(numeric_cols) > 0:
        plt.scatter(df_celsius.index, df_celsius[numeric_cols[0]].round(2), label=numeric_cols[0])
        plt.title(f'Temperatura de {numeric_cols[0]}')
    else:
        plt.title('No hay columnas numéricas para graficar')

plt.title('Temperatura en Phoenix durante 2016')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid()
plt.savefig("temperatura_phoenix_2016.png")
plt.show()

# Exportar el DataFrame modificado a un nuevo archivo CSV (valores ya redondeados a 2 decimales)
df_celsius.to_csv("temperatura_celsius.csv")
