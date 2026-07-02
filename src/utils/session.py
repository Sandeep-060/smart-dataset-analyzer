import streamlit as st


def initialize_session_state():
    """
    Initialize all session state variables used throughout the application.
    This function runs only once per user session.
    """

    defaults = {
        "uploaded_file": None,
        "dataframe": None,
        "dataset_name": None,
        "analysis_completed": False,
        "current_page": "🏠 Home",
        "uploader_key": 0
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
