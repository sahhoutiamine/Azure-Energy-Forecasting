import pandas as pd

def azureml_main(dataframe1=None, dataframe2=None):

    df = dataframe1.copy()

    # Ensure correct data types
    df["Datetime"] = pd.to_datetime(
        df["Datetime"], errors="coerce"
    )

    df["PJME_MW"] = pd.to_numeric(
        df["PJME_MW"], errors="coerce"
    )

    # Remove invalid values
    df = df.dropna(subset=["Datetime", "PJME_MW"])

    # Sort chronologically
    df = df.sort_values("Datetime").reset_index(drop=True)

    # Feature Engineering
    df["Hour"] = df["Datetime"].dt.hour
    df["DayOfWeek"] = df["Datetime"].dt.dayofweek
    df["Month"] = df["Datetime"].dt.month
    df["Quarter"] = df["Datetime"].dt.quarter
    df["Year"] = df["Datetime"].dt.year
    df["DayOfYear"] = df["Datetime"].dt.dayofyear

    print("Dataset shape:", df.shape)
    print(df.head())

    return df,