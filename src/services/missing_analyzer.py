import pandas as pd


def analyze_missing_values(df: pd.DataFrame) :
    """
    Returns a DataFrame containing
    missing value statistics for each column.
    """

    missing_count = df.isnull().sum()

    missing_percentage = (missing_count / len(df)) * 100

    result = pd.DataFrame({
        "Column": df.columns,
        "Missing Values": missing_count.values,
        "Missing %": missing_percentage.values
    })

    return result


def get_quality_summary(df):
    """
    Returns overall dataset quality information.
    """

    duplicate_rows = df.duplicated().sum()
    duplicate_columns = df.columns.duplicated().sum()
    constant_columns = (df.nunique(dropna=False) <= 1).sum()

    memory_usage = (
        df.memory_usage(deep=True)
        / (1024 ** 2)
    )

    heavy_columns = memory_usage[memory_usage > 1]

    return {
        "duplicate_rows": duplicate_rows,
        "duplicate_columns": duplicate_columns,
        "constant_columns": constant_columns,
        "heavy_columns": heavy_columns
    }