import os
import google.generativeai as genai
from random import randrange

from log_printer import print_log

def get_content_using_AI():

    try:
        print_log("Configuring Gemini")
        GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=GEMINI_API_KEY)
        # gemini-pro-vision (in case of need to give image input)

        model = genai.GenerativeModel('gemini-pro')
        
        prompts = [
        "Generate only one viral tech tweet with hashtags. This tweet should factual. Keep the tone more like a curious human and less like someone trying to sell something. Don't explain your answer.",
        "Generate only one viral tech tweet with hashtags. This tweet should educational. Keep the tone more like a curious human and less like someone trying to sell something. Don't explain your answer.",
        "Generate only one viral tech tweet with hashtags. This tweet should be tech news. Keep the tone more like a curious human and less like someone trying to sell something. Don't explain your answer.",
        "Generate only one viral tech tweet with hashtags. This tweet should be question about some tech preference. Keep the tone more like a curious human and less like someone trying to sell something. Don't explain your answer.",
        "Generate only one viral tech tweet with hashtags. This tweet should be a joke or a pun related to the world of tech and programming. Keep the tone more like a curious human and less like someone trying to sell something. Don't explain your answer.",
        ]
        
        prompt = prompts[randrange(len(prompts))]

        print_log(f"Using prompt: {prompt}")
        response = model.generate_content(prompt)
        
        return response.text

    except Exception as e:
        print_log(f'{type(e).__name__}: {e}')
        print(f'{type(e).__name__}: {e}')