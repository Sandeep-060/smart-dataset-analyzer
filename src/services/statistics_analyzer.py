import pandas as pd


def calculate_statistics(series: pd.Series):
    """
    Calculates descriptive statistics
    for a numerical column.

    Parameters
    ----------
    series : pandas.Series

    Returns
    -------
    dict
    """

    # Remove missing values
    series = series.dropna()

    mode_values = series.mode()

    if len(mode_values) == 0:
        mode = "No Mode"
    else:
        mode = ", ".join(map(str, mode_values.tolist()))
        if len(mode_values) == 1:
            mode = str(mode_values.iloc[0])

        elif len(mode_values) <= 3:
            mode = ", ".join(map(str, mode_values.tolist()))

        else:
            mode = f"{mode_values.iloc[0]}, {mode_values.iloc[1]} + {len(mode_values)-2} more"

    statistics = {
        "Mean": series.mean(),
        "Median": series.median(),
        "Mode": mode,
        "Variance": series.var(),
        "Standard Deviation": series.std(),
        "Minimum": series.min(),
        "Maximum": series.max(),
        "Q1": series.quantile(0.25),
        "Q3": series.quantile(0.75),
        "IQR": series.quantile(0.75) - series.quantile(0.25),
        "Skewness": series.skew(),
        "Kurtosis": series.kurt()
    }

    return statistics

def calculate_categorical_statistics(series: pd.Series):
    """
    Calculates statistics for a categorical column.
    """

    series = series.dropna()

    frequencies = series.value_counts()

    return {
        "Unique Values": series.nunique(),
        "Most Common": frequencies.index[0],
        "Frequency Table": frequencies.reset_index().rename(
            columns={
                "index": "Category",
                series.name: "Count"
            }
        )
    }

def get_dataset_statistics_summary(df: pd.DataFrame):
    """
    Returns overall dataset statistics
    (not column-wise).
    """

    memory = (
        df.memory_usage(deep=True).sum()
        / (1024 * 1024)
    )

    return {
        "Rows": len(df),
        "Columns": df.shape[1],
        "Numerical Columns":
            len(df.select_dtypes(include="number").columns),
        "Categorical Columns":
            len(df.select_dtypes(exclude="number").columns),
        "Memory (MB)": round(memory, 2)
    }