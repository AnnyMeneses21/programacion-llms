import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_detectar_canciones_virales():

    n = random.randint(10,20)

    songs = [f"song_{i}" for i in range(n)]
    artists = [f"artist_{random.randint(1,5)}" for _ in range(n)]
    streams = np.random.randint(10000,1000000,size=n)

    df = pd.DataFrame({
        "song_name": songs,
        "artist": artists,
        "streams": streams
    })

    factor = random.uniform(1.2,2.0)

    input_data = {
        "df": df.copy(),
        "factor": factor
    }

    mean_streams = df["streams"].mean()
    output_data = df[df["streams"] > mean_streams * factor]

    return input_data, output_data
