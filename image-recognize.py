import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

img1 = genai.upload_file(path="image-recognize1.jpg")
img2 = genai.upload_file(path="image-recognize2.jpg")

response = model.generate_content([img2, "Identifique o cachorro da foto e falar da origem, fornecer também duas ou três frases de informações a respeito do animal, de preferência alguma curiosidade interessante e em português, citando a fonte da informação, e sempre de um jeito leve e interessante."])

print(response.text)
