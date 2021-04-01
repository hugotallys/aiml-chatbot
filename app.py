import os
import aiml

from unidecode import unidecode
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    
    userText = unidecode(request.args.get('msg'))

    bot_response = kernel.respond(userText)

    return bot_response

if __name__ == "__main__":

    kernel = aiml.Kernel()

    brain_file = "brains/turista_bot_brain.brn"

    if os.path.exists(brain_file):
        kernel.bootstrap(brainFile=brain_file)
    else:
        kernel.bootstrap(learnFiles="turista-bot-startup.xml", commands="load turista bot")
        kernel.saveBrain(brain_file)
    
    app.run()