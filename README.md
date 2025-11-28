[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/GTBl3wgV)
# Ejercicio: Análisis con archivos CSV - Temperatura


### 🎯 Objetivo
- Manipulación de DataFrames con Pandas.
- Creación y aplicación de funciones personalizadas (apply).
- Cálculo de estadísticas descriptivas (mínimo, máximo, promedio).
- Visualización de datos (Scatter plot).
- Exportación de datos a CSV.

### 📝 Descripción del Problema
El script carga un archivo CSV (data.csv) que contiene registros históricos de temperatura en grados Kelvin de tres ciudades distintas. El ejercicio consiste en convertir estas temperaturas a grados Celsius, analizar los datos de una ciudad específica (Phoenix), visualizar la variación de temperatura a lo largo del año y exportar los resultados a un nuevo archivo CSV.

## Instrucciones

Sigue los pasos a continuación para completar el ejercicio:

**1. Conversión de Unidades**

Crea una función llamada `kelvin_to_celsius` que acepte una temperatura en **Kelvin** y retorne su equivalente en **Celsius**.

$$C = K - 273.15$$

Posteriormente, aplica esta función a las columnas de las ciudades (San Diego, Phoenix, Toronto) y guarda los resultados en un nuevo DataFrame llamado `df_celsius`.

**2. Análisis de Datos (Phoenix)**

Utilizando el DataFrame transformado (`df_celsius`), calcula e imprime en consola los siguientes datos para la ciudad de Phoenix con su respectivo mensaje.  
**Nota:** redondea los resultados de temperatura a 2 decimales

1. ¿Qué día y a que hora se registró la temperatura mínima en Phoenix durante 2016?
   ```
   El día con la temperatura mínima en Phoenix fue: {fecha hora}
   ```

2. ¿Cuál fue la temperatura mínima registrada en Phoenix durante 2016?
   ```
   La temperatura mínima registrada en Phoenix fue de: {temperatura} °C
   ```

3. ¿Qué día y a que hora se registró la temperatura máxima en Phoenix durante 2016?
   ```
   El día con la temperatura máxima en Phoenix fue: {fecha hora}
   ```

4. ¿Cuál fue la temperatura máxima registrada en Phoenix durante 2016?
   ```
   La temperatura máxima registrada en Phoenix fue de: {temperatura} °C
   ```

5. ⁠Temperatura promedio del año en Phoenix
   ```
   La temperatura promedio durante 2016 en Phoenix fue de: {temperatura} °C
   ```

**3. Visualización**

Genera un gráfico de dispersión (*scatter plot*) que muestre la variación de la temperatura en Phoenix a lo largo del año. El código base ya incluye la configuración para graficar la temperatura de Phoenix.
- Debes guardar la gráfica generada como un archivo de imagen llamado: `temperatura_phoenix_2016.png`.

**4. Exportación**

Finalmente, exporta el DataFrame con las temperaturas ya convertidas a Celsius a un nuevo archivo CSV llamado `data_celsius.csv`.

### 🛠️ Resumen

El archivo de código contiene comentarios marcados como `# TODO` donde debes implementar las soluciones para cada uno de los pasos descritos anteriormente. Asegúrate de seguir las instrucciones cuidadosamente y de probar tu código para verificar que funciona correctamente antes de finalizar el ejercicio.

---

## 📂 Estructura del Repositorio

```
.
├── README                        # Instrucciones de la tarea [No modificar]
├── data.csv                      # Dataset original (Temperaturas en Kelvin)
├── main.py                       # Archivo para ejecutar el programa
├── .gitignore                    # Archivo para ignorar archivos en Git [No modificar]
├── requirements.txt              # Archivo para dependencias [No modificar]
├── disparador_autoevaluacion.py  # Archivo de respaldo para disparar la autoevaluación [Modificar solo si es necesario]
```