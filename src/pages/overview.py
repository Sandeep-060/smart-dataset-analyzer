import streamlit as st

def show_overview_page():
    """
    Displays the Dataset Overview page.
    """

    st.title("📊 Dataset Overview")

    # Check whether a dataset has been uploaded
    if st.session_state.dataframe is None:
        st.warning("⚠ Please upload a dataset from the Home page first.")
        return

    dataframe = st.session_state.dataframe
    st.success("Dataset loaded successfully!")

    # Dataset Information
    rows, columns = dataframe.shape
    memory_usage = dataframe.memory_usage(deep=True).sum()
    memory_kb = memory_usage / 1024
    st.markdown("### 📌 Dataset Information")
    st.info(f"**Dataset:** {st.session_state.dataset_name}")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            label="Rows",
            value=f"{rows:,}"
        )

    with col2:
        st.metric(
            label="Columns",
            value=columns
        )

    with col3:
        st.metric(
            label="Memory",
            value=f"{memory_kb:.2f} KB"
        )

    # Quick Summary
    st.markdown("### ⚡ Quick Summary")
    missing_values = dataframe.isnull().sum().sum()
    duplicate_rows = dataframe.duplicated().sum()
    numeric_columns = dataframe.select_dtypes(include="number").shape[1]
    categorical_columns = dataframe.select_dtypes(exclude="number").shape[1]

    summary1, summary2, summary3, summary4 = st.columns(4)
    with summary1:
        st.metric(
            "Missing Values",
            missing_values
        )

    with summary2:
        st.metric(
            "Duplicate Rows",
            duplicate_rows
        )

    with summary3:
        st.metric(
            "Numeric Columns",
            numeric_columns
        )

    with summary4:
        st.metric(
            "Categorical Columns",
            categorical_columns
        )


    # Column Data Types
    st.markdown("### 🧾 Column Data Types")
    st.caption("Data type detected for every column in the uploaded dataset.")
    dtype_dataframe = dataframe.dtypes.reset_index()
    dtype_dataframe.columns = ["Column", "Data Type"]
    dtype_dataframe["Data Type"] = dtype_dataframe["Data Type"].astype(str)
    st.dataframe(
        dtype_dataframe,
        width="stretch",
        hide_index=True
    )



    # Dataset Preview
    st.markdown("### 👀 Dataset Preview")
    st.caption("Preview the first few rows of your dataset.")
    preview_rows = st.slider(
        "Number of rows to preview",
        min_value=5,
        max_value=20,
        value=10
    )

    st.dataframe(
        dataframe.head(preview_rows),
        width="stretch",
        hide_index=True
    )