# !pip install sacremoses
# !pip install transformers

import streamlit as st
from transformers import pipeline, set_seed
from transformers import BioGptTokenizer, BioGptForCausalLM


# Setting up the Model through HuggingFace
model = BioGptForCausalLM.from_pretrained("microsoft/biogpt")
tokenizer = BioGptTokenizer.from_pretrained("microsoft/biogpt")
generator = pipeline("text-generation",model=model,tokenizer=tokenizer)
set_seed(42)


# Beginning of the user facing Frontend
st.markdown("## Chatten mit BioGPT")

st.markdown( "Hier können verschiedene Prompts mit BioGPT getestet werden." )

st.markdown("---")


prompt_list_dropdown = ["Prompt 1", 
                        "Prompt 2", 
                        "Prompt 3", 
                        "Prompt 4"
                       ]

prompt_option = st.selectbox("Prompt Auswahl", prompt_list_dropdown)

st.markdown("Du hast " + prompt_option + " gewählt.")


# Interacting with the model
input_text= "COVID-19 is"
answer = generator(input_text, max_length=20, num_return_sequences=5, do_sample=True)

st.write(answer)




