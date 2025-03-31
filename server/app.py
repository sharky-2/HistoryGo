# pip install flask
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
            "text2": char.get("text2"),
            "text-2": char.get("text-2"),
            "subtitle": char.get("subtitle"),
            "button": char.get("button"),
            "img": char.get("img"),
            "amount": char.get("amount"),

            "page_name": name_,

            "rank0": char.get("rank-0"),
            "rank1": char.get("rank-1"),
            "rank2": char.get("rank-2"),
            "rank3": char.get("rank-3"),
            "rank4": char.get("rank-4")
        }

        module_function = getattr(modules, char.get("type"), None)
        if module_function:
            module += module_function(**context)

    return render_template("main.html", modules = module)

@app.route("/selected-country")
def selected_country(): 
    name_ = "selected-country"
    module = ""

    with open("data/resources/content.json") as f:
        data = json.load(f)

    for char in data.get(name_, []):
        context = {
            "title": char.get("title"),
            "text": char.get("text"),
            "text2": char.get("text2"),
            "text-2": char.get("text-2"),
            "subtitle": char.get("subtitle"),
            "button": char.get("button"),
            "img": char.get("img"),
            "amount": char.get("amount"),

            "page_name": name_,

            "rank0": char.get("rank-0"),
            "rank1": char.get("rank-1"),
            "rank2": char.get("rank-2"),
            "rank3": char.get("rank-3"),
            "rank4": char.get("rank-4")
        }

        module_function = getattr(modules, char.get("type"), None)
        if module_function:
            module += module_function(**context)

    return render_template("selected-country.html", modules = module)

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
            "text2": char.get("text2"),
            "text-2": char.get("text-2"),
            "subtitle": char.get("subtitle"),
            "button": char.get("button"),
            "img": char.get("img"),
            "amount": char.get("amount"),

            "page_name": name_
        }

        module_function = getattr(modules, char.get("type"), None)
        if module_function:
            module += module_function(**context)

    return render_template("test.html", modules = module)

if __name__ == '__main__':
    app.run(debug=True)