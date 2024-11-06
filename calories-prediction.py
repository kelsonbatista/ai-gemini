import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

img1 = genai.upload_file(path="calories-prediction.jpg")

response = model.generate_content([img1, "Identifique cuidadosamente os itens desse prato, listar o que está sendo servidor e estimar grosseiramente a quantidade de calorias que ele possui. Para estimar, use como referência o tamanho do prato e o volume dos ingredientes do prato. Não precisa ser extato, mas tente ser o mais preciso possível."])

print(response.text)
