import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_calcular_crecimiento_prestamos():

    n_libraries = random.randint(2,5)
    n_years = random.randint(3,6)

    libraries = [f"library_{i}" for i in range(n_libraries)]
    years = list(range(2018, 2018 + n_years))

    data = []

    for lib in libraries:
        borrows = np.random.randint(1000,10000,size=n_years)
        for y,b in zip(years,borrows):
            data.append([lib,y,b])

    df = pd.DataFrame(data,columns=["library_id","year","borrow_count"])

    input_data = {"df": df.copy()}

    df_sorted = df.sort_values(["library_id","year"])
    df_sorted["growth_rate"] = df_sorted.groupby("library_id")["borrow_count"].pct_change()

    output_data = df_sorted

    return input_data, output_data
