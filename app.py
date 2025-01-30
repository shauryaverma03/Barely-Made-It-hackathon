import openai
import streamlit as st

# 🔹 Set your OpenAI API key here (Replace with your actual API key)
openai.api_key = "open_api_ev"  # Replace with your API Key

# Add custom CSS for styling
st.markdown(
    """
    <style>
        /* Global Styling */
        body {
            background-color: #f4f4f9;
            font-family: 'Arial', sans-serif;
            color: #333;
        }

        h1 {
            color: #4c6ef5;
            font-size: 36px;
            text-align: center;
            padding: 20px;
        }

        h3 {
            color: #4c6ef5;
            font-size: 24px;
            text-align: center;
        }

        p {
            font-size: 16px;
            line-height: 1.6;
            text-align: center;
            color: #555;
        }

        /* Input Box Styling */
        .stTextInput>div>div>input {
            font-size: 16px;
            padding: 12px;
            border-radius: 8px;
            border: 1px solid #ddd;
            width: 70%;
            margin: 0 auto;
            display: block;
        }

        .stTextInput>div>div>input:focus {
            border-color: #4c6ef5;
        }

        /* Chat Bubble Styling */
        .chat-bubble {
            background-color: #e4e4e9;
            border-radius: 15px;
            padding: 10px 20px;
            margin: 10px 0;
            max-width: 70%;
            margin-left: auto;
            margin-right: auto;
        }

        .chatbot-bubble {
            background-color: #4c6ef5;
            color: white;
        }

        .user-bubble {
            background-color: #e4e4e9;
            color: #333;
        }

        /* Button Styling */
        .stButton>button {
            background-color: #4c6ef5;
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 16px;
            border-radius: 8px;
            cursor: pointer;
            width: 70%;
            margin: 20px auto;
            display: block;
        }

        .stButton>button:hover {
            background-color: #3751d1;
        }

        .stButton>button:focus {
            outline: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit UI with Styling
st.title("🧠 AI Mental Health Chatbot")
st.write("""
    Welcome to our AI-driven mental health assistant. 😊  
    I'm here to offer a listening ear and provide support when you need it most.  
    Whether you're feeling down, stressed, or just want someone to talk to,  
    I can help guide you through it. Please feel free to share how you're feeling today.
""")
st.write("I can help you process your emotions, suggest resources, or just chat with you.")

# User input
user_input = st.text_input("You:", "")

if user_input:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use GPT-3.5-turbo or GPT-4 if available
            messages=[
                {"role": "system", "content": "You are a kind and supportive mental health assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        chatbot_reply = response["choices"][0]["message"]["content"]

        # Display user input and chatbot response with styling
        st.markdown(f'<div class="chat-bubble user-bubble">{user_input}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="chat-bubble chatbot-bubble">{chatbot_reply}</div>', unsafe_allow_html=True)
    
    except Exception as e:
        st.error(f"❌ API Error: {e}")
