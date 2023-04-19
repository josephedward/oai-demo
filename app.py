import openai
import os
#load environment variables
from dotenv import load_dotenv
load_dotenv()

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load model name from environment variable
model_name = os.getenv("OPENAI_MODEL", "text-davinci-002")

# Create OpenAI model instance
model = openai.Model(model_name)

# Set up REPL to ask for prompts
while True:
    prompt = input("Enter a prompt or 'exit' to quit: ")
    if prompt == "exit":
        break
    # Generate text with the OpenAI GPT-3 model
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.7,
    )

    # Print the response
    print(response.choices[0].text)

