import pandas as pd
from loguru import logger


def read_excel(filename: str):
    df = pd.ExcelFile(filename, engine='openpyxl')
    return df


def write_to_excel(df, filename: str):
    with pd.ExcelWriter(filename) as writer:
        df.to_excel(writer)
        logger.info(f"Результат записан в файл {filename}")
