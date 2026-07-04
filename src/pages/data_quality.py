import streamlit as st

from src.services.missing_analyzer import (
    analyze_missing_values,
    get_quality_summary
)

def show_data_quality_page():
    """
    Displays missing value analysis.
    """

    st.title("🧹 Data Quality Analysis")

    # Check whether a dataset has been uploaded
    if st.session_state.dataframe is None:
        st.warning("⚠ Please upload a dataset first.")
        return

    # Get the uploaded DataFrame
    df = st.session_state.dataframe

    # Analyze missing values
    missing_df = analyze_missing_values(df)

    # Dataset Missing Summary
    total_missing = int(df.isna().sum().sum())
    columns_with_missing = int((df.isna().sum() > 0).sum())
    rows_with_missing = int(df.isna().any(axis=1).sum())
    total_cells = df.shape[0] * df.shape[1]
    completeness = (
        ((total_cells - total_missing) / total_cells) * 100
        if total_cells > 0
        else 100
    )


    st.markdown("### 📊 Missing Values Summary")
    st.caption("Overview of missing values detected in the uploaded dataset.")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(
            "Total Missing",
            total_missing
        )

    with col2:
        st.metric(
            "Affected Columns",
            columns_with_missing
        )

    with col3:
        st.metric(
            "Affected Rows",
            rows_with_missing
        )

    with col4:
        st.metric(
            "Completeness",
            f"{completeness:.2f}%"
        )

    st.markdown("### 📋 Missing Values by Column")
    st.caption("Shows the number of missing values present in every column.")

    st.dataframe(
        missing_df,
        width="stretch",
        hide_index=True
    )
    st.markdown("### 📈 Missing Values Visualization")

    chart_data = missing_df[missing_df["Missing Values"] > 0]

    if chart_data.empty:
        st.success("🎉 No missing values found in this dataset.")
    else:
        st.bar_chart(
            data=chart_data.set_index("Column")["Missing Values"],
            width="stretch"
        )
    

    st.markdown("### 📋 Dataset Quality Summary")

    st.caption("Additional quality indicators for the uploaded dataset.")

    summary = get_quality_summary(df)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Duplicate Rows",
            summary["duplicate_rows"]
        )

        st.metric(
            "Duplicate Columns",
            summary["duplicate_columns"]
        )



    with col2:

        st.metric(
            "Constant Columns",
            summary["constant_columns"]
        )
        
        st.metric(
            "Memory Heavy Columns",
            len(summary["heavy_columns"])
        )



    st.markdown("### 💾 Memory Heavy Columns")

    st.caption("Columns consuming relatively higher memory.")
    if len(summary["heavy_columns"]) == 0:
        st.success("No memory-heavy columns found.")
    else:

        memory_df = (
            summary["heavy_columns"]
            .reset_index()
        )

        memory_df.columns = [
            "Column",
            "Memory (MB)"
        ]

        memory_df["Memory (MB)"] = (
            memory_df["Memory (MB)"]
            .round(2)
        )

        st.dataframe(
            memory_df,
            width="stretch",
            hide_index=True
        )