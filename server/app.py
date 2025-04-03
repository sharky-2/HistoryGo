import json
import subprocess
import sys

from flask import Flask, render_template, request, redirect, url_for, session
from data.resources import modules

app = Flask(__name__)

def load_and_process_context(name_, __path__):
    module = ""
    try:
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
                "__path__": __path__
            }
            
            for i in range(4): 
                context[f'rank{i}'] = char.get(f'rank-{i}')
            
            module_function = getattr(modules, char.get("type"), None)
            if module_function:
                module += module_function(**context)

    except Exception as e:
        print(f"Error loading or processing JSON file: {e}")

    return module

__country__ = "Belgium"
# ---------------------------------------------------------------------------------
# Recive country name from "recomended"
@app.route("/get_country_name", methods=['POST'])
def get_country_name():
    global __country__
    for key in request.form:
        print(request.form)
        print(key)
        __country__ = key

    return redirect(url_for("selected_country"))

# ---------------------------------------------------------------------------------
# Web Sites
@app.route("/", methods=['POST', 'GET'])
def MainPage():
    # if request.method == "POST":
    #     country_name = request.form.get("__country__")
    #     session['__country__'] = country_name
    #     return redirect(url_for("selected_country"))

    name_ = "main-page"
    __path__ = f"data/resources/content/{name_}.json"
    module = load_and_process_context(name_, __path__)
    return render_template("main.html", modules=module)

@app.route("/selected-country")
def selected_country():
    global __country__
    
    if not __country__: return redirect(url_for("MainPage"))

    name_ = "selected-country"
    __path__ = f"data/resources/content/{__country__}.json"
    module = load_and_process_context(name_, __path__)
    return render_template("selected-country.html", modules=module)

if __name__ == '__main__': 
    # subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    app.run(debug=True)
