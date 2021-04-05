import os
import re
import aiml
import string

from unidecode import unidecode
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = "static"

def clean_input(text):
    text = unidecode(text)
    return text.translate(str.maketrans("", "", string.punctuation)).upper().strip(" ")

def validate_monetary(text):
    return re.match(r"^[1-9]\d{0,2}(\.\d{3})*,\d{2}$", text) is not None

def validate_email(text):
    return re.search(r"^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$", text) is not None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    msg = request.args.get("msg")
    
    if validate_monetary(msg) or validate_email(msg):
        userText = msg
    else:
        userText = clean_input(msg)

    userText = userText.replace(".", "") # remove pontos

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
