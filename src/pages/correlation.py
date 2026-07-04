import streamlit as st

from src.services.correlation_analyzer import (
    get_correlation_matrix,
    create_heatmap,
    get_strongest_relationships,
    create_scatter_plot

)


def show_correlation_page():

    st.title("🔗 Correlation Analysis")

    if st.session_state.dataframe is None:
        st.warning("⚠ Please upload a dataset first.")
        return

    dataframe = st.session_state.dataframe

    correlation_matrix = get_correlation_matrix(dataframe)

    if correlation_matrix is None:
        st.warning(
            "At least two numerical columns are required."
        )
        return

    st.success("Correlation analysis completed.")

    st.markdown("### 📋 Correlation Matrix")

    st.caption("Displays the correlation coefficient between every pair of numerical columns.")


    st.dataframe(
        correlation_matrix.round(2),
        width="stretch"
    )

    st.markdown("### 🔥 Correlation Heatmap")

    st.caption("Color intensity indicates the strength of correlation.")

    heatmap = create_heatmap(correlation_matrix)

    st.pyplot(heatmap)

    positive, negative = get_strongest_relationships(
        correlation_matrix
    )

    st.markdown("### 📈 Strongest Positive Relationships")

    st.caption("Highly positive correlated feature pairs.")
    st.dataframe(
        positive,
        width="stretch",
        hide_index=True
    )

    st.markdown("### 📉 Strongest Negative Relationships")
    st.caption("Highly negative correlated feature pairs.")

    st.dataframe(
        negative,
        width="stretch",
        hide_index=True
    )

    st.markdown("### 🎯 Interactive Scatter Plot")

    st.caption("Choose any two numerical columns to visualize their relationship.")

    numeric_columns = dataframe.select_dtypes(
        include="number"
    ).columns.tolist()

    if len(numeric_columns) < 2:
        st.warning("At least two numerical columns are required to create a scatter plot.")
        return

    col1, col2 = st.columns(2)

    with col1:
        x_column = st.selectbox(
            "X-axis",
            numeric_columns,
            key="scatter_x"
        )

    with col2:
        remaining_columns = [
            column
            for column in numeric_columns
            if column != x_column
        ]

        y_column = st.selectbox(
            "Y-axis",
            remaining_columns,
            key="scatter_y"
        )

    scatter = create_scatter_plot(
        dataframe,
        x_column,
        y_column
    )

    st.pyplot(scatter)