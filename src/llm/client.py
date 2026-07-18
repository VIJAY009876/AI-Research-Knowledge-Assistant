from openai import OpenAI
# from google import genai
# from google.genai import types

from src.prompts.system_prompt import SYSTEM_PROMPT

from config import (
    OPENROUTER_API_KEY,
    BASE_URL,
    # GEMINI_API_KEY,
    MODEL
)

# #create client instance
client = OpenAI(
api_key=OPENROUTER_API_KEY,
base_url=BASE_URL
)

# client = genai.Client(api_key = GEMINI_API_KEY)



# function to send a request to the OpenRouter API
def ask_llm(prompt : str)-> str:
    """
    Sends a prompt to the OpenRouter API and returns the response.
    Args: 
       prompt (str): The input prompt to send to the LLM."""
    
    response = client.chat.completions.create(
        model = MODEL,
        temperature = 0.2,  # we can say randomness is 0.4
        max_tokens = 200,  # This prevents unnecessarily long responses: defult is 500
        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content


    #gemini api call

    # config = types.GenerateContentConfig(
    #     system_instruction=SYSTEM_PROMPT,
    #     temperature=0.4, # Gemini handles this as "temperature"
    #     max_output_tokens=100
    # )

    # # Generate the content
    # response = client.models.generate_content(
    #     model=MODEL, # Or use 'gemini-2.5-pro' for complex reasoning
    #     contents=prompt,
    #     config=config
    # )

    # return response.text
        

