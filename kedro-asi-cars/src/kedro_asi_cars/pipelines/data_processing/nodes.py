import numpy as np
import pandas as pd


def generate_age_feature(df: pd.DataFrame) -> pd.DataFrame:
    dataset_creation_year = 2022
    df['age_years'] = dataset_creation_year - df['year']
    return df


def generate_mileage_per_year_feature(df: pd.DataFrame) -> pd.DataFrame:
    df = df.replace([np.inf, -np.inf], np.nan).dropna()
    df['safe_age_years'] = df['age_years'].replace(0, 1)  # dzielenie przez zero
    df['mileage_per_year'] = (df['mileage'] / df['safe_age_years']).astype(int)
    df.drop(columns='safe_age_years', inplace=True)

    return df

def deleteOutliers(df: pd.DataFrame) -> pd.DataFrame:
    df = deleteOutliersHelper(df, 'price')
    df = deleteOutliersHelper(df, 'mileage')
    df = deleteOutliersHelper(df, 'vol_engine')
    return df

def deleteUnimportantColumns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(df.columns[0], axis=1) # usuwamy kolumnę 0 - licznik wierszy
    df = df.drop(columns=['city'])
    return df

def deleteGeneration(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(columns=['generation_name'])
    return df

def deleteYear(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop(columns=['year'])
    return df

def deleteOutliersHelper(df, field):
    Q1 = df[field].quantile(0.25)
    Q3 = df[field].quantile(0.75)
    IQR = Q3 - Q1
    return df[(df[field] >= Q1 - 1.5 * IQR) & (df[field] <= Q3 + 1.5 * IQR)] # usuwanie outlierów