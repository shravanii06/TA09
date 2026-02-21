import pandas as pd
def preprocess_data(df):
    df=df.fillna(df.mean())

    df["temp_humidity_index"]=df["temperature"]*df["humidity"]
    df["rainfall_density"]=df["rainfall"]*df["population_density"]

    return df