import pandas as pd
from pandas.api.types import (
    is_numeric_dtype,
    is_datetime64_any_dtype,
)


def generate_feature_engineering_recommendations(df):
    """
    Generate feature engineering recommendations
    without modifying the dataset.
    """

    recommendations = []

    total_rows = len(df)

    for column in df.columns:

        series = df[column]

        dtype = str(series.dtype)

        # Identifier Detection
        column_lower = column.lower()

        if (
            "id" == column_lower
            or column_lower.endswith("_id")
            or column_lower.endswith("id")
        ):
            recommendations.append({
                "Column": column,
                "Type": "Identifier",
                "Issue": "Identifier Column",
                "Recommendation": "Exclude from Machine Learning Features",
                "Reason":
                      "Unique identifier. Usually excluded from ML features."
            })

            continue

        # Missing Values
        missing_count = series.isna().sum()

        if missing_count > 0:

            missing_percent = (missing_count / total_rows) * 100

            if missing_percent < 5:

                recommendation = (
                    "Consider dropping affected rows "
                    "or simple imputation"
                )

               
                reason = (
                    f"{missing_percent:.1f}% missing. "
                    "Drop affected rows or use simple imputation."
                )

            elif missing_percent < 30:

                if is_numeric_dtype(series):

                    recommendation = "Median Imputation"

                    reason = (
                        f"{missing_percent:.1f}% missing. "
                        "Median handles outliers well."
                    )

                else:

                    recommendation = "Mode Imputation"

                    reason = (
                        f"{missing_percent:.1f}% missing. "
                        "Mode suits categorical columns."
                    )

            else:

                recommendation = (
                    "Consider dropping this feature "
                    "or using advanced imputation"
                )

                reason = (
                    f"{missing_percent:.1f}% missing. "
                    "A large portion of the column is missing, "
                    "so evaluate whether the feature is useful."
                )

            recommendations.append({
                "Column": column,
                "Type": dtype,
                "Issue": "Missing Values",
                "Recommendation": recommendation,
                "Reason": reason
            })

        # Encoding Recommendation
        if not is_numeric_dtype(series):

            unique_values = series.nunique(dropna=True)

            if unique_values <= 10:

                recommendations.append({
                    "Column": column,
                    "Type": "Categorical",
                    "Issue": "Low Cardinality",
                    "Recommendation": "One-Hot Encoding",
                    "Reason":f"{unique_values} categories. Good for One-Hot Encoding."
                })

            elif unique_values <= 50:

                recommendations.append({
                    "Column": column,
                    "Type": "Categorical",
                    "Issue": "Medium Cardinality",
                    "Recommendation": "Ordinal / Label Encoding (if appropriate)",
                    "Reason":f"{unique_values} categories. Use Label/Ordinal Encoding if ordered."
                })

            else:

                recommendations.append({
                    "Column": column,
                    "Type": "Categorical",
                    "Issue": "High Cardinality",
                    "Recommendation": "Frequency Encoding",
                    "Reason":f"{unique_values} categories. One-Hot Encoding is inefficient."
                })

        # Scaling Recommendation
        if is_numeric_dtype(series):

            if series.nunique() <= 1:
                continue

            value_range = series.max() - series.min()

            if value_range > 1000:

                recommendations.append({
                    "Column": column,
                    "Type": "Numerical",
                    "Issue": "Wide Value Range",
                    "Recommendation": "StandardScaler or MinMaxScaler",
                    "Reason":"Large value range. Scaling is recommended."
                })

        # Date Features
        if (
            is_datetime64_any_dtype(series)
            or "date" in column.lower()
            or "time" in column.lower()
        ):

            recommendations.append({
                "Column": column,
                "Type": "Date",
                "Issue": "Date Feature",
                "Recommendation":
                    "Extract Year, Month, Day, Weekday or other useful components",
                "Reason":"Extract useful time-based features."
            })

    if len(recommendations) == 0:

        return pd.DataFrame(columns=[
            "Column",
            "Type",
            "Issue",
            "Recommendation",
            "Reason"
        ])

    return pd.DataFrame(recommendations)