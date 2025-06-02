from openai import OpenAI

# Set up client with your API key
client = OpenAI(api_key="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")

# Get user input
raw_data = input("Enter raw data: ")

# Generate response using ChatGPT model
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": raw_data}
    ],
    temperature=0.7,
    max_tokens=50,
)

# Output result
generated_output = response.choices[0].message.content.strip()
print("Generated output:")
print(generated_output)