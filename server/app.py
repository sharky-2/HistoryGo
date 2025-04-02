import json
from flask import Flask, render_template
from data.resources import modules

app = Flask(__name__)

def load_and_process_context(name_, __path__):
    module = ""
    with open(__path__) as f:
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

                "__path__": __path__,
            }
            
            for i in range(2): context[f'rank{i}'] = char.get(f'rank-{i}')

            module_function = getattr(modules, char.get("type"), None)
            if module_function:
                module += module_function(**context)
    return module

@app.route("/")
def MainPage(): 
    name_ = "main-page"
    __path__ = "data/resources/content/main-page.json"
    module = load_and_process_context(name_, __path__)
    return render_template("main.html", modules=module)

@app.route("/selected-country")
def selected_country(): 
    name_ = "selected-country"
    __path__ = "data/resources/content/italy.json"
    module = load_and_process_context(name_, __path__)
    return render_template("selected-country.html", modules=module)

@app.route("/Test") 
def Test(): 
    name_ = "test-page"
    module = load_and_process_context(name_)
    return render_template("test.html", modules=module)

if __name__ == '__main__':
    app.run(debug=True)
