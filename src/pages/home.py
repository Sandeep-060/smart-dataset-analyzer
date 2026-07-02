import streamlit as st
from src.components.uploader import show_file_uploader


def show_home_page():
    """
    Displays the landing page of the Smart Dataset Analyzer.
    """

    # Hero Section
    st.title("📊 Smart Dataset Analyzer")
    st.markdown("""
    Analyze your CSV datasets with professional exploratory data analysis,
    data quality checks, descriptive statistics, visualizations,
    correlation analysis, feature engineering recommendations,
    and an overall dataset health score.
    """)
    st.divider()

    # Features
    st.subheader("✨ What You Can Do")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - 📁 Upload CSV Dataset
        - 📈 Dataset Overview
        - 🧹 Data Quality Analysis
        - 📊 Descriptive Statistics
        """)
    with col2:
        st.markdown("""
        - 📉 Visualizations
        - 🔗 Correlation Analysis
        - ⚙️ Feature Engineering Suggestions
        - ❤️ Dataset Health Score
        """)
    st.divider()

    # Supported Files
    st.subheader("📄 Supported File")
    st.info("Currently, only CSV (.csv) files are supported.")
    st.divider()

    # Upload Section
    st.subheader("⬆️ Upload Dataset")
    show_file_uploader()
    st.divider()

    # Footer
    st.caption("Smart Dataset Analyzer • Version 1.0")