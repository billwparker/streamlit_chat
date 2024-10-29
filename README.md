# streamlit_chat

pip install streamlit
pip install groq
pip install openai
pip install -q -U google-generativeai

streamlit run main.py

Create a .streamlit folder with a file called secrets.toml. Put in this file these two lines:

open_api_key = 'Your openai api key'<br>
groq_key = 'Your groq api key'<br>
gemeni_key = 'Your gemeni key'
