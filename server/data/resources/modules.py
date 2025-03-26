import json

# -------------------------------------------------------------------------------------------------
# Design
def design(**context):
    title = context.get("title")
    text = context.get("text")

    module = f"""
    """
    return module

# -------------------------------------------------------------------------------------------------
# Header 
def header(**context):
    title = context.get("title")
    subtitle = context.get("subtitle")
    button = context.get("button")
    page_name = context.get("page_name")

    blog_image_amount = 4
    item = ""
    for i in range(blog_image_amount):

        with open("data/resources/content.json") as f:
            data = json.load(f)

        for char in data.get(page_name, []):
            type_ = char.get("type", None)
            if type_ == "header": 

                image = char.get(f"image-{i}", None)                    
                item += f"""<img src="{image}" class="hero-image box-shadow">"""


    module = f"""
    <header>

        <div class="text-frame" style="text-align: center; align-items: center; justify-content: center;">
            <h1 class="title-design text-shadow">{title}</h1>
            <label class="subtitle-design">{subtitle}</label>
            <a href="#"><input type="button" value="{button}" class="blue-button-design box-shadow button-hover"></a>
        </div>

        <div class="hero-container">
            {item}
        </div>
    </header>

    """
    return module

# -------------------------------------------------------------------------------------------------
# Blog 
def blog_2(**context):
    title = context.get("title")
    subtitle = context.get("subtitle")
    text = context.get("text")
    page_name = context.get("page_name")

    blog_image_amount = 5
    item = ""
    for i in range(blog_image_amount):

        with open("data/resources/content.json") as f:
            data = json.load(f)

        for char in data.get(page_name, []):
            type_ = char.get("type", None)
            if type_ == "blog_2": 

                image = char.get(f"image-{i}", None)                    
                item += f"""<img src="{image}" class="box-shadow img-anim">"""


    module = f"""
    <section class="blog-2">
        <div class="top text-frame">
            <h1 class="title-design text-shadow">{title}</h1>
            <label class="subtitle-design">{subtitle}</label>
        </div>
        <div class="bottom">
            <div class="bottom-1">
                <label class="text-design">{text}</label>
            </div>
            <div class="bottom-2">
                <div class="img-frame">
                    {item}
                </div>
            </div>
        </div>
    </section>
    """
    return module

def blog_3(**context):
    title = context.get("title")
    subtitle = context.get("subtitle")
    text = context.get("text")
    text_2 = context.get("text-2")
    page_name = context.get("page_name")

    blog_image_amount = 2
    item = ""
    for i in range(blog_image_amount):

        with open("data/resources/content.json") as f:
            data = json.load(f)

        for char in data.get(page_name, []):
            type_ = char.get("type", None)
            if type_ == "blog_3": 

                image = char.get(f"image-{i}", None)                    
                item += f"""<img src="{image}" class="box-shadow img-anim">"""


    module = f"""
    <section class="blog-3">
        <div class="top text-frame">
            <h1 class="title-design text-shadow">{title}</h1>
            <label class="subtitle-design">{subtitle}</label>
        </div>
        <div class="bottom">
            <div class="bottom-1">
                <label class="text-design">{text}</label>
            </div>
            <div class="bottom-2">
                <label class="text-design">{text_2}</label>
                <div class="img-frame">
                    {item}
                </div>
            </div>
        </div>
    </section>
    """
    return module

def blog_4(**context):
    title = context.get("title")
    subtitle = context.get("subtitle")
    text = context.get("text")
    text_2 = context.get("text-2")
    page_name = context.get("page_name")
    button = context.get("button")

    blog_image_amount = 4
    item = ""
    for i in range(blog_image_amount):

        with open("data/resources/content.json") as f:
            data = json.load(f)

        for char in data.get(page_name, []):
            type_ = char.get("type", None)
            if type_ == "blog_4": 

                image = char.get(f"image-{i}", None)                    
                item += f"""<img src="{image}" class="box-shadow img-anim">"""


    module = f"""
    <section class="blog-4">
        <div class="left">
            <div class="top text-frame">
                <h1 class="title-design text-shadow">{title}.</h1>
                <label class="subtitle-design">{subtitle}</label>
                <a href="#"><input type="button" value="{button}" class="blue-button-design box-shadow button-hover"></a>
            </div>
            <div class="bottom">
                <label class="text-design">{text}</label>
            </div>
        </div>
        <div class="right">
            {item}
        </div>
    </section>
    """
    return module

# -------------------------------------------------------------------------------------------------
# Title
def title_1(**context):
    title = context.get("title")
    subtitle = context.get("subtitle")

    module = f"""
    <section class="title title-1">
        <h1 class="title-design text-shadow">{title}</h1>
        <label class="subtitle-design">{subtitle}</label>
    </section>
    """
    return module

def title_2(**context):
    title = context.get("title")
    subtitle = context.get("subtitle")
    button = context.get("button")

    module = f"""
    <section class="title title-2">
        <div class="textframe">
            <div class="left">
                <h1 class="title-design text-shadow">{title	}</h1>
                <label class="subtitle-design">{subtitle}</label>
            </div>
            <div class="right">
                <a href="#"><input type="button" value="{button}" class="blue-button-design box-shadow button-hover"></a>
            </div>
        </div>
    </section>
    """
    return module

def title_3(**context):
    title = context.get("title")
    subtitle = context.get("subtitle")
    img = context.get("img")

    module = f"""
    <section class="title title-2">
        <div class="textframe">
            <div class="left">
                <h1 class="title-design text-shadow">{title}</h1>
                <label class="subtitle-design">{subtitle}</label>
            </div>
            <div class="right">
                <img src="{img}" class="box-shadow img-anim">
            </div>
        </div>
    </section>
    """
    return module

