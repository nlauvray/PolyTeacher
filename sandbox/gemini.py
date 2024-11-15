import google.generativeai as genai
import os

os.environ["KEY"] = "AIzaSyAfRdDYwvWUVC16MZu8TzXzXTeGoeoyov0"
genai.configure(api_key=os.environ["KEY"])
prompt = input("Entrez votre prompt : ")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(prompt)
print(response.text)