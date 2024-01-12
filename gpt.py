import openai
import os

def generate_text(prompt, temperature = 0.8, model = "gpt-3.5-turbo"):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    success = False
    while not success:
        try:
            messages = [{"role": "user", "content": f"{prompt}"}]
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature,
            )
            success = True
        except Exception as e:
            print(f"An error occurred: {e}. Retrying...")
    return response.choices[0].message.content