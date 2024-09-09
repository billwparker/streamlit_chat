import openai
import streamlit as st

from models import openai_chat, groq_chat

def get_default_model():
  
  return 'Groq: Meta Llama 3 70B'

if 'model' not in st.session_state:
    st.session_state.model = get_default_model()


if 'message_list' not in st.session_state:
  st.session_state.message_list = [
      {"role": "system", "content": "You are a helpful assistant."}
    ]      

  
if __name__ == "__main__":
  
  st.title('Chatbot')
  
  models = ['GPT 4o', 'GPT 4o Mini', 'Groq: Meta Llama 3 70B']
  
  model_index = models.index(st.session_state.model)
  
  st.session_state.model = st.selectbox('Choose Model:', models, index=model_index)
  selected_model = st.session_state.model
  
  initial_message = "Hello human!"  
  
  with st.chat_message("assistant"):
    st.write(initial_message)
    
    
  # Forcing everything to Groq model, once we put in security, we will take this out.
  if selected_model == 'GPT 4o' or selected_model == 'GPT 4o Mini':
    selected_model = 'Groq: Meta Llama 3 70B'

  
  prompt = st.chat_input("Ask a question")
  if prompt:
    
    with st.spinner('Thinking...'):

      st.session_state.message_list.append({"role": "user", "content": prompt})
      
      content = ', '.join([str(elem) for elem in st.session_state.message_list])
                  
      if selected_model == 'GPT 4o':
        answer = conversation = openai_chat(content, model='gpt-4o')
      elif selected_model == 'GPT 4o Mini':
        answer = conversation = openai_chat(content, model='gpt-4o-mini')
      elif selected_model == 'Groq: Meta Llama 3 70B':
        answer = conversation = groq_chat(content, model='llama3-70b-8192')

      st.session_state.message_list.append({"role": "assistant", "content": answer})  
                  
      for l in st.session_state.message_list:
                
        if l['role'] == 'user':
          with st.chat_message("user"):
            st.write(l['content'])
        elif l['role'] == 'assistant':
          with st.chat_message("assistant"):
            st.write(l['content'])
            
      st.write(f'Using model: {selected_model}')
          