# -------------------------------------------------------------------------------------------------
# Image 
def img_1(**context):
    page_name = context.get("page_name")

    image_amount = 4
    item = ""
    for i in range(image_amount):

        with open("data/resources/content.json") as f:
            data = json.load(f)

        for char in data.get(page_name, []):
            type_ = char.get("type", None)
            if type_ == "img_1": 

                image = char.get(f"image-{i}", None)                    
                item += f"""<img src="{image}" class="box-shadow">"""

    module = f"""
    <section id="img-1">
        {item}
    </section>
    """
    return module

def img_2(**context):
    page_name = context.get("page_name")

    image_amount = 5
    item = ""
    for i in range(image_amount):

        with open("data/resources/content.json") as f:
            data = json.load(f)

        for char in data.get(page_name, []):
            type_ = char.get("type", None)
            if type_ == "img_2": 

                image = char.get(f"image-{i}", None)                    
                item += f"""<img src="{image}" class="box-shadow ">"""

    module = f"""
    <section id="img-2">
        {item}
    </section>
    """
    return module

def img_3(**context):
    page_name = context.get("page_name")

    image_amount = 3
    item = ""
    for i in range(image_amount):

        with open("data/resources/content.json") as f:
            data = json.load(f)

        for char in data.get(page_name, []):
            type_ = char.get("type", None)
            if type_ == "img_3": 

                image = char.get(f"image-{i}", None)                    
                item += f"""<img src="{image}" class="box-shadow ">"""

    module = f"""
    <section id="img-3">
        {item}
    </section>
    """
    return module

# -------------------------------------------------------------------------------------------------
# Cards
def card(**context):
    page_name = context.get("page_name")
    card_amount = context.get("card_amount")
    item = ""
    for i in range(card_amount):

        with open("data/resources/content.json") as f:
            data = json.load(f)

        for char in data.get(page_name, []):
            type_ = char.get("type", None)
            if type_ == "card": 

                image = char.get(f"image-{i}", None)                    
                title = char.get(f"title-{i}", None)                    
                subtitle = char.get(f"subtitle-{i}", None)   

                item += f"""
                <div class="card">
                    <img src="{image}" class="box-shadow ">
                    <div class="textframe">
                        <h1 class="title-design text-shadow">{title}</h1>
                        <label class="subtitle-design">{subtitle}</label>
                        <code class="subtitle-design rating" style="opacity: 1;">
                            <img src="../static/img/icons/star.png">
                            4.53
                        </code>
                    </div>
                </div>
                """


    module = f"""
    <section id="card-module">
        <div class="cards">
            {item}
        </div>
    </section>
    """
    return module

def card_category(**context):
    page_name = context.get("page_name")
    card_amount = context.get("card_amount")
    title = context.get("title")
    subtitle = context.get("subtitle")


    item = ""
    for i in range(card_amount):

        with open("data/resources/content.json") as f:
            data = json.load(f)

        for char in data.get(page_name, []):
            type_ = char.get("type", None)
            if type_ == "card": 

                image = char.get(f"image-{i}", None)                    
                title_card = char.get(f"title-{i}", None)                    
                subtitle_card = char.get(f"subtitle-{i}", None)   

                item += f"""
                <div class="card">
                    <img src="{image}" class="box-shadow ">
                    <div class="textframe">
                        <h1 class="title-design text-shadow">{title_card}</h1>
                        <label class="subtitle-design">{subtitle_card}</label>
                        <code class="subtitle-design rating" style="opacity: 1;">
                            <img src="../static/img/icons/star.png">
                            4.53
                        </code>
                    </div>
                </div>
                """


    module = f"""
    <section id="card-module">

        <h1 class="title-design text-shadow" style="text-align: center;">{title}</h1>
        <label class="subtitle-design" style="text-align: center;">{subtitle}</label>
        <br>
        <div class="category-frame">
            <div class="button">
                <div class="img box-shadow"><img src="../static/img/icons/star.png"></div>
                <label class="subtitle-design">favorite</label>
            </div>
            <div class="button">
                <div class="img box-shadow"><img src="../static/img/icons/confetti.png"></div>
                <label class="subtitle-design">fun</label>
            </div>
            <div class="button">
                <div class="img box-shadow"><img src="../static/img/icons/island.png"></div>
                <label class="subtitle-design">beach</label>
            </div>
            <div class="button">
                <div class="img box-shadow"><img src="../static/img/icons/castle.png"></div>
                <label class="subtitle-design">castle</label>
            </div>
            <div class="button">
                <div class="img box-shadow"><img src="../static/img/icons/ski.png"></div>
                <label class="subtitle-design">ski</label>
            </div>
            <div class="button">
                <div class="img box-shadow"><img src="../static/img/icons/swimming-man.png"></div>
                <label class="subtitle-design">swim</label>
            </div>
            <div class="button">
                <div class="img box-shadow"><img src="../static/img/icons/sailing-boat.png"></div>
                <label class="subtitle-design">boat</label>
            </div>
            <div class="button">
                <div class="img box-shadow"><img src="../static/img/icons/plane.png"></div>
                <label class="subtitle-design">flying</label>
            </div>
            <div class="button">
                <div class="img box-shadow"><img src="../static/img/icons/sun.png"></div>
                <label class="subtitle-design">sunny</label>
            </div>
           
        </div>

        <div class="cards">
            {item}
        </div>
    </section>
    """
    return module