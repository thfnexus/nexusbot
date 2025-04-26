from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    # simple logic ya apna Q/A json load karke matching kar sakte ho
    if "hello" in user_message.lower():
        bot_response = "Hello! What's up?"
    elif "how old" in user_message.lower():
        bot_response = "I'm timeless!"
    else:
        bot_response = "Sorry, I didn't understand that."
    
    return jsonify({'reply': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
