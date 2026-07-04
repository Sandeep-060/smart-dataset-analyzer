import pandas as pd

from src.services.missing_analyzer import (
    analyze_missing_values,
    get_quality_summary,
)

from src.services.feature_engineering import (
    generate_feature_engineering_recommendations,
)

from src.services.outlier_detector import (
    detect_outliers_iqr,
)


def calculate_health_score(df: pd.DataFrame):
    """
    Calculates an overall dataset health score
    and returns detailed score breakdown.
    """

    # Missing Values
    missing_df = analyze_missing_values(df)

    total_missing = missing_df["Missing Values"].sum()

    total_cells = df.shape[0] * df.shape[1]

    if total_cells == 0:
        missing_percentage = 100
    else:
        missing_percentage = (
            total_missing / total_cells
        ) * 100

    missing_score = max(
        0,
        round(20 * (1 - missing_percentage / 100))
    )

    # Duplicate Rows
    quality = get_quality_summary(df)

    duplicate_rows = quality["duplicate_rows"]

    if len(df) == 0:
        duplicate_percentage = 100
    else:
        duplicate_percentage = (
            duplicate_rows / len(df)
        ) * 100

    duplicate_score = max(
        0,
        round(20 * (1 - duplicate_percentage / 100))
    )

    # Outliers
    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    outlier_percentages = []

    for column in numeric_columns:

        result = detect_outliers_iqr(df, column)

        outlier_percentages.append(
            result["percentage"]
        )

    if len(outlier_percentages) == 0:

        average_outlier_percentage = 0

    else:

        average_outlier_percentage = (
            sum(outlier_percentages)
            / len(outlier_percentages)
        )

    outlier_score = max(
        0,
        round(
            20 * (
                1 - average_outlier_percentage / 100
            )
        )
    )

    # Feature Engineering Readiness
    recommendations = (
        generate_feature_engineering_recommendations(df)
    )

    recommendation_count = len(recommendations)

    feature_score = max(
        0,
        round(
            20 * (1 - min(recommendation_count, 20) / 20)
        )
    )

    # Dataset Completeness
    completeness_score = 20

    if df.shape[0] < 30:
        completeness_score -= 5

    if df.shape[1] < 3:
        completeness_score -= 5

    if total_missing > 0:
        completeness_score -= 5

    if duplicate_rows > 0:
        completeness_score -= 5

    completeness_score = max(
        0,
        completeness_score
    )

    # Final Score

    total_score = (
        missing_score
        + duplicate_score
        + outlier_score
        + feature_score
        + completeness_score
    )

    indicators = []

    if missing_percentage < 5:
        indicators.append("✅ Very few missing values")
    else:
        indicators.append("⚠ Missing values present")

    if duplicate_rows == 0:
        indicators.append("✅ No duplicate rows")
    else:
        indicators.append(f"⚠ {duplicate_rows} duplicate rows found")

    if average_outlier_percentage < 5:
        indicators.append("✅ Very few outliers")
    else:
        indicators.append("⚠ Significant outliers detected")

    if recommendation_count <= 5:
        indicators.append("✅ Good ML readiness")
    else:
        indicators.append("⚠ Several preprocessing steps recommended")

    suggestions = []

    if missing_percentage >= 5:
        suggestions.append("Handle missing values before training.")

    if duplicate_rows > 0:
        suggestions.append("Remove duplicate rows.")

    if average_outlier_percentage >= 5:
        suggestions.append("Investigate outliers.")

    if recommendation_count > 5:
        suggestions.append("Apply recommended feature engineering.")

    return {
        "Overall Score": total_score,

        "Missing Values": missing_score,

        "Duplicate Rows": duplicate_score,

        "Outliers": outlier_score,

        "Feature Engineering": feature_score,

        "Dataset Completeness": completeness_score,

        "Missing Percentage": round(
            missing_percentage,
            2
        ),

        "Duplicate Percentage": round(
            duplicate_percentage,
            2
        ),

        "Average Outlier Percentage": round(
            average_outlier_percentage,
            2
        ),

        "Recommendation Count": recommendation_count,
        "indicators": indicators,
        "suggestions": suggestions
    }