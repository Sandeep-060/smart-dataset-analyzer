import streamlit as st

from src.services.outlier_detector import (
    detect_outliers_iqr,
    detect_outliers_zscore,
    create_outlier_boxplot
)

def show_outliers_page():
    """
    Displays the Outlier Detection page.
    """

    st.title("⚠ Outlier Detection")

    # Dataset check
    if st.session_state.dataframe is None:
        st.warning("⚠ Please upload a dataset first.")
        return

    dataframe = st.session_state.dataframe

    numeric_columns = dataframe.select_dtypes(
        include="number"
    ).columns.tolist()

    if len(numeric_columns) == 0:
        st.warning("No numerical columns found.")
        return

    st.success("Dataset loaded successfully.")

    st.markdown("### ⚙️ Detection Settings")

    st.caption("Select a numerical column and choose an outlier detection method.")
    # Column Selection
    selected_column = st.selectbox(
        "Select Numerical Column",
        numeric_columns
    )

    # Method Selection
    method = st.radio(
        "Choose Detection Method",
        [
            "IQR",
            "Z-Score"
        ],
        horizontal=True
    )

    # Detection
    if method == "IQR":
        result = detect_outliers_iqr(
            dataframe,
            selected_column
        )
    else:
        result = detect_outliers_zscore(
            dataframe,
            selected_column
        )

    # Summary Cards

    st.markdown("### 📊 Detection Summary")

    st.caption("Summary of the detected outliers for the selected column.")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Outliers Found",
            result["count"]
        )

    with col2:
        st.metric(
            "Percentage",
            f'{result["percentage"]}%'
        )

    # Method Information
    st.markdown(f"### 🔍 {method} Details")

    if method == "IQR":

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Lower Limit",
                f"{result['lower']:.2f}"
            )

        with col2:
            st.metric(
                "Upper Limit",
                f"{result['upper']:.2f}"
            )

    else:

        st.metric(
            "Z-Score Threshold",
            result["threshold"]
        )

    # Outlier Table

    st.markdown("### 📋 Detected Outliers")

    st.caption("Rows identified as outliers using the selected detection method.")
    if result["outliers"].empty:

        st.success(
            "🎉 No outliers detected."
        )

    else:


        display_df = result["outliers"][[selected_column]].copy()
        display_df.insert(0, "Row Index", result["outliers"].index)

        st.dataframe(
            display_df,
            width="stretch",
            hide_index=True
        )
    st.markdown("### 📦 Box Plot")

    st.caption("Visual representation of the data distribution and detected outliers.")
    figure = create_outlier_boxplot(
        dataframe,
        selected_column
    )

    st.pyplot(figure)