from google import genai

# Initialize the Google AI Client
client = genai.Client(api_key="AIzaSyC8WO_tDMFNE4R46fxvaRg6B7zRQ0Ois5k")  # Replace with your actual API key

while True:
    # Get user input (AI/Web Development question)
    user_question = input("\nAsk me anything about AI or Web Development (or type 'exit' to quit): ")

    if user_question.lower() == "exit":
        print("Goodbye! 👋")
        break  # Exit loop if user types 'exit'

    # Generate response from AI
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=user_question
    )

    # Print AI's answer
    print("\nAI's Response:\n")
    print(response.text)



