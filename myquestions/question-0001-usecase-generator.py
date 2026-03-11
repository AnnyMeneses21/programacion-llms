import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_calcular_crecimiento_popularidad():

    n_groups = random.randint(2,5)
    n_years = random.randint(3,6)

    groups = [f"group_{i}" for i in range(n_groups)]
    years = list(range(2018, 2018 + n_years))

    data = []

    for g in groups:
        sales = np.random.randint(1000, 10000, size=n_years)
        for y, s in zip(years, sales):
            data.append([g, y, s])

    df = pd.DataFrame(data, columns=["group_name","year","album_sales"])

    input_data = {"df": df.copy()}

    df_sorted = df.sort_values(["group_name","year"])
    df_sorted["growth_rate"] = df_sorted.groupby("group_name")["album_sales"].pct_change()

    output_data = df_sorted

    return input_data, output_data
