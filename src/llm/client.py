from openai import OpenAI
from src.prompts.system_prompt import SYSTEM_PROMPT

from config import (
    OPENROUTER_API_KEY,
    BASE_URL,
    MODEL
)

#create client instance
client = OpenAI(
api_key=OPENROUTER_API_KEY,
base_url=BASE_URL
)

# function to send a request to the OpenRouter API
def ask_llm(prompt : str)-> str:
    """
    Sends a prompt to the OpenRouter API and returns the response.
    Args: 
       prompt (str): The input prompt to send to the LLM."""
    
    response = client.chat.completions.create(
        model = MODEL,
        temperature = 0.2,  # we can say randomness is 0.4
        max_tokens = 100,  # This prevents unnecessarily long responses: defult is 500
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

