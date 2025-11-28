import pandas as pd
import matplotlib.pyplot as plt

def kelvin_to_celsius_df(df):
    # Convert numeric temperature columns from K to °C
    numeric_cols = df.select_dtypes(include=['number']).columns
    # vectorized conversion avoids applymap deprecation
    df[numeric_cols] = df[numeric_cols] - 273.15
    df[numeric_cols] = df[numeric_cols].round(2)
    return df

def main():
    df = pd.read_csv("data.csv")
    df['Datetime'] = pd.to_datetime(df['Datetime'])
    df.set_index('Datetime', inplace=True)

    df_celsius = df.copy()
    df_celsius = kelvin_to_celsius_df(df_celsius)

    # Analysis sobre Phoenix
    if 'Phoenix' in df_celsius.columns:
        phoenix = df_celsius['Phoenix']

        # Primero: promedio durante 2016
        phoenix_2016 = phoenix[phoenix.index.year == 2016]
        if not phoenix_2016.empty:
            temp_prom_2016 = phoenix_2016.mean()
            print(f"La temperatura promedio durante 2016 en Phoenix fue de: {temp_prom_2016:.1f} °C")
        else:
            print("No hay datos de Phoenix para el año 2016 en el DataFrame.")

        # Luego: mínimos y máximos
        fecha_min = phoenix.idxmin()
        temp_min = phoenix.min()
        if pd.notnull(fecha_min):
            print(f"El día con la temperatura mínima en Phoenix fue: {fecha_min.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("No se pudo determinar la fecha de la temperatura mínima en Phoenix.")
        print(f"La temperatura mínima registrada en Phoenix fue de: {temp_min:.1f} °C")

        fecha_max = phoenix.idxmax()
        temp_max = phoenix.max()
        if pd.notnull(fecha_max):
            print(f"El día con la temperatura máxima en Phoenix fue: {fecha_max.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("No se pudo determinar la fecha de la temperatura máxima en Phoenix.")
        print(f"La temperatura máxima registrada en Phoenix fue de: {temp_max:.1f} °C")
    else:
        print("La columna 'Phoenix' no existe en el DataFrame.")

    # Plot and save (do not call plt.show() in CI)
    plt.figure(figsize=(20, 10))
    if 'Phoenix' in df_celsius.columns:
        phoenix_2016 = df_celsius[df_celsius.index.year == 2016]
        if not phoenix_2016.empty:
            plt.scatter(phoenix_2016.index, phoenix_2016['Phoenix'].round(1), label='Phoenix')
        else:
            plt.scatter(df_celsius.index, df_celsius['Phoenix'].round(1), label='Phoenix')
    else:
        numeric_cols = df_celsius.select_dtypes(include=['number']).columns
        if len(numeric_cols) > 0:
            plt.scatter(df_celsius.index, df_celsius[numeric_cols[0]].round(1), label=numeric_cols[0])
            plt.title(f'Temperatura de {numeric_cols[0]}')
        else:
            plt.title('No hay columnas numéricas para graficar')

    plt.title('Temperatura en Phoenix durante 2016')
    plt.xlabel('Fecha')
    plt.ylabel('Temperatura (°C)')
    plt.legend()
    plt.grid()
    plt.savefig("temperatura_phoenix_2016.png")
    # plt.show()  # keep commented out for CI/headless runs

    df_celsius.to_csv("temperatura_celsius.csv")

if __name__ == "__main__":
    main()
