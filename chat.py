from flask import Flask, request, jsonify
import nltk
from nltk.tokenize import word_tokenize

app = Flask(__name__)

# A simple chatbot response function
def get_bot_response(message):
    # Tokenize the user message
    user_message = word_tokenize(message.lower())

    # Example responses (you can expand this with more complex logic)
    if "help" in user_message:
        return "How can I assist you? You can ask me about our website navigation."
    elif "contact" in user_message:
        return "You can contact us at contact@example.com."
    elif "products" in user_message:
        return "You can view our products at example.com/products."
    else:
        return "I'm not sure how to help with that. Can you try asking differently?"

# Web route for the chatbot
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')
    return jsonify({'response': get_bot_response(user_message)})

if __name__ == '__main__':
    app.run(debug=True)
