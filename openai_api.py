import openai
import os

# Load the OpenAI API key from the file
def load_api_key(file_path="OPENAI_API_KEY.txt"):
    try:
        with open(file_path, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        raise Exception(f"API key file not found at {file_path}. Please create the file and add your OpenAI API key.")

# Initialize OpenAI API key
openai.api_key = load_api_key()

# Example function to interact with OpenAI API
def generate_response(prompt, model="gpt-4o-mini", max_tokens=100):
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=prompt,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error interacting with OpenAI API: {e}")
        return None

# Example usage
if __name__ == "__main__":
    user_prompt = [{"role": "user", "content": "Write a short poem about the ocean."}]
    response = generate_response(user_prompt)
    if response:
        print("Generated Response:")
        print(response)