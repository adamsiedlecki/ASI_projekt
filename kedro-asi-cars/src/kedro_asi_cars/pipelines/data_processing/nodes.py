import pandas as pd


def generate_age_feature(df: pd.DataFrame) -> pd.DataFrame:
    dataset_creation_year = 2022
    df['age_years'] = dataset_creation_year - df['year']
    return df


def generate_mileage_per_year_feature(df: pd.DataFrame) -> pd.DataFrame:
    df['mileage_per_year'] = df['mileage'] / df['age_years']
    return df
