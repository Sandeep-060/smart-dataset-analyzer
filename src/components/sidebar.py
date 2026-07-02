import streamlit as st

PAGES = [
    "🏠 Home",
    "📁 Dataset Overview",
    "🧹 Data Quality",
    "📊 Statistics",
    "📈 Visualizations",
    "🔗 Correlation",
    "⚠ Outlier Detection",
    "⚙ Feature Engineering",
    "❤️ Health Score",
    "📄 Report"
]

def show_sidebar():
    """
    Displays the application's sidebar
    and returns the selected page.
    """
    st.sidebar.title("📊 Navigation")
    selected_page = st.sidebar.radio(
        label="Go to",
        options=PAGES
    )
    return selected_page