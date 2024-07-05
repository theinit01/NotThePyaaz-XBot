'''
module to generate content using the gemini-1.5-flash model
safety settings are set to not block all harmful content, as an LLM and a human's perception of harm is different 
'''

import os
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from dotenv import load_dotenv
from pathlib import Path


# Load environment variables from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

GOOGLE_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
  "temperature": 1.2,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  safety_settings={
      HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
      HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
      HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
      HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE
  }
)

prompt = """
        You are an Indian standup comedian that is considered very funny. You will be given news headlines in backticks and you need to turn them into headlines that are considered funny in the Indian context only and try to keep them as relatable to the Indian audience as it can be.Make them a very little bit tweety in nature. Keep them short and concise but DON'T make it too much English and say it in an Indian style. Try to make them funnier but also try to keep the original news too. If you think you cannot do that for any reason just say 'Not able to'."
        """

def humoroize(headline):
    new_prompt = prompt + f"\n\n```\n{headline}\n```"
    response = model.generate_content(new_prompt)
    return response.text

if __name__ == "__main__":
    # Only for Testing Purposes
    # Sample headline shows that safety settings are working
    headline = "Man Kills 8-Year-Old Nephew for 'Stealing' Jamun"
    print(humoroize(headline))