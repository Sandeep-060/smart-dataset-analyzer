import streamlit as st

from src.services.feature_engineering import (
    generate_feature_engineering_recommendations,
)


def show_feature_engineering_page():

    st.title("⚙ Feature Engineering Recommendations")

    if st.session_state.dataframe is None:
        st.warning("⚠ Please upload a dataset first.")
        return

    df = st.session_state.dataframe

    recommendations = generate_feature_engineering_recommendations(df)

    st.success("Dataset loaded successfully!")


    st.markdown("### 📊 Recommendation Summary")

    st.caption("Overview of potential feature engineering improvements identified in the dataset.")
    total = len(recommendations)

    missing = (recommendations["Issue"] == "Missing Values").sum()

    encoding = recommendations["Issue"].str.contains(
        "Cardinality",
        case=False,
        na=False,
    ).sum()

    scaling = (recommendations["Issue"] == "Wide Value Range").sum()

    dates = (recommendations["Issue"] == "Date Feature").sum()

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("Total", total)
    c2.metric("Missing", missing)
    c3.metric("Encoding", encoding)
    c4.metric("Scaling", scaling)
    c5.metric("Date", dates)


    st.markdown("### 💡 Recommendations")

    st.caption(
        "Review the suggested preprocessing and feature engineering steps before training machine learning models."
    )
    if recommendations.empty:

        st.success("🎉 No feature engineering recommendations found.")

    else:

        st.dataframe(
            recommendations,
            width="stretch",
            hide_index=True,
        )