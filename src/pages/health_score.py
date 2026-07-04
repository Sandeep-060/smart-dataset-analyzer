import streamlit as st

from src.services.health_score import calculate_health_score


def show_health_score_page():
    """
    Displays overall dataset health score.
    """

    st.title("❤️ Dataset Health Score")

    if st.session_state.dataframe is None:
        st.warning("⚠ Please upload a dataset first.")
        return

    df = st.session_state.dataframe

    result = calculate_health_score(df)

    st.success("Dataset analyzed successfully.")

    st.divider()

    # Overall Score
    st.subheader("Overall Health Score")

    st.metric(
        "Dataset Score",
        f"{result['Overall Score']}/100"
    )

    score = result["Overall Score"]

    if score >= 90:
        grade = "🟢 Excellent"
    elif score >= 75:
        grade = "🟡 Good"
    elif score >= 60:
        grade = "🟠 Fair"
    else:
        grade = "🔴 Poor"

    st.markdown(f"### {grade}")

    st.progress(result["Overall Score"] / 100)

    st.caption("""
        Score is calculated using:

        • Missing Values (20)
        • Duplicate Rows (20)
        • Outliers (20)
        • Dataset Structure (20)
        • ML Readiness (20)
        """)

    st.divider()

    # Score Breakdown
    st.subheader("Score Breakdown")

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("Missing", result["Missing Values"])
    c2.metric("Duplicates", result["Duplicate Rows"])
    c3.metric("Outliers", result["Outliers"])
    c4.metric("Structure",result["Dataset Completeness"])
    c5.metric("ML Ready",result["Feature Engineering"])

    st.divider()

    # Quality Indicators
    st.subheader("Quality Indicators")

    indicators = result["indicators"]

    for indicator in indicators:
        st.write(indicator)

    st.divider()

    # Improvement Suggestions
    st.subheader("Improvement Suggestions")

    suggestions = result["suggestions"]

    if len(suggestions) == 0:
        st.success("🎉 Excellent dataset. No major improvements required.")

    else:

        for suggestion in suggestions:
            st.warning(suggestion)