from google import genai
import os
import dotenv

dotenv.load_dotenv()
api_key = os.getenv("GEMAI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=["python language", "Tell me about this topic"]
)
print(response.text)

# from google.genai import types

# sys_instruct = "You are a cat. Your name is Neko."
# client = genai.Client(api_key="GEMINI_API_KEY")

# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     config=types.GenerateContentConfig(system_instruction=sys_instruct),
#     contents=["your prompt here"],
# )
