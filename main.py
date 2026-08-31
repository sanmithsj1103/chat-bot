from preprocessing import TextPreprocessing
from ai_chatbot import AIPoweredChatbot
from rule_patterns import create_nltk_chatbot, basic_chatbot_response


def main():
    print("="*60)
    print("         Welcome to AI Chatbot Application")
    print("="*60)
    
    preprocessor = TextPreprocessing()
    ai_bot = AIPoweredChatbot()
    nltk_chatbot = create_nltk_chatbot()
    
    print("\nChatbot: Hello, How can I help you?")
    print("(Type 'exit' to quit)\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() == 'exit':
                print("Chatbot: Goodbye! Have a great day!")
                break
            
            if not user_input:
                continue
            
            preprocessed_text = preprocessor.preprocess(user_input)
            
            # Generate response using AI chatbot
            # (You can switch between different chatbot modes)
            response = ai_bot.chatbot_response(preprocessed_text)
            
            # Alternative chatbot modes (uncomment to use):
            # response = nltk_chatbot.respond(preprocessed_text)
            # response = basic_chatbot_response(preprocessed_text)
            
            print(f"Chatbot: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\nChatbot: Goodbye! Have a great day!")
            break
        except Exception as e:
            print(f"Error: {e}")
            print("Chatbot: I encountered an error. Please try again.\n")


if __name__ == "__main__":
    main()

    