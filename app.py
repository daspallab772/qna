import os
#import pandas as pd 
#import numpy as np
import streamlit as st
#import pickle
from textblob import TextBlob
from transformers import pipeline

st.set_page_config(page_title='Question and Answer', page_icon='favicon', layout='wide', initial_sidebar_state='auto')

@st.cache()
def Q_to_A(question,context):
    #model_file = 'finalized_model_pipeline.sav'
    # load the model from disk
    #nlp = pickle.load(open(model_file, 'rb'))
    nlp = pipeline('question-answering',model ='mrm8488/bert-small-finetuned-squadv2') #'bert-large-cased-whole-word-masking-finetuned-squad')
    ans= nlp(question = question, context = context)
    #print('Question:- "' + question3 + '"')
    #print('Answer:- "' +ans['answer'] + '"')
    return ans['answer']

def translation(transcript):
    # transcript_simple = "".join(transcript)
    blob = TextBlob(transcript)
    convrt=str(blob.translate(to='en'))
    return convrt    

st.title("📄 Text to Question and Answer ")

transcript = st.text_input("Put your text in English (or Hindi, Bengali, Marathi)",'')

select_language = st.selectbox("Select the text laguage from the drop down",("Please select correct audio language","English(USA)","English(India)","Hindi(India)","Bengali(India)","Marathi(India)"))

if select_language == "English(USA)":
    language = "en-US"
    convrt= transcript
if select_language == "English(India)":
    language = "en-IN"
    convrt= transcript
if (select_language == "Hindi(India)"):
    language = "hi-IN"
    convrt=translation(transcript)
if (select_language == "Bengali(India)"):
    language = "bn-IN"
    convrt=translation(transcript)
if (select_language == "Marathi(India)"):
    language = "mr-IN" 
    convrt=translation(transcript)

q1 = st.text_input("Ask a suitable question relevant to the text in English. ",'')

if q1!="" :
    ans1= Q_to_A(q1,convrt)
    st.subheader("Answer :  :point_down: ")
    st.write(ans1)  

q2 = st.text_input("Ask another suitable question relevant to the text in English. ",'')
if q2!="" :
    ans2= Q_to_A(q2,convrt)
    st.subheader("Answer :  :point_down: ")
    st.write(ans2)   

    

