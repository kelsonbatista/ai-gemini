import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

img1 = genai.upload_file(path="image-description.webp")

response = model.generate_content([img1, "Gere uma descrição para esta imagem. Quero algo para escrever no post no Instagram e uma descrição da imagem para fins de acessibilidade."])

print(response.text)
