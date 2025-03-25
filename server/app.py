# pip install json flask
import json
from flask import Flask, render_template, request
from data.resources import modules

app = Flask(__name__)
@app.route("/")
def MainPage(): 
    name_ = "main-page"
    module = ""

    with open("data/resources/content.json") as f:
        data = json.load(f)

    for char in data.get(name_, []):
        context = {
            "title": char.get("title"),
            "text": char.get("text"),
            "text-2": char.get("text-2"),
            "subtitle": char.get("subtitle"),
            "button": char.get("button"),
            "img": char.get("img"),

            "page_name": name_
        }

        module_function = getattr(modules, char.get("type"), None)
        if module_function:
            module += module_function(**context)

    return render_template("main.html", modules = module)

@app.route("/Test") 
def Test(): 
    name_ = "test-page"
    module = ""

    with open("data/resources/content.json") as f:
        data = json.load(f)

    for char in data.get(name_, []):
        context = {
            "title": char.get("title"),
            "text": char.get("text"),
            "text-2": char.get("text-2"),
            "subtitle": char.get("subtitle"),
            "button": char.get("button"),
            "img": char.get("img"),

            "page_name": name_
        }

        module_function = getattr(modules, char.get("type"), None)
        if module_function:
            module += module_function(**context)

    return render_template("test.html", modules = module)

if __name__ == '__main__':
    app.run(debug=True)