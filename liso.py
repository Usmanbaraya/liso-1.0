import streamlit as st
import os
from dotenv import load_dotenv

#Load the environmental variable
from openai import OpenAI
load_dotenv()

#Initialize openAi
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

client = OpenAI()

#fuction to get the response from the model
def get_liso_response(user_message: str) -> str:
    liso_chat = client.chat.completions.create(
        model= "ft:gpt-4o-2024-08-06:personal:liso:B9CdHKPF",
        messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": user_message}
    ]
)
    return liso_chat.choices[0].message.content

#Building Streamlit app
def main():
    st.title("Liso")
    st.write("Welcome to liso chatbot! Ask me anything about Appliso Technologies.")
    user_message = st.text_input("You:")
    
#When the user submits a message, get the response from the model
    if st.button("Send"):
        liso_response = get_liso_response(user_message)
        st.subheader("liso's Answer")
        st.write("Liso: ", liso_response)

if __name__== "__main__" :
    main()