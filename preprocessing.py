import string
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


class TextPreprocessing:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stopwords = set(stopwords.words('english'))
    
    def remove_punctuation(self, text):
        return text.translate(str.maketrans('', '', string.punctuation))

    def tokenize(self, text):
        return word_tokenize(text)

    def lemmatize(self, tokens):
        return [self.lemmatizer.lemmatize(token) for token in tokens]

    def remove_stopwords(self, tokens):
        return [token for token in tokens if token not in self.stopwords]

    def preprocess(self, text):
        text = self.remove_punctuation(text)
        text = text.lower()
        tokens = self.tokenize(text)
        tokens = self.lemmatize(tokens)
        # tokens = self.remove_stopwords(tokens)  # Optional
        return " ".join(tokens)
