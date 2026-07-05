import streamlit as st
from src.components.sidebar import show_sidebar
from src.navigation.router import route_page
from src.utils.session import initialize_session_state
from pathlib import Path



st.set_page_config(
    page_title="Smart Dataset Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


def load_css():
    """
    Loads global CSS styling.
    """


    css_file = Path(__file__).parent / "src" / "styles" / "style.css"

    with open(css_file) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

def main():
    initialize_session_state()
    load_css()
    selected_page = show_sidebar()
    route_page(selected_page)

if __name__ == "__main__":
    main()