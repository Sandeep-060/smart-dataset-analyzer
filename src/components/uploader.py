import streamlit as st

from src.services.dataset_loader import load_dataset
from src.services.validator import validate_dataset


def show_file_uploader():
    """
    Displays the CSV uploader and keeps the uploaded
    dataset available using Session State.
    """

    uploaded_file = st.file_uploader(
        "📂 Upload your dataset",
        type=["csv"],
        help="Only CSV files are supported.",
        key=f"file_uploader_{st.session_state.uploader_key}"
    )

    # New Upload
    if uploaded_file is not None:
        
        try:
          dataframe = load_dataset(uploaded_file)
          is_valid, message = validate_dataset(dataframe)
        except ValueError as e:
              st.error(str(e))
              return
        if is_valid:
            st.session_state.uploaded_file = uploaded_file
            st.session_state.dataframe = dataframe
            st.session_state.dataset_name = uploaded_file.name
        else:
            st.error(message)
            st.session_state.uploaded_file = None
            st.session_state.dataframe = None
            st.session_state.dataset_name = None

    # Display Dataset Information
    if st.session_state.dataframe is not None:
        st.success("✅ Dataset uploaded successfully!")
        st.info(f"📄 Dataset : {st.session_state.dataset_name}")
        st.info(
            f"📊 Rows : {st.session_state.dataframe.shape[0]} | "
            f"Columns : {st.session_state.dataframe.shape[1]}"
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button("📊 Go to Dataset Overview", width="stretch"):
                st.session_state.current_page = "📁 Dataset Overview"
                st.rerun()

        with col2:
            if st.button("🗑 Clear Dataset", width="stretch"):
                clear_uploaded_file()


def clear_uploaded_file():
    """
    Clears the uploaded dataset and resets the uploader widget.
    """
    st.session_state.uploaded_file = None
    st.session_state.dataframe = None
    st.session_state.dataset_name = None

    # Force Streamlit to create a brand-new uploader widget
    st.session_state.uploader_key += 1

    st.rerun()