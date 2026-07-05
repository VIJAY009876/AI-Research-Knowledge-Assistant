from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
# Fetch API key from environment
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY: 
    raise ValueError("OPENROUTER_API_KEY is not set in the environment variables.")

# Base URL for OpenRouter API
BASE_URL = "https://api.openrouter.ai/v1"
#default model to use for requests
MODEL = "deepseek/deepseek-r1:free"
