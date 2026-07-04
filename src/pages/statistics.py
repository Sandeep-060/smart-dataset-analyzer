import streamlit as st
from src.services.statistics_analyzer import (
    calculate_statistics,
    calculate_categorical_statistics,
)

def show_statistics_page():
    """
    Displays numerical statistics
    for uploaded datasets.
    """

    st.title("📊 Statistics")

    # Check dataset
    if st.session_state.dataframe is None:
        st.warning("⚠ Please upload a dataset first.")
        return

    df = st.session_state.dataframe

    st.success("Dataset loaded successfully!")


    st.markdown("### 🔢 Numerical Statistics")
    st.caption("Select a numerical column to view descriptive statistical .")

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    if len(numeric_columns) == 0:
        st.error("No numerical columns found.")
        return

    selected_column = st.selectbox(
        "Choose a column",
        numeric_columns
    )


    statistics = calculate_statistics(df[selected_column])

    st.markdown(f"### 📈 Statistics for **{selected_column}**")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Mean", f"{statistics['Mean']:.2f}")
        st.metric("Variance", f"{statistics['Variance']:.2f}")
        st.metric("Minimum", statistics["Minimum"])
        st.metric("Q1", f"{statistics['Q1']:.2f}")

    with col2:
        st.metric("Median", f"{statistics['Median']:.2f}")
        st.metric(
            "Std Deviation",
            f"{statistics['Standard Deviation']:.2f}"
        )
        st.metric("Maximum", statistics["Maximum"])
        st.metric("Q3", f"{statistics['Q3']:.2f}")

 
    with col3:
        st.metric("Mode", statistics["Mode"])
        st.metric("IQR", f"{statistics['IQR']:.2f}")
        st.metric("Skewness", f"{statistics['Skewness']:.2f}")
        st.metric("Kurtosis", f"{statistics['Kurtosis']:.2f}")



    st.markdown("### 🏷️ Categorical Statistics")
    st.caption("Select a categorical column to explore category distribution.")
    categorical_columns = df.select_dtypes(exclude="number").columns.tolist()
    if len(categorical_columns) == 0:
        st.info("No categorical columns found.")
        return
    selected_category = st.selectbox(
            "Choose a categorical column",
            categorical_columns
        )
    category_statistics = calculate_categorical_statistics(
                        df[selected_category]
                        )
    
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Unique Values",
            category_statistics["Unique Values"]
        )

    with col2:
        st.metric(
            "Most Common",
            category_statistics["Most Common"]
        )
    st.markdown("### 📋 Frequency Table")

    st.caption("Frequency distribution of values in the selected categorical .")
    st.dataframe(
        category_statistics["Frequency Table"],
        width="stretch",
        hide_index=True
    )

