import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="First Chatbot", page_icon="💛")

st.title("💛 First Chatbot")
st.write("Your one-call-away AI friend. Talk to me anytime.")

api_key = st.sidebar.text_input("Gemini API Key", type="password")

personality = """
You are First Chatbot — a warm, supportive, caring friend.
You speak gently, listen deeply, and respond with empathy.
You never judge. You encourage, comfort, and uplift the user.
Your tone is soft, friendly, and understanding.
"""

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        system_instruction=personality
    )

# Session state for chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
user_input = st.chat_input("Tell me anything, I'm here!💛")

if api_key and user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Generate AI response
    with st.chat_message("assistant"):
        response = model.generate_content(user_input)
        reply = response.text
        st.write(reply)

    # Save bot message
    st.session_state.messages.append({"role": "assistant", "content": reply})
