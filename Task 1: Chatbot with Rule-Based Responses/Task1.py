import datetime
import random
print("=" * 50)
print("      WELCOME TO CODSOFT CHATBOT")
print("=" * 50)
print("Type 'help' to see available commands.")
print("Type 'bye' to exit.\n")
greetings = [
    "Hello! How can I help you?",
    "Hi there! Nice to meet you.",
    "Hey! What can I do for you?"
]
fallback_responses = [
    "Sorry, I didn't understand that.",
    "Can you please rephrase your question?",
    "I'm still learning. Please try another question."
]
while True:
    user_input = input("You: ").strip().lower()
    if not user_input:
        print("Bot: Please enter a message.")
        continue
    elif user_input in ["hi", "hello", "hey"]:
        print("Bot:", random.choice(greetings))

    elif "your name" in user_input or "who are you" in user_input:
        print("Bot: I am a Rule-Based Chatbot developed for the CodSoft AI Internship.")

    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        print(f"Bot: Current time is {current_time}")
    elif "date" in user_input:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's date is {current_date}")
    elif "how are you" in user_input:
        print("Bot: I'm doing great! Thanks for asking.")
    elif user_input == "help":
        print("\nAvailable Commands:")
        print("- hi / hello / hey")
        print("- how are you")
        print("- what is your name")
        print("- time")
        print("- date")
        print("- help")
        print("- bye\n")
    elif "internship" in user_input:
        print("Bot: This chatbot is developed as part of the CodSoft AI Internship.")
    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Thank you for chatting. Goodbye!")
        break
    else:
        print("Bot:", random.choice(fallback_responses))
