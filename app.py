import os
import openai
import streamlit as st
import pandas as pd
import numpy as np
import random
import re
import urllib
responses = ["Making pancakes","Going on StackOverflow","Watching TechWithTim","Getting a latte"]
st.title('Epic Bookmarklet Creator')
openai.api_key=st.text_input("Enter your API_KEY here (don't worry we don't store anything): ")
prompt = "/* "+st.text_input("Enter what you would like your bookmarklet to do here")+" */"
if st.button("Generate"):
    try:
         with st.spinner(text=random.choice(responses)):
        
            response = openai.Completion.create(
    model="code-davinci-002",
    prompt=f"<!DOCTYPE html> <html> <head></head> <body> \n<script>\n/* {prompt} */\n",
    temperature=0.05,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0.62,
    presence_penalty=0
    )
            st.code(response["choices"][0]["text"].split("</script>")[0])
         with st.spinner(text=random.choice(responses)):
            st.code("javascript:void function(){"+urllib.parse.quote(response["choices"][0]["text"].split("</script>")[0].encode('utf-8'), safe='')+"}();")
    except Exception as e:
        print(e)
        st.error("Something went wrong 😔, check your API key")
else:
    pass
