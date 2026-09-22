"""
Rule-Based AI Chatbot
DecodeLabs - Artificial Intelligence Project 1

A simple rule-based chatbot using if/elif/else and a continuous loop.
"""

def get_response(user_input):
    """Return a predefined response based on the user's input."""
    text = user_input.lower().strip()

    if text in ["hi", "hello", "hey", "hii"]:
        return "Hello! 👋 I am your Rule-Based AI Chatbot. How can I help you?"

    elif "how are you" in text:
        return "I am doing great! 😊 Thanks for asking."

    elif "your name" in text or "who are you" in text:
        return "I am a Chatbot ."

    elif "what can you do" in text:
        return "I can answer predefined questions using simple if-elif-else rules."

    elif "ai" in text or "artificial intelligence" in text:
        return "AI means Artificial Intelligence. It enables computers to perform tasks that normally require human intelligence."

    elif "python" in text:
        return "Python is a popular programming language that is simple and beginner-friendly."

    elif "thank" in text:
        return "You're welcome! 😊"

    elif text in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! 👋 Have a great day!"

    else:
        return "Sorry, I don't understand that yet. Try asking about AI, Python, my name, or what I can do."


def main():
    print("=" * 55)
    print("        🤖 RULE-BASED AI CHATBOT")
    print("=" * 55)
    print("Type 'bye', 'exit', or 'quit' to end the chat.")
    print()

    while True:
        user_input = input("You: ")

        response = get_response(user_input)
        print("Bot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break

        print()


if __name__ == "__main__":
    main()
