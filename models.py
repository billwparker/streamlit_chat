import streamlit as st
from groq import Groq 
from openai import OpenAI

import groq as gq
import google.generativeai as genai
# print(f'version of groq: {gq.__version__}')

open_api_key = st.secrets["open_api_key"]
groq_key = st.secrets["groq_key"]
genai.configure(api_key=st.secrets["gemeni_key"])

def gemeni_chat(txt:str = "", model:str = "gemini-1.5-flash"):
  
  model = genai.GenerativeModel("gemini-1.5-flash", generation_config={"response_mime_type": "text/plain"})

  try:
    response = model.generate_content(txt)
        
    text = response.text
    
    text = text.replace("{'role': 'assistant', 'content': ", "").replace("}", "").replace("\"", "")\
      .replace('\\n', '').replace('json', '').replace("```", '')
      
    if text[0] == "'":
      text = text[1:]
    if text[-1] == "'":
      text = text[:-1]
        
  except:
    return None
  
  return text

def mistral_chat(txt:str = "", model:str = "Mistral 7B"):
  
  client = OpenAI(
      base_url = 'http://localhost:11434/v1',
      api_key='ollama', # api_key is required, but unused for local models
  )
  
  q = {
    "role": "user",
    "content": txt
  }
        
  response = client.chat.completions.create(
    model="mistral",
    messages=st.session_state.message_list
  )
    
  try:
    result = response.choices[0].message.content
    
  except:
    return None
    
  return result

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
