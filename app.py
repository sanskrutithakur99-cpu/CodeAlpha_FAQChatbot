import json
from pathlib import Path

import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="Student FAQ Chatbot",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student FAQ Chatbot")
st.caption("An NLP-powered chatbot built for the CodeAlpha AI Internship")

FAQ_FILE = Path(__file__).parent / "faqs.json"

with open(FAQ_FILE, "r", encoding="utf-8") as file:
    faq_data = json.load(file)["faqs"]

questions = [item["question"] for item in faq_data]
answers = [item["answer"] for item in faq_data]

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1, 2)
)
question_vectors = vectorizer.fit_transform(questions)


def get_answer(user_question):
    user_vector = vectorizer.transform([user_question])
    similarities = cosine_similarity(
        user_vector, question_vectors
    )[0]

    best_index = similarities.argmax()
    best_score = similarities[best_index]

    if best_score < 0.15:
        return (
            "Sorry, I couldn't find a relevant FAQ. "
            "Please try rephrasing your question."
        )

    return answers[best_index]


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hi! 👋 Ask me anything about college admissions, "
                "fees, exams, scholarships or student services."
            )
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your question here..."):
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    answer = get_answer(prompt)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant"):
        st.markdown(answer)

with st.sidebar:
    st.header("About this project")
    st.write(
        "This chatbot uses TF-IDF and cosine similarity "
        "to match questions with a predefined FAQ dataset."
    )
    st.write(f"Total FAQs: {len(faq_data)}")
    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.rerun()