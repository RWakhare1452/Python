from google import genai
import config

# Initialize the AI client with the API key from config.py
client = genai.Client(api_key=config.GEMINI_API_KEY)

# Function to generate AI responses
def generate_response(prompt):
    """
    Sends a prompt to the Gemini AI model and returns the response.
    
    Args:
        prompt (str): The user's question or instruction
    
    Returns:
        str: The AI's generated response
    """
    try:
        # Try different model name formats
        model_names = [
            "gemini-1.5-flash",
            "gemini-1.5-pro", 
            "gemini-pro",
            "gemini-2.0-flash-exp"
        ]
        
        for model_name in model_names:
            try:
                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt
                )
                return response.text
            except Exception as model_error:
                if "NOT_FOUND" in str(model_error):
                    continue  # Try next model
                else:
                    raise  # Re-raise if it's a different error
        
        # If all models failed
        return "❌ Error: Could not find a working model. Please run check_models.py to see available models."
        
    except Exception as e:
        if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
            return "⚠ API quota exceeded. Please wait a minute and try again."
        else:
            return f"❌ Error: {str(e)}"

# Function to interactively guide the user in creating specific prompts
def silly_prompt():
    """
    Interactive tutorial that guides users through three levels of prompt engineering:
    1. Vague prompt
    2. Specific prompt
    3. Contextual prompt
    """
    print("Welcome to the AI Prompt Engineering Tutorial!")
    print("In this activity, we will learn about *Clarity and Specificity* and *Contextual Information* in crafting prompts for AI.")
    print("\nLet's start by crafting a vague prompt, making it more specific, and then adding context.")
    
    # Step 1: Vague Prompt Creation
    vague_prompt = input("\nPlease enter a vague prompt (e.g., 'Tell me about technology'): ")
    
    # Generate response for vague prompt
    print(f"\nYour vague prompt: {vague_prompt}")
    vague_response = generate_response(vague_prompt)
    print("\nAI's response to the vague prompt:")
    print(vague_response)
    
    # Step 2: Make the Prompt Clear and Specific
    specific_prompt = input("\nNow, make the prompt more specific (e.g., 'Explain how AI works in self-driving cars'): ")
    
    # Generate response for specific prompt
    print(f"\nYour specific prompt: {specific_prompt}")
    specific_response = generate_response(specific_prompt)
    print("\nAI's response to the specific prompt:")
    print(specific_response)
    
    # Step 3: Add Context to the Prompt
    contextual_prompt = input("\nNow, add context to your specific prompt (e.g., 'Given the advancements in autonomous vehicles, explain how AI is used in self-driving cars to make real-time driving decisions'): ")
    
    # Generate response for contextual prompt
    print(f"\nYour contextual prompt: {contextual_prompt}")
    contextual_response = generate_response(contextual_prompt)
    print("\nAI's response to the contextual prompt:")
    print(contextual_response)
    
    # Reflection Questions
    print("\n--- Reflection ---")
    print("1. How did the AI's response change when the prompt was made more specific?")
    print("2. How did the AI's response improve with the added context?")
    print("3. Which prompt produced the most relevant and tailored response? Why?")

# Run the interactive tutorial
if __name__ == "__main__":
    silly_prompt()