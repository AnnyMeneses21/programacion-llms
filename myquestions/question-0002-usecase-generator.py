import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_detectar_libros_populares():

    n = random.randint(10,20)

    books = [f"book_{i}" for i in range(n)]
    authors = [f"author_{random.randint(1,5)}" for _ in range(n)]
    borrows = np.random.randint(100,5000,size=n)

    df = pd.DataFrame({
        "book_title": books,
        "author": authors,
        "borrow_count": borrows
    })

    factor = random.uniform(1.2,2.0)

    input_data = {
        "df": df.copy(),
        "factor": factor
    }

    mean_borrow = df["borrow_count"].mean()

    output_data = df[df["borrow_count"] > mean_borrow * factor]

    return input_data, output_data
