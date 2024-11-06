import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

with open("improve-cv-file.txt", "r") as file:
    curriculum = file.read()


response = model.generate_content(f"Melhorar o curriculo a seguir para deixar ele mais assertivo e enfatiando os pontos positivos. Segue o curriculum: {curriculum}")

print(response.text)