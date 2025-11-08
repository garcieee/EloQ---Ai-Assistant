import random

responses = {
    "can_hear": [
        "Yes, I can hear you loud and clear!",
        "Absolutely, I'm here and listening.",
        "Indeed! I'm ready to help you.",
        "Yes, go ahead - I'm all ears!",
        "Affirmative, I can hear you perfectly."
    ],
    "goodbye": [
        "Goodbye! Have a great day!",
        "See you later!",
        "Take care!",
        "Until next time!",
        "Farewell, looking forward to our next chat!"
    ],
    "thank_you": [
        "You're welcome!",
        "Happy to help!",
        "My pleasure!",
        "Anytime!",
        "Glad I could assist!"
    ],
    "greeting": [
        "Hi there! How can I help you today?",
        "Hello! Nice to meet you!",
        "Hey! What can I do for you?",
        "Greetings! How may I assist you?",
        "Welcome! How can I be of service?"
    ],
    "not_understood": [
        "I'm sorry, I didn't quite catch that.",
        "Could you please rephrase that?",
        "I'm not sure I understood. Can you say that differently?",
        "Would you mind clarifying that?",
        "I didn't get that. Can you explain further?"
    ]
}

def get_response(intent):
    if intent in responses:
        return random.choice(responses[intent])
    return None

def get_intent(text):
    text = text.lower().strip()
    
    if text in ["can you hear me", "are you there", "hello", "hi", "hey"]:
        return "can_hear"
    elif text in ["goodbye", "bye", "see you", "see ya", "farewell"]:
        return "goodbye"
    elif text in ["thank you", "thanks", "thx", "appreciate it"]:
        return "thank_you"
    elif text.startswith(("hi", "hello", "hey", "greetings")):
        return "greeting"
    else:
        return "not_understood"