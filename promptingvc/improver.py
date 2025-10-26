"""AI-powered prompt improvement using OpenAI."""

import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class PromptImprover:
    """Uses AI to improve prompts."""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize with OpenAI API key."""
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        self.client = None
        
        if self.api_key:
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=self.api_key)
            except ImportError:
                pass

    def is_available(self) -> bool:
        """Check if AI improvement is available."""
        return self.client is not None

    def improve_prompt(self, original_prompt: str, goals: Optional[str] = None) -> str:
        """
        Improve a prompt using AI.
        
        Args:
            original_prompt: The original prompt to improve
            goals: Optional specific goals for improvement
            
        Returns:
            Improved version of the prompt
        """
        if not self.is_available():
            raise RuntimeError("OpenAI client not available. Please set OPENAI_API_KEY environment variable.")

        system_message = """You are an expert at improving GPT prompts. Your task is to enhance prompts to be:
- Clear and specific
- Well-structured
- More effective at getting desired results
- Following best practices for prompt engineering

Provide only the improved prompt without explanations unless asked."""

        user_message = f"Please improve this prompt:\n\n{original_prompt}"
        
        if goals:
            user_message += f"\n\nSpecific goals for improvement: {goals}"

        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise RuntimeError(f"Failed to improve prompt: {str(e)}")

    def analyze_prompt(self, prompt: str) -> str:
        """
        Analyze a prompt and provide suggestions.
        
        Args:
            prompt: The prompt to analyze
            
        Returns:
            Analysis and suggestions
        """
        if not self.is_available():
            raise RuntimeError("OpenAI client not available. Please set OPENAI_API_KEY environment variable.")

        system_message = """You are an expert at analyzing GPT prompts. Provide constructive feedback on:
- Clarity and specificity
- Structure and organization
- Potential improvements
- Best practices that could be applied"""

        user_message = f"Please analyze this prompt and provide suggestions:\n\n{prompt}"

        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.7,
                max_tokens=1500
            )
            
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise RuntimeError(f"Failed to analyze prompt: {str(e)}")
