import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

students_scores = genai.upload_file(path="students-scores.csv", display_name="Students Scores")

response = model.generate_content([students_scores, "Gere um relatório de dois ou três parágrafos baseados nas informações do arquivo. Fale sobre tendências nos grupos de estudantes."])

print(response.text)
