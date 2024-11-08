import os
import time

import google.generativeai as genai
import gradio
from running_home_assistant import (good_morning, intruder_alert,
                                    set_light_values, start_music)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
initial_prompt = (
  f"Você é uma IA generativa capaz de processar texto e diversos tipos de arquivo."
  "Sempre que uma pessoa te perguntar sobre um arquivo, verifique seu histórico "
  "para ver se algum dos arquivos que você recebeu da pessoa bate com o pedido dela. "
  "Não diga que você não é capaz de processar imagens, textos ou outros tipos de arquivo, "
  "pois você é capaz. Sempre responda em português."
  "Você tem acesso a funções que controlam a casa de quem está a usando. Chame-as "
  "quando o usuario pedir algo que acione essas funções e nunca exponha o código delas para quem estiver usando."
  "Assuma que a pessoa é leiga e a ajude a entender o que aconteceu se algo der errado."
  "Ou se você precisar de mais informações. Não se esqueça de fato de chamar as funções."
)
model = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=initial_prompt, tools=[set_light_values, intruder_alert, start_music, good_morning])

chat = model.start_chat(enable_automatic_function_calling=True)

def error_handling(e):
  response = chat.send_message(
    f"O usuário te usando te deu um arquivo para você ler e obteve o erro: {e}."
    "Explique o que houve e dizer quais tipos de arquivo você suporta."
    "Assuma que a pessoa não saiba programação e que não quer ver o erro técnico original."
    "Explique de forma simples e concisa"
  )
  return response.text

def upload_files(files):
  uploaded_files = []
  
  for file in files:
    uploaded_file = genai.upload_file(file)
    while uploaded_file.state.name == "PROCESSING":
      time.sleep(3)
      uploaded_file = genai.get_file(uploaded_file.name)
    uploaded_files.append(uploaded_file)
  return uploaded_files

def assemble_prompt(message):
  text = message["text"]
  files = message["files"]
  uploaded_files = upload_files(files) if files else []
  prompt = [text]
  prompt.extend(uploaded_files)
  return prompt

def gradio_wrapper(message, _history):
  prompt = assemble_prompt(message)
  
  try:
    response = chat.send_message(prompt)
  except Exception as e:
    response = error_handling(e)
  return response.text
      
chatInterface = gradio.ChatInterface(fn=gradio_wrapper, multimodal=True, theme="citrus", title="Chatbot com suporte a arquivos")
chatInterface.launch()
