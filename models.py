import streamlit as st
from groq import Groq 
from openai import OpenAI


import groq as gq
print(f'version of groq: {gq.__version__}')

open_api_key = st.secrets["open_api_key"]
groq_key = st.secrets["groq_key"]


def openai_chat(txt:str = "", model:str = "gpt-4.0-mini"):

  client = OpenAI(
    api_key=open_api_key,
  )
  chat_completion = client.chat.completions.create(
      model=model,
      messages=[
          {
            "role": "system",
            "content": "You are a conversation assistannt"},  
          {
            "role": "user",
            "content": txt
          }
      ]
  )  
  
  try:
    result = chat_completion.choices[0].message.content
    
  except:
    return None
  
  return result


def groq_chat(txt:str = "", model:str = "llama3-70b-8192"):
    
  client = Groq(
      api_key = groq_key,
  )

  chat_completion = client.chat.completions.create(
      messages=[
          {
            "role": "system", 
            "content": "You are a conversation assistannt"},  
          {
            "role": "user",
            "content": txt
          }
      ],
      model = model,
  )
  
  try:
    result = chat_completion.choices[0].message.content
      
  except:
    return None
  
  return result
