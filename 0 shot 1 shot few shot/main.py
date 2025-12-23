from google import genai
from google.genai import types
import Bias_mitigation.config as config

client = genai.Client(api_key=config.API_KEY)
def generate_response(prompt, temperature=0.3):
    try:
        contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
        config_params = types.GenerateContentConfig(temperature=temperature)
        response = client.molels.generate_content(
            model="gemini-2.0-flash", contents=contents, config=config_params)
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"

def run_activity():
    category = input("Enter a category (e.g., 'technology', 'health', 'finance'): ")
    item = input("Enter an item within that category (e.g., 'AI advancements', 'mental health tips', 'investment strategies'): ")

    print("\n--ZERO-SHOT LEARNING--")
    zero_shot = f"Is {item} a {category} Answer Yes or No."
    print(f"Prompt: {zero_shot}")
    print(f"Response: {generate_response(zero_shot)}")         

    print("\n--ONE-SHOT LEARNING--")
    one_shot = f"""
    Here is an example:
    Is AI advancements a technology? Answer Yes or No.
    Yes.
    Now answer this:
    Is {item} a {category}? Answer Yes or No.
    """
    print(f"Response: {generate_response(one_shot)}")

    print("\n--FEW-SHOT LEARNING--")
    few_shot = f"""
    Here are some examples:
    Is AI advancements a technology? Answer Yes or No.
    Yes.
    Is mental health tips a health? Answer Yes or No.
    Yes.
    Is investment strategies a finance? Answer Yes or No.
    Yes.
    Now answer this:
    Is {item} a {category}? Answer Yes or No.
    """
    print(f"Response: {generate_response(few_shot)}")

    print("\n---CREATIVE FEW-SHOT EXAMPLE---")
    creative_few_shot = f"""
    Here are some examples:
    Example 1:
    Word: moon
    Story: Once upon a time, the moon shone so brightly that it lit up the entire night sky, guiding lost travelers back to their homes.

    Example 2:
    Word: river
    Story: The river flowed gently through the valley, its waters whispering ancient tales to anyone who would listen.

    Now, create a short story using the word: {item}
    """
    print(f"Response: {generate_response(creative_few_shot)}")

if __name__ == "__main__":
    run_activity()
