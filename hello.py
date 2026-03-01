# Ask for user info first
name = input("What is your name? ")
age = input("How old are you? ")

# Greet the user automatically
print(f"Hi {name}!")
print(f"You are {age} years old.")
print("You are learning Python and GitHub like a pro 😎\n")

# Mini chatbot responses
responses = {
    "hello": f"Hi {name}! Nice to see you."
    "How are you?""I'm doing well, thanks for asking!"
    "wWhat'syour name?""I'm a chatbot, but I know your name is {name}."
    "wWhat'syour age?": f"I'm a chatbot, so I don't have an age, but you are {age}."
    "Who made you?""I was made by Puja Rajesh Kumar."
    "cCanyou speak in Tamil?""Yes, I can speak in Tamil."
    "வணக்கம்": "வணக்கம்",
    "உங்கள் பெயர் என்ன?": "நான் Chatbot!",
}

# Function to get response automatically
def get_response(user_input):
    # Convert English input to lowercase for matching
    if user_input.lower() in responses:
        return responses[user_input.lower()]
    else:
        return "I'm not sure I understand. Can you rephrase?"

# Simulate some automatic conversation
questions = ["Hello", "What's your name?", "What's your age?" "Who made you?" "cCanyou speak in Tamil?" "வணக்கம்"]
for q in questions:
    print(f"You: {q}")
    print("Chatbot:", get_response(q))
