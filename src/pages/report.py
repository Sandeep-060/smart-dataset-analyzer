import streamlit as st

from src.services.report_generator import generate_pdf_report


def show_report_page():
    """
    Displays the report generation page.
    """

    st.title("📄 Dataset Analysis Report")

    if st.session_state.dataframe is None:
        st.warning("⚠ Please upload a dataset first.")
        return

    df = st.session_state.dataframe

    st.success("Dataset ready for report generation.")


    st.markdown("### 📑 Report Contents")

    st.caption(
        "The generated PDF provides a comprehensive summary of the uploaded dataset."
    )
    st.markdown("""
The generated PDF includes:

- 📁 Dataset Overview

- 📊 Descriptive Statistics

- 🧹 Missing Value Analysis

- ✅ Data Quality Summary

- 🔗 Correlation Summary

- ⚠ Outlier Detection Summary

- ⚙️ Feature Engineering Recommendations

- ❤️ Dataset Health Score

- 💡 Improvement Suggestions

""")
    st.info(
        "Interactive charts are excluded because they depend on user-selected columns and may not represent the entire dataset."
    )

    st.markdown("### 📥 Generate PDF Report")

    st.caption(
        "Generate and download a professional PDF report for the uploaded dataset."
    )
    if st.button(
        "Generate PDF Report",
        type="primary",
        use_container_width=True
    ):

        with st.spinner("Generating PDF..."):

            pdf_buffer = generate_pdf_report(df)

        st.success("Report generated successfully.")
        dataset_name = (
            st.session_state.dataset_name
            .rsplit(".", 1)[0]
            .replace(" ", "_")
        )
        st.download_button(
            label="📥 Download PDF Report",
            data=pdf_buffer,
            file_name=f"{dataset_name}_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )