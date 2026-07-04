import streamlit as st
from src.components.uploader import show_file_uploader


def show_home_page():
    """
    Displays the landing page of the Smart Dataset Analyzer.
    """

    # Hero Section
    st.title("📊 Smart Dataset Analyzer")

    st.markdown(
        """
Analyze your CSV datasets with professional **Exploratory Data Analysis (EDA)**,
data quality assessment, descriptive statistics, interactive visualizations,
correlation analysis, feature engineering recommendations, and an overall
dataset health score—all in one place.
"""
    )

    # st.markdown("---")

    # Features
    st.subheader("✨ What You Can Do")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
- 📁 Upload CSV Dataset
- 📊 Explore Dataset Structure
- 🧹 Analyze Data Quality
- 📈 Generate Descriptive Statistics
""")

    with col2:
        st.markdown("""
- 📉 Interactive Visualizations
- 🔗 Correlation Analysis
- ⚙️ Feature Engineering Suggestions
- ❤️ Dataset Health Score
""")

    # st.markdown("---")

    # Supported Files
    st.markdown("### 📄 Supported File")
    st.info("Currently, only **CSV (.csv)** files are supported.")
    
    # Upload Dataset
    st.markdown("### ⬆️ Upload Dataset")
    st.markdown("Choose a CSV dataset below to begin the complete analysis.")
    show_file_uploader()
    st.markdown("---")

    # Footer
    st.caption("Smart Dataset Analyzer • Version 1.0")