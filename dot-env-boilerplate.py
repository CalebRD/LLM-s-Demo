from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

# This program requires you to have a .env file.
# You can create a new file in this folder, and name it .env
# Then, add a single line that says "GOOGLE_API_KEY:{key_here}",
# but replace {key_here} with an API key from google.


load_dotenv()
apiKey = os.getenv("GOOGLE_API_KEY")
if not apiKey:
    raise RuntimeError("Please set GOOGLE_API_KEY in .env") 

# you can swap this code for any code to get or generate a prompt.

myPrompt = "What is the Capital of Austraillia?"

client = genai.Client(api_key=apiKey)
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
        myPrompt
    ]
)

print(response.text)