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

def model_inference2(radio_options,sex,quality):
    env_path = find_dotenv()

    load_dotenv(env_path)

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    llm = ChatGroq(temperature=1, model_name="llama3-8b-8192")

    response = PromptTemplate.from_template(
        """Generate me a pick-up line according to the choosen scenario {selected_option}.
        Output must only be the response, Keep it to a maximum of two lines only.
        Don't add anything extra. Also the output should be for the given sex {sex_option}, and it should be focused on the desired quality by the user input {text_option}
        """
    )
    output = llm.invoke(response.format(selected_option = radio_options, sex_option = sex, text_option = quality))
    return output.content


original_title = '<p style="font-family:\'Roboto\', sans-serif; color:Red; font-size: 20px;">Pickup Cupid - Generate awesome pickup lines for your loved ones</p>'
st.markdown(original_title, unsafe_allow_html=True)

radio_options = st.radio(
    "Choose a pick_line scenario",
    ("Cheesy", "Romantic", "Funny", "Weird", "Smooth", "Cute", "Dirty")
)

sex = st.radio(
    "Choose from below to whom you want to say this",
    ("Male", "Female")
)

quality = st.text_area("Enter any additional context or customize the pickup line", "")

st.write("You have selected",radio_options)

if st.button("Get line"):
    output = model_inference2(radio_options,sex,quality)
    answer = st.text_area('Here is one for you',output)
    





