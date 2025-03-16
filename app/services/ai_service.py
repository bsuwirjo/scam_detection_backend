import openai
from app.config import Config

openai.api_key = Config.OPENAI_API_KEY

class AIService:
    """Handles AI-generated scam explanations."""
    @staticmethod
    def generate_explanation(message: str) -> str: 
        message_list = [{"role": "system", "content": "You are acybersecurity assistant."}]
        message_list += message
        response = openai.chat.completions.create(
            model="gpt-4-turbo",
            messages=message_list
        )
        return response.choices[0].message.content
