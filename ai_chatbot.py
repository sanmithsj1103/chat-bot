from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline


class AIPoweredChatbot:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()
        self.pipeline = make_pipeline(self.vectorizer, self.model)
        self.train_data()


    def train_data(self):
        training_sentences = [
            "hello", "hi", "hey", "goodbye", "bye", 
            "how are you", "i am fine", "thanks", "thank you",
            "what is your name", "who created you", 
            "tell me a joke", "i love you"
        ]

        responses = [
            "Hi there!", "Hi there!", "Hello!", 
            "Goodbye!", "Bye!", 
            "I'm doing great, thanks!", "That's good to hear!",
            "You're welcome!", "You're welcome!",
            "I'm a chatbot!", "I was created by a developer!",
            "Why don't scientists trust atoms? Because they make up everything!", 
            "I love you too!"
        ]

        self.pipeline.fit(training_sentences, responses)


    def chatbot_response(self, user_input):
        return self.pipeline.predict([user_input])[0]
