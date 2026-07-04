import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def detect_outliers_iqr(dataframe, column):
    """
    Detect outliers using the IQR method.
    """

    series = dataframe[column].dropna()

    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    mask = (dataframe[column] < lower) | (dataframe[column] > upper)

    outliers = dataframe.loc[mask]

    return {
        "count": len(outliers),
        "percentage": round(len(outliers) / len(dataframe) * 100, 2),
        "lower": lower,
        "upper": upper,
        "outliers": outliers
    }

def detect_outliers_zscore(dataframe, column, threshold=3):
    """
    Detect outliers using Z-score.
    """

    series = dataframe[column]

    mean = series.mean()
    std = series.std()

    if std == 0:
        return {
            "count": 0,
            "percentage": 0,
            "threshold": threshold,
            "outliers": pd.DataFrame()
        }

    z_scores = np.abs((series - mean) / std)

    mask = z_scores > threshold

    outliers = dataframe.loc[mask]

    return {
        "count": len(outliers),
        "percentage": round(len(outliers) / len(dataframe) * 100, 2),
        "threshold": threshold,
        "outliers": outliers
    }


def create_outlier_boxplot(dataframe, column):
    """
    Creates a box plot for the selected numerical column.
    """

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.boxplot(
        dataframe[column].dropna(),
        vert=False,
        patch_artist=True
    )

    ax.set_title(f"Box Plot - {column}")
    ax.set_xlabel(column)

    plt.tight_layout()

    return fig