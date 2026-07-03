import pandas as pd
import matplotlib.pyplot as plt

def get_numerical_columns(dataframe):
    """
    Returns all numerical columns.
    """

    return dataframe.select_dtypes(include="number").columns.tolist()

def get_categorical_columns(dataframe):
    """
    Returns all categorical columns.
    """

    return dataframe.select_dtypes(exclude="number").columns.tolist()


def create_histogram(dataframe, column):
    """
    Creates a Histogram.
    """

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.hist(
        dataframe[column].dropna(),
        bins=20
    )

    ax.set_title(f"Histogram - {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")

    return fig


def create_boxplot(dataframe, column):
    """
    Creates a Box Plot.
    """

    fig, ax = plt.subplots(figsize=(8, 2))

    ax.boxplot(
        dataframe[column].dropna(),
        vert=False
    )

    ax.set_title(f"Box Plot - {column}")

    return fig


def create_kde_plot(dataframe, column):
    """
    Creates a KDE Plot.
    """

    fig, ax = plt.subplots(figsize=(8, 4))

    dataframe[column].dropna().plot(
        kind="density",
        ax=ax
    )

    ax.set_title(f"KDE Plot - {column}")
    ax.set_xlabel(column)

    return fig

def create_missing_value_chart(dataframe):
    """
    Creates a bar chart showing
    missing values in each column.
    """

    missing = dataframe.isnull().sum()

    missing = missing[missing > 0]

    if missing.empty:
        return None

    fig, ax = plt.subplots(figsize=(8, 4))

    missing.sort_values(ascending=False).plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Missing Values by Column")
    ax.set_xlabel("Columns")
    ax.set_ylabel("Missing Count")

    plt.xticks(rotation=45)

    return fig

def create_bar_chart(dataframe, column):
    """
    Creates a bar chart for
    categorical columns.
    """

    counts = dataframe[column].value_counts()

    fig, ax = plt.subplots(figsize=(8, 4))

    counts.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(f"Bar Chart - {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")

    plt.xticks(rotation=45)

    return fig