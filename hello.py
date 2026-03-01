# Ask for user info first
name = input("What is your name? ")
age = input("How old are you? ")

# Greet the user automatically
print(f"Hi {name}!")
print(f"You are {age} years old.")
print("You are learning Python and GitHub like a pro 😎\n")

# Mini chatbot responses
responses = {
    "hello": f"Hi {name}! Nice to see you.",
    "how are you?": "I'm doing well, thanks for asking!",
    "what's your name?": f"I'm a chatbot, but I know your name is {name}.",
    "what's your age?": f"I'm a chatbot, so I don't have an age, but you are {age}.",
    "who made you?": "I was made by Puja Rajesh Kumar.",
    "can you speak in tamil?": "Yes, I can speak in Tamil.",
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
questions = ["Hello", "what's your name?", "what's your age?", "who made you?", "can you speak in tamil?", "வணக்கம்"]
for q in questions:
    print(f"You: {q}")
    print("Chatbot:", get_response(q))
