import streamlit as st
import json
from collections import Counter

# Load quiz data from JSON
with open("data/comm_through_clusters_quiz.json", "r") as f:
    quiz = json.load(f)

st.set_page_config(page_title="Comm-Through Cluster Quiz", page_icon="✨", layout="centered")
st.title("✨ Comm-Through Cluster Quiz")
st.write("Discover your communication avatar — Vision Weaver, Bridge Builder, Truth Speaker, or Momentum Mover.")

# Session state to track progress
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "answers" not in st.session_state:
    st.session_state.answers = []

questions = quiz["questions"]

# Display questions one at a time
if st.session_state.current_q < len(questions):
    q = questions[st.session_state.current_q]
    st.subheader(f"Q{q['id']}: {q['text']}")
    
    options = [opt["answer"] for opt in q["options"]]
    choice = st.radio("Choose one:", options, key=f"q{q['id']}")
    
    if st.button("Next"):
        # Find which cluster this choice maps to
        for opt in q["options"]:
            if opt["answer"] == choice:
                st.session_state.answers.append(opt["cluster"])
        st.session_state.current_q += 1
        st.rerun()

# Show results at the end
else:
    st.subheader("🎉 Your Comm-Through Cluster Result")
    counts = Counter(st.session_state.answers)
    result = counts.most_common(1)[0][0]  # Get the top cluster
    
    st.success(f"✨ You are a **{result}**!")
    
    # Avatar descriptions
    descriptions = {
        "Vision Weaver": "Creativity, big-picture thinking, inspiration. Growth: anchor vision in steps.",
        "Bridge Builder": "Harmony, connection, mediation. Growth: balance others with your own voice.",
        "Truth Speaker": "Bold honesty, clarity, courage. Growth: add empathy to your truth.",
        "Momentum Mover": "Action, energy, forward-drive. Growth: slow down and create space for others."
    }
    
    st.write(descriptions.get(result, "Unknown cluster"))
    
    if st.button("Restart Quiz"):
        st.session_state.current_q = 0
        st.session_state.answers = []
        st.rerun()

