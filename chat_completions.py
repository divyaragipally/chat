import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Streamlit app title
st.title("AI Joke Generator")

# Set up Hugging Face Inference Client
client = InferenceClient("mistralai/Mixtral-8x7B-Instruct-v0.1")

# User input
user_input = st.text_input("Enter your prompt", value="Tell me a joke")

# Button to generate the joke
if st.button("Generate Joke"):
    with st.spinner("Generating..."):
        # Get chat completion from the model
        chat_completion = client.chat_completion(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ], max_tokens=100)

        # Display the output
        st.success(chat_completion.choices[0].message.content)

# Add a footer or additional information if needed
st.write("Powered by Hugging Face and Streamlit")
