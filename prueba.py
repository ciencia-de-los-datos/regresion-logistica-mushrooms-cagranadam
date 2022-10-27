import pandas as pd
   
   # Lea el archivo `mushrooms.csv` y asignelo al DataFrame `df`
df = pd.read_csv('mushrooms.csv')

    # Remueva la columna `veil-type` del DataFrame `df`.
    # Esta columna tiene un valor constante y no sirve para la detección de hongos.
df.drop("veil_type", axis=1)

    # Asigne la columna `type` a la variable `y`.
y = df["type"]

    # Asigne una copia del dataframe `df` a la variable `X`.
X = df.copy()

    # Remueva la columna `type` del DataFrame `X`.
X.drop("type", axis=1)

    # Retorne `X` y `y`
print(X)