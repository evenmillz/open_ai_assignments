import openai
import os

# Initialize the OpenAI client with my API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def translate_to_french(english_text):
    response = client.chat.completions.create(        model="gpt-4",  # or "gpt-3.5-turbo" to reduce cost
        messages=[
            {"role": "system", "content": "You are a helpful assistant that translates English to French."},
            {"role": "user", "content": f"Translate this to French: {english_text}"}
        ],
        temperature=0.3,
        max_tokens=100
    )
    return response.choices[0].message.content.strip()

# Prompt the user
english_input = input("Enter an English sentence: ")
french_output = translate_to_french(english_input)
print("French translation:", french_output)