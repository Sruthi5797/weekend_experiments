import streamlit as st
import os
from dotenv import find_dotenv, load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_community.llms import Ollama
from langchain_groq import ChatGroq

def model_inference(radio_options):
    llm_call = Ollama(model="llama3") 
    prompt = PromptTemplate.from_template(
        """Generate me a pick-up line according to the choosen scenario {selected_option}.
        Output must only be the response, Keep it to a maximum of two lines only.
        Don't add anything extra.
        """
    )
    pickupline_output = llm_call.invoke(prompt.format(selected_option=radio_options))
    return pickupline_output

def model_inference2(radio_options):
    env_path = find_dotenv()

    load_dotenv(env_path)

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    llm = ChatGroq(temperature=1, model_name="llama3-8b-8192")

    response = PromptTemplate.from_template(
        """Generate me a pick-up line according to the choosen scenario {selected_option}.
        Output must only be the response, Keep it to a maximum of two lines only.
        Don't add anything extra.
        """
    )
    output = llm.invoke(response.format(selected_option = radio_options))
    return output.content


original_title = '<p style="font-family:Fantasy; color:Blue; font-size: 20px;">Pickup Cupid - Generate awesome pickup lines for your loved ones</p>'
st.markdown(original_title, unsafe_allow_html=True)

radio_options = st.radio(
    "Choose a pick_line scenario",
    ("Cheesy", "Romantic", "Funny", "Weird", "Smooth", "Cute")
)

st.write("You have selected",radio_options)

if st.button("Get line"):
    output = model_inference2(radio_options)
    answer = st.text_area('Here is one for you',output)
    





