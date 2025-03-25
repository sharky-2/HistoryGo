# pip install json flask
import json
from flask import Flask, render_template, request
from server.data import web_page

app = Flask(__name__)
@app.route("/")
def MainPage(): return render_template("index.html")

@app.route("/Test") 
def Test(): 
    name_ = "test-page"
    module = ""

    with open("sesrver/data/web_page.json") as f:
        data = json.load(f)

    for char in data.get(name_, []):
        context = {
            "title": char.get("title"),
            "text": char.get("text"),
            "img": char.get("img"),
            "button": char.get("button"),

            "accordion_amount": char.get("accordion_amount"),
            "image_amount": char.get("image_amount"),
            "blog_amount": char.get("blog_amount"),
            "card_amount": char.get("card_amount"),

            "page_name": name_
        }

        module_function = getattr(web_page, char.get("type"), None)
        if module_function:
            module += module_function(**context)

    return render_template("test.html", modules = module)

if __name__ == '__main__':
    app.run(debug=True)