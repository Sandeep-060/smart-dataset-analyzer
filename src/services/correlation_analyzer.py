import pandas as pd
import matplotlib.pyplot as plt


def get_correlation_matrix(dataframe):
    """
    Returns the Pearson correlation matrix
    for all numerical columns.
    """

    numeric_df = dataframe.select_dtypes(include="number")

    if numeric_df.shape[1] < 2:
        return None

    return numeric_df.corr()


def create_heatmap(correlation_matrix):
    """
    Creates a correlation heatmap.
    """

    fig, ax = plt.subplots(figsize=(8, 6))

    image = ax.imshow(
        correlation_matrix,
        interpolation="nearest",
        aspect="auto"
    )

    ax.set_xticks(range(len(correlation_matrix.columns)))
    ax.set_xticklabels(
        correlation_matrix.columns,
        rotation=45,
        ha="right"
    )

    ax.set_yticks(range(len(correlation_matrix.columns)))
    ax.set_yticklabels(correlation_matrix.columns)

    plt.colorbar(image)

    plt.tight_layout()

    return fig


def get_strongest_relationships(correlation_matrix):
    """
    Returns strongest positive and negative
    relationships.
    """

    corr = correlation_matrix.copy()

    # Remove self correlations
    for i in range(len(corr)):
        corr.iat[i, i] = None

    pairs = (
        corr.stack()
            .reset_index()
    )

    pairs.columns = [
        "Column A",
        "Column B",
        "Correlation"
    ]

    # Remove duplicate pairs
    pairs["Pair"] = pairs.apply(
        lambda row: tuple(
            sorted([row["Column A"], row["Column B"]])
        ),
        axis=1
    )

    pairs = pairs.drop_duplicates("Pair")

    pairs = pairs.drop(columns="Pair")

    positive = (
        pairs[pairs["Correlation"] > 0]
        .sort_values(
            by="Correlation",
            ascending=False
        )
        .head(10)
    )

    negative = (
        pairs[pairs["Correlation"] < 0]
        .sort_values(
            by="Correlation"
        )
        .head(10)
    )

    return positive, negative


def create_scatter_plot(dataframe, x_column, y_column):
    """
    Creates a scatter plot between two
    numerical columns.
    """

    fig, ax = plt.subplots(figsize=(7, 5))

    plot_df = dataframe[[x_column, y_column]].dropna()

    ax.scatter(
        plot_df[x_column],
        plot_df[y_column],
        alpha=0.7
    )

    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_title(f"{x_column} vs {y_column}")

    plt.tight_layout()

    return fig