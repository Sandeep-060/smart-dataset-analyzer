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
    Displays the sidebar and synchronizes
    the selected page with Session State.
    """

    st.sidebar.title("📊 Navigation")

    selected_page = st.sidebar.radio(
        label="Go to",
        options=PAGES,
        index=PAGES.index(st.session_state.current_page)
    )

    # Update Session State
    if selected_page != st.session_state.current_page:
        st.session_state.current_page = selected_page
        st.rerun()

    return st.session_state.current_page

