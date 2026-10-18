# AI Chatbot Application

A versatile Python-based chatbot implementation featuring multiple conversation engines and natural language processing capabilities.

## 📋 Project Overview

This project demonstrates three different approaches to building conversational AI:

1. **AI-Powered Chatbot** - Machine learning-based responses using Naive Bayes classification
2. **Rule-Based Chatbot** - Pattern matching using NLTK's Chat utility
3. **Basic Chatbot** - Simple keyword-based responses
4. **Learning Roadmap Chatbot** - Rule-based chatbot using the Gradio platform

The application processes user input through text preprocessing (tokenization, lemmatization, punctuation removal) before generating responses.

## 🏗️ Project Structure

```
chat-bot/
├── main.py                                 # Main application entry point
├── preprocessing.py                        # Text preprocessing module
├── ai_chatbot.py                           # ML-powered chatbot implementation
├── rule_patterns.py                        # Rule-based chatbot and patterns
├── learning_roadmap_chatbot.ipynb          # Chatbot using Gradio.app
├── requirements.txt                        # Project dependencies
└── README.md                               # This file
```

### File Descriptions

- **main.py**: Entry point that initializes all chatbot components and manages the interactive conversation loop
- **preprocessing.py**: Handles text preprocessing including tokenization, lemmatization, and stopword removal
- **ai_chatbot.py**: Implements the machine learning chatbot using scikit-learn's Naive Bayes classifier
- **rule_patterns.py**: Contains rule-based patterns for NLTK Chat and basic keyword matching logic
- **learning_roadmap_chatbot.ipynb**: Provides an offline Gradio chatbot that generates step-by-step learning roadmaps using keyword and fuzzy topic matching

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Navigate to the project directory:
```bash
cd chat-bot
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Download required NLTK data:
```bash
python -m nltk.downloader punkt wordnet averaged_perceptron_tagger stopwords
```

### Running the Application

Start the chatbot application:
```bash
python main.py
```

To run the learning roadmap chatbot, open `learning_roadmap_chatbot.ipynb` in Jupyter Notebook or VS Code and run all cells. The notebook installs Gradio and launches the interactive interface locally.

The chatbot will prompt you with:
```
Chatbot: Hello, How can I help you?
(Type 'exit' to quit)

You: 
```

Type your message and press Enter to get a response. Type `exit` to quit the application.

## 💬 Features

### Text Preprocessing
- **Tokenization**: Breaks text into individual words/tokens
- **Lemmatization**: Converts words to their base form
- **Punctuation Removal**: Cleans up text by removing punctuation
- **Stopwords Removal**: Optional filtering of common words (currently disabled)
- **Lowercasing**: Normalizes text to lowercase

### Chatbot Modes

#### AI-Powered Mode (Default)
Uses machine learning to understand patterns in training data and generate intelligent responses.

```python
response = ai_bot.chatbot_response(preprocessed_text)
```

#### Rule-Based Mode
Uses predefined conversation patterns with NLTK.

```python
response = nltk_chatbot.respond(preprocessed_text)
```

#### Basic Mode
Uses simple keyword matching for quick responses.

```python
response = basic_chatbot_response(preprocessed_text)
```

## 🛠️ Switching Between Chatbot Modes

In `main.py`, uncomment your preferred chatbot mode:

```python
# Generate response using AI chatbot
response = ai_bot.chatbot_response(preprocessed_text)

# OR use rule-based chatbot
# response = nltk_chatbot.respond(preprocessed_text)

# OR use basic chatbot
# response = basic_chatbot_response(preprocessed_text)
```

## 📦 Dependencies

- **nltk**: Natural Language Toolkit for NLP tasks
- **scikit-learn**: Machine learning library for the classifier

See `requirements.txt` for specific versions.

## 🔄 Extending the Chatbot

### Adding New Training Data

Modify the training data in `ai_chatbot.py`:

```python
def train_data(self):
    training_sentences = [
        "your new query", 
        # ... more queries
    ]
    responses = [
        "your new response",
        # ... more responses
    ]
    self.pipeline.fit(training_sentences, responses)
```

### Adding New Patterns

Modify the patterns in `rule_patterns.py`:

```python
CHAT_PAIRS = [
    [
        r"your regex pattern",
        ["response 1", "response 2"]
    ],
    # ... more patterns
]
```

## 📝 Example Conversation

```
You: Hello
Chatbot: Hi there!

You: How are you?
Chatbot: I'm doing great, thanks!

You: What is your name?
Chatbot: I'm a chatbot!

You: exit
Chatbot: Goodbye! Have a great day!
```

## 🎯 Future Enhancements

- Add persistent conversation history
- Implement context awareness for multi-turn conversations
- Integrate with external APIs for real-time information
- Add user feedback mechanism to improve model accuracy
- Implement intent recognition using deep learning
- Add multi-language support
- Create a web-based interface using Flask or FastAPI

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests for improvements

---

**Developed with ❤️ using Python, NLTK, and scikit-learn**
