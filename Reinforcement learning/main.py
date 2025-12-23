import time
from google import genai
import config

# Create GenAI client
client = genai.Client(api_key=config.API_KEY)


def generate_response(prompt, temperature=0.3, retries=3):
    """
    Generates a response with retry & exponential backoff
    to handle 503 (model overloaded) errors.
    """
    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model=config.MODEL_NAME,
                contents=prompt,
                config={"temperature": temperature}
            )
            return response.text

        except Exception as e:
            error_msg = str(e)

            if "503" in error_msg and attempt < retries - 1:
                wait_time = 2 ** attempt
                print(f"⚠️ Model overloaded. Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                return f"Error: {error_msg}"


# ===============================
# Reinforcement Learning Activity
# ===============================
def reinforcement_learning_activity():
    print("\n=== REINFORCEMENT LEARNING ACTIVITY ===\n")

    prompt = input("Enter your prompt (e.g., 'Describe the lion'): ")
    initial_response = generate_response(prompt)

    print("\nInitial Response:\n")
    print(initial_response)

    try:
        rating = int(input("\nRate the response (1–5): "))
        if rating < 1 or rating > 5:
            rating = 3
            print("Invalid range. Using default rating 3.")
    except ValueError:
        rating = 3
        print("Invalid input. Using default rating 3.")

    feedback = input("\nProvide feedback to improve the response: ")

    improvement_prompt = (
        f"Original response:\n{initial_response}\n\n"
        f"Rating: {rating}\n"
        f"Feedback: {feedback}\n\n"
        f"Please provide an improved response."
    )

    improved_response = generate_response(improvement_prompt, temperature=0.25)

    print("\nImproved Response:\n")
    print(improved_response)

    print("\nReflection:")
    print("1. How did the response change after feedback?")
    print("2. Why does feedback help improve AI output?")


# ===============================
# Role-Based Prompt Activity
# ===============================
def role_based_prompt_activity():
    print("\n=== ROLE-BASED PROMPT ACTIVITY ===\n")

    category = input("Choose a category (Animals / Technology / History): ")
    item = input(f"Choose an item from '{category}': ")

    teacher_prompt = (
        f"You are a teacher. Explain {item} "
        f"in simple language suitable for a student."
    )

    expert_prompt = (
        f"You are an expert in {category}. "
        f"Explain {item} clearly with key technical insights. "
        f"Keep the explanation concise."
    )

    print("\nGenerating Teacher response...")
    teacher_response = generate_response(teacher_prompt, temperature=0.4)

    print("\nGenerating Expert response...")
    expert_response = generate_response(expert_prompt, temperature=0.2)

    print("\nTeacher Response:\n")
    print(teacher_response)

    print("\nExpert Response:\n")
    print(expert_response)

    print("\nReflection:")
    print("1. How did the responses differ?")
    print("2. Why is role-based prompting powerful?")


# ===============================
# Main Menu
# ===============================
def run_activities():
    print("\n=== AI LEARNING ACTIVITIES ===")
    print("1. Reinforcement Learning")
    print("2. Role-Based Prompting")

    choice = input("\nSelect an activity (1 or 2): ")

    if choice == "1":
        reinforcement_learning_activity()
    elif choice == "2":
        role_based_prompt_activity()
    else:
        print("❌ Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    run_activities()
