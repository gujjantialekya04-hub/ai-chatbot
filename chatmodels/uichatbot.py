import streamlit as st
from transformers import pipeline

# Load model
@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="Qwen/Qwen2.5-1.5B-Instruct"
    )

chatbot = load_model()

# Page title
st.title("🤖 AI Chatbot")
st.write("Hello krushik!")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
prompt = st.chat_input("Type your message...")

if prompt:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    # Messages sent to model
    messages = [
        {"role": "system", "content": "you are a funny AI agent"},
        {"role": "user", "content": prompt}
    ]

    # Generate response
    response = chatbot(
        messages,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7
    )

    bot_reply = response[0]["generated_text"][-1]["content"]

    # Store assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )

    # Show assistant response
    with st.chat_message("assistant"):
        st.write(bot_reply)