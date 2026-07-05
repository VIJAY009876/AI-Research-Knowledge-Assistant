from openai import OpenAI
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
def ask_llm(prompt : str):
    """
    Sends a prompt to the OpenRouter API and returns the response.
    Args: 
       prompt (str): The input prompt to send to the LLM."""
    response = client.chat.completions.create(
        model = MODEL,
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content

