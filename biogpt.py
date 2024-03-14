# !pip install sacremoses
# !pip install transformers

import streamlit as st


# Beginning of the user facing Frontend
st.markdown("## Chatten mit BioGPT")

st.markdown( "Hier können verschiedene Prompts mit BioGPT getestet werden." )

st.markdown("---")


#--------------------------------------------------------------------------------------------------
# Hugging Face Models: Leaving them our for now. 


#from transformers import pipeline, set_seed
from transformers import BioGptTokenizer, BioGptForCausalLM


# Setting up the Model through HuggingFace
#model = BioGptForCausalLM.from_pretrained("microsoft/biogpt")
#tokenizer = BioGptTokenizer.from_pretrained("microsoft/biogpt")
#generator = pipeline("text-generation",model=model,tokenizer=tokenizer)
#set_seed(42)





prompt_list_dropdown = ["Prompt 1", 
                        "Prompt 2", 
                        "Prompt 3", 
                        "Prompt 4"
                       ]

prompt_option = st.selectbox("Prompt Auswahl", prompt_list_dropdown)

st.markdown("Du hast " + prompt_option + " gewählt.")

st.markdown("---")


# Interacting with the model
#input_text= "COVID-19 is"
#answer = generator(input_text, max_length=20, num_return_sequences=5, do_sample=True)

#st.write(answer)



#---------------------------------------------------------------------------------------------------------
# Simple Chatbot interface: 

import random
import time


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})




