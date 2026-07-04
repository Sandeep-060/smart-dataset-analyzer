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

    st.divider()


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

    st.divider()

    # Summary Cards

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

    st.divider()

    # Method Information
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

    st.divider()

    # Outlier Table

    st.subheader("Detected Outliers")

    if result["outliers"].empty:

        st.success(
            "🎉 No outliers detected."
        )

    else:

        # st.dataframe(
        #     result["outliers"],
        #     width="stretch",
        #     hide_index=True
        # )

        display_df = result["outliers"][[selected_column]].copy()
        display_df.insert(0, "Row Index", result["outliers"].index)

        st.dataframe(
            display_df,
            width="stretch",
            hide_index=True
        )
    st.divider()

    st.subheader("Box Plot")

    figure = create_outlier_boxplot(
        dataframe,
        selected_column
    )

    st.pyplot(figure)