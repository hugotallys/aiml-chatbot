import os
import aiml
import string

from unidecode import unidecode
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = "static"

def clean_input(text):
    text = unidecode(text)
    return text.translate(str.maketrans("", "", string.punctuation))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = clean_input(request.args.get("msg"))
    return kernel.respond(userText)

if __name__ == "__main__":

    kernel = aiml.Kernel()

    load_brain = False
    brain_file = "brains/turista_bot_brain.brn"

    if os.path.exists(brain_file) and load_brain:
        kernel.bootstrap(brainFile=brain_file)
    else:
        kernel.bootstrap(learnFiles="turista-bot-startup.xml", commands="load turista bot")
        kernel.saveBrain(brain_file)
    
    app.run()
