from nltk.chat.util import Chat, reflections

CHAT_PAIRS = [
    [
        r"hi|hello|hey",
        ["Hello, How can I help you?", "Hey there! What's up?", "Hi! how's it going?"]
    ],
    [
        r"what is your name?",
        ["I am a simple Chatbot created using Python and NLTK."]
    ],
    [
        r"how are you?",
        ["I'm just a bot, but I'm doing great! How about you?", "I'm good! Thanks for asking."]
    ],
    [
        r"(.*) your name?",
        ["My name is ChatBot. What's yours?", "I am ChatBot, your virtual assistant."]
    ],
    [
        r"(.*) help (.*)",
        ["I can help you with general queries. What do you need help with?", "Sure! Let me know your question."]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day!", "See you later! Take care."]
    ],
    [
        r"(.*)",
        ["I'm not sure how to respond to that. Could you rephrase?", "That's interesting! Tell me more."]
    ]
]


def basic_chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hello, How can I help you?"
    elif "how are you" in user_input:
        return "I'm just a chatbot. I dont have feelings."
    elif "your name" in user_input:
        return "I am a chatbot. What can I do for you?"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand your question."


def create_nltk_chatbot():
    return Chat(CHAT_PAIRS, reflections)
