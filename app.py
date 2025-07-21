import streamlit as st

def main():
    st.title("🔍 Soft Skills Feedback Quality Evaluator")
    st.markdown("Rate the following criteria from **1 (Poor)** to **4 (Excellent)**")

    st.markdown("---")

    criteria = {
        "Clarity": "Is the feedback clear and understandable?",
        "Specificity": "Does it include concrete examples?",
        "Constructiveness": "Does it give helpful suggestions?",
        "Balanced Tone": "Does it include both positives and areas to improve?",
        "Actionability": "Are the suggestions practical and doable?"
    }

    scores = {}
    total_score = 0

    for key, description in criteria.items():
        score = st.slider(f"{key}: {description}", min_value=1, max_value=4, value=3)
        scores[key] = score
        total_score += score

    st.markdown("---")

    if st.button("Evaluate Feedback Quality"):
        st.subheader("📝 Evaluation Summary")

        for key, score in scores.items():
            st.write(f"**{key}**: {score}/4")

        avg_score = total_score / len(criteria)
        st.markdown(f"### 📊 Average Score: `{avg_score:.2f}/4`")

        if avg_score >= 3.5:
            st.success("✅ **Feedback Quality: Excellent**")
        elif avg_score >= 2.5:
            st.info("👍 **Feedback Quality: Good**")
        elif avg_score >= 1.5:
            st.warning("⚠️ **Feedback Quality: Needs Improvement**")
        else:
            st.error("❌ **Feedback Quality: Poor**")

if __name__ == "__main__":
    main()
