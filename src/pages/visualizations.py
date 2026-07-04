import streamlit as st

from src.services.visualization_service import (
    get_numerical_columns,
    get_categorical_columns,
    create_histogram,
    create_boxplot,
    create_kde_plot,
    create_bar_chart,
    create_missing_value_chart
)

def show_visualization_page():
    """
    Visualization Dashboard
    """

    st.title("📈 Dataset Visualizations")

    if st.session_state.dataframe is None:
        st.warning("⚠ Please upload a dataset first.")
        return

    dataframe = st.session_state.dataframe

    st.success("Dataset loaded successfully!")

    numerical_columns = get_numerical_columns(dataframe)
    categorical_columns = get_categorical_columns(dataframe)

    st.markdown("### 📊 Numerical Visualizations")
    st.caption("Visualize the distribution and spread of numerical columns.")

    if numerical_columns:

        selected_numeric = st.selectbox(
            "Select Numerical Column",
            numerical_columns
        )

        st.markdown("### 📊 Histogram")
        histogram = create_histogram(dataframe,selected_numeric)
        st.pyplot(histogram)

        st.markdown("### 📈 KDE Plot")
        kde = create_kde_plot(dataframe,selected_numeric)
        st.pyplot(kde)

        st.markdown("### 📦 Box Plot")
        boxplot = create_boxplot(dataframe,selected_numeric)
        st.pyplot(boxplot)

    else:

        st.warning("No numerical columns found.")


    st.markdown("### 🏷️ Categorical Visualization")
    st.caption("Visualize the frequency distribution of categorical values.")
    categorical_columns = dataframe.select_dtypes(exclude="number").columns.tolist()

    if categorical_columns:
        selected_category = st.selectbox(
            "Select Categorical Column",
            categorical_columns
        )

        bar = create_bar_chart(
            dataframe,
            selected_category
        )

        st.pyplot(bar)

    else:

        st.info("No categorical columns found.")

    st.markdown("### 🧹 Missing Value Visualization")
    st.caption("Identify columns containing missing values.")
    missing_chart = create_missing_value_chart(dataframe)

    if missing_chart is None:
        st.success("🎉 No missing values found.")
    else:
        st.pyplot(missing_chart)