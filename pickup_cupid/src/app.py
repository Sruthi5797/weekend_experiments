import streamlit as st
from langchain.prompts.prompt import PromptTemplate
from langchain_community.llms import Ollama

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


original_title = '<p style="font-family:Fantasy; color:Blue; font-size: 20px;">Pickup Cupid - Generate awesome pickup lines for your loved ones</p>'
st.markdown(original_title, unsafe_allow_html=True)

radio_options = st.radio(
    "Choose a pick_line scenario",
    ("Cheesy", "Romantic", "Funny", "Weird", "Smooth", "Cute")
)

st.write("You have selected",radio_options)

if st.button("Get line"):
    output = model_inference(radio_options)
    answer = st.text_area('Here is one for you',output)
    





