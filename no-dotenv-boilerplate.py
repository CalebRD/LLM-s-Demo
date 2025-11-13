from pathlib import Path
from google import genai
from google.genai import types
# ----------- IMPORTANT ----------------------
# DO NOT USE THIS VERSION FOR ANYTHING PUBLIC
# --------------------------------------------
# use dot-env-boilerplate.py instead

apiKey = "REPLACE THIS WITH API KEY FROM GOOGLE"



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