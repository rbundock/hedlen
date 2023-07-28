import requests
import openai
import os
from bs4 import BeautifulSoup

openai.api_key = os.getenv('OPENAI_API_KEY')   # Set your OpenAI API key

def extract_data_from_html(url, prompt):
    # Send a request to the website
    r = requests.get(url)

    # Parse the website content
    soup = BeautifulSoup(r.text, 'html.parser')

    output = soup.prettify()

    # Pass the HTML content and the prompt to the language model
    response = openai.Completion.create(
        model="gpt-3.5-turbo-16k",  # Use the most advanced model available
        prompt=f"{output}\n{prompt}",
        temperature=0.5,  # Adjust as needed for more or less randomness
        max_tokens=200  # Adjust as needed based on how much data you expect to extract
    )

    # Print the model's response
    print(response.choices[0].text.strip())

url = "https://cohaesus.co.uk/blog/guide-to-ecommerce-replatforming/"  # Replace with your desired URL
prompt = "Extract the main text from this webpage."  # Replace with your desired instruction
extract_data_from_html(url, prompt)
