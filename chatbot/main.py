# Import necessary libraries
from flask import Flask, request, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initialize Flask app
app = Flask(__name__)

# Initialize ChatBot
fitness_bot = ChatBot("FitnessBot")
trainer = ChatterBotCorpusTrainer(fitness_bot)
trainer.train("chatterbot.corpus.english")

# Define routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    bot_response = str(fitness_bot.get_response(user_input))
    return bot_response

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
