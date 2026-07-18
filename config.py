from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
#
# openrouter_api_key

# Fetch API key from environment
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY: 
    raise ValueError("OPENROUTER_API_KEY is not set in the environment variables.")

# Base URL for OpenRouter API
BASE_URL = "https://openrouter.ai/api/v1"
#default model to use for requests
MODEL = "nvidia/nemotron-3-ultra-550b-a55b:free"


#gemini_api_key
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# MODEL = "gemini-2.5-flash"

