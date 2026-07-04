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


# def show_sidebar():
#     """
#     Displays the sidebar and synchronizes
#     the selected page with Session State.
#     """

#     st.sidebar.title("📊 Navigation")

#     selected_page = st.sidebar.radio(
#         label="Go to",
#         options=PAGES,
#         index=PAGES.index(st.session_state.current_page)
#     )

#     # Update Session State
#     if selected_page != st.session_state.current_page:
#         st.session_state.current_page = selected_page
#         st.rerun()

#     return st.session_state.current_page



def show_sidebar():
    """
    Displays the sidebar and synchronizes
    the selected page with Session State.
    """

    with st.sidebar:

        st.markdown("## 📊 Navigation")
        st.caption("Smart Dataset Analyzer")
        selected_page = st.radio(
            "Navigation",
            options=PAGES,
            index=PAGES.index(st.session_state.current_page),
            label_visibility="collapsed"
        )
        st.divider()
        if st.session_state.dataframe is None:
            st.info("📂 Upload a CSV dataset to begin.")
        else:
            rows, cols = st.session_state.dataframe.shape
            st.success("Dataset Loaded")
            st.write(f"**{st.session_state.dataset_name}**")
            st.caption(f"{rows:,} Rows • {cols:,} Columns")

    if selected_page != st.session_state.current_page:
        st.session_state.current_page = selected_page
        st.rerun()

    return st.session_state.current_page