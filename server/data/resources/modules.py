import json
__selected_country__ = "data/resources/content/slovenia.json"
# __path__ = "data/resources/content.json"

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
    __path__ = context.get("__path__")

    amount = 4
    item = ""
    for i in range(amount):

        with open(__path__) as f:
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
    __path__ = context.get("__path__")

    amount = 5
    item = ""
    for i in range(amount):

        with open(__path__) as f:
            data = json.load(f)

        for char in data.get(page_name, []):
            type_ = char.get("type", None)
            if type_ == "blog_2": 

                image = char.get(f"image-{i}", None)                    
                item += f"""<img src="{image}" class="box-shadow ">"""


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
    __path__ = context.get("__path__")

    amount = 2
    item = ""
    for i in range(amount):

        with open(__path__) as f:
            data = json.load(f)

        for char in data.get(page_name, []):
            type_ = char.get("type", None)
            if type_ == "blog_3": 

                image = char.get(f"image-{i}", None)                    
                item += f"""<img src="{image}" class="box-shadow ">"""


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
    __path__ = context.get("__path__")

    amount = 4
    item = ""
    for i in range(amount):

        with open(__path__) as f:
            data = json.load(f)

        for char in data.get(page_name, []):
            type_ = char.get("type", None)
            if type_ == "blog_4": 

                image = char.get(f"image-{i}", None)                    
                item += f"""<img src="{image}" class="box-shadow ">"""


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
    __path__ = context.get("__path__")

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
    __path__ = context.get("__path__")

    module = f"""
    <section class="title title-2">
        <div class="textframe">
            <div class="left">
                <h1 class="title-design text-shadow">{title}</h1>
                <label class="subtitle-design">{subtitle}</label>
            </div>
            <div class="right">
                <img src="{img}" class="box-shadow ">
            </div>
        </div>
    </section>
    """
    return module

# -------------------------------------------------------------------------------------------------
# Image 
def img_1(**context):
    page_name = context.get("page_name")
    __path__ = context.get("__path__")

    amount = 4
    item = ""
    for i in range(amount):

        with open(__path__) as f:
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
    __path__ = context.get("__path__")

    amount = 5
    item = ""
    for i in range(amount):

        with open(__path__) as f:
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
    __path__ = context.get("__path__")

    amount = 3
    item = ""
    for i in range(amount):

        with open(__path__) as f:
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
    amount = context.get("amount")
    __path__ = context.get("__path__")
    item = ""
    for i in range(amount):

        with open(__path__) as f:
            data = json.load(f)

        for char in data.get(page_name, []):
            type_ = char.get("type", None)
            if type_ == "card": 

                image = char.get(f"image-{i}", None)                    
                title = char.get(f"title-{i}", None)                    
                subtitle = char.get(f"subtitle-{i}", None)   

                item += f"""
                <div class="card">
                    <img src="{image}" class="box-shadow">
                    <div class="textframe">
                        <h1 class="title-design text-shadow">{title}</h1>
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

# def card_category(**context):
#     page_name = context.get("page_name")
#     card_amount = context.get("card_amount")
#     title = context.get("title")
#     subtitle = context.get("subtitle")
    # __path__ = context.get("__path__")


#     item = ""
#     for i in range(card_amount):

#         with open(__path__) as f:
#             data = json.load(f)

#         for char in data.get(page_name, []):
#             type_ = char.get("type", None)
#             if type_ == "card_category": 

#                 image = char.get(f"image-{i}", None)                    
#                 title_card = char.get(f"title-{i}", None)                    
#                 subtitle_card = char.get(f"subtitle-{i}", None)   

#                 item += f"""
#                 <div class="card">
#                     <img src="{image}" class="box-shadow ">
#                     <div class="textframe">
#                         <h1 class="title-design text-shadow">{title_card}</h1>
#                         <code class="subtitle-design rating" style="opacity: 1;">
#                             <img src="../static/img/icons/star.png">
#                             4.53
#                         </code>
#                     </div>
#                 </div>
#                 """


#     module = f"""
#     <section id="card-module">

#         <h1 class="title-design text-shadow" style="text-align: center;">{title}</h1>
#         <label class="subtitle-design" style="text-align: center;">{subtitle}</label>
#         <br>
#         <div class="category-frame">
#             <div class="button">
#                 <div class="img box-shadow"><img src="../static/img/icons/star.png"></div>
#                 <label class="subtitle-design">favorite</label>
#             </div>
#             <div class="button">
#                 <div class="img box-shadow"><img src="../static/img/icons/confetti.png"></div>
#                 <label class="subtitle-design">fun</label>
#             </div>
#             <div class="button">
#                 <div class="img box-shadow"><img src="../static/img/icons/island.png"></div>
#                 <label class="subtitle-design">beach</label>
#             </div>
#             <div class="button">
#                 <div class="img box-shadow"><img src="../static/img/icons/castle.png"></div>
#                 <label class="subtitle-design">castle</label>
#             </div>
#             <div class="button">
#                 <div class="img box-shadow"><img src="../static/img/icons/ski.png"></div>
#                 <label class="subtitle-design">ski</label>
#             </div>
#             <div class="button">
#                 <div class="img box-shadow"><img src="../static/img/icons/swimming-man.png"></div>
#                 <label class="subtitle-design">swim</label>
#             </div>
#             <div class="button">
#                 <div class="img box-shadow"><img src="../static/img/icons/sailing-boat.png"></div>
#                 <label class="subtitle-design">boat</label>
#             </div>
#             <div class="button">
#                 <div class="img box-shadow"><img src="../static/img/icons/plane.png"></div>
#                 <label class="subtitle-design">flying</label>
#             </div>
#             <div class="button">
#                 <div class="img box-shadow"><img src="../static/img/icons/sun.png"></div>
#                 <label class="subtitle-design">sunny</label>
#             </div>
           
#         </div>

#         <div class="cards">
#             {item}
#         </div>
#     </section>
#     """
#     return module

# -------------------------------------------------------------------------------------------------
# Image title
def img_title_1(**context):
    page_name = context.get("page_name")
    title = context.get("title")
    subtitle = context.get("subtitle")
    button = context.get("button")
    __path__ = context.get("__path__")

    item = ""
    for i in range(2):

        with open(__path__) as f:
            data = json.load(f)

        for char in data.get(page_name, []):
            type_ = char.get("type", None)
            if type_ == "img_title_1": 

                image = char.get(f"image-{i}", None)        
                item += f"""<img src="{image}" class="box-shadow">"""

    module = f"""
    <section class="img-title-1">
        <div class="textframe">
            <h1 class="title-design text-shadow">{title}</h1>
            <label class="subtitle-design">{subtitle}</label>
            <a href="#"><input type="button" value="{button}" class="blue-button-design box-shadow button-hover"></a>  
        </div>
        <div class="imgframe">
            {item}
        </div>
    </section>
    """
    return module

def img_title_2(**context):
    page_name = context.get("page_name")
    title = context.get("title")
    subtitle = context.get("subtitle")
    button = context.get("button")
    __path__ = context.get("__path__")

    item = ""
    for i in range(4):

        with open(__path__) as f:
            data = json.load(f)

        for char in data.get(page_name, []):
            type_ = char.get("type", None)
            if type_ == "img_title_2": 

                image = char.get(f"image-{i}", None)        
                item += f"""<img src="{image}" class="box-shadow">"""

    module = f"""
    <section class="img-title-2">
        <div class="textframe">
            <h1 class="title-design text-shadow">{title}</h1>
            <label class="subtitle-design">{subtitle}</label>
            <a href="#"><input type="button" value="{button}" class="blue-button-design box-shadow button-hover"></a>  
        </div>
        <div class="imgframe">
            {item}
        </div>
    </section>
    """
    return module

def img_title_3(**context):
    page_name = context.get("page_name")
    title = context.get("title")
    subtitle = context.get("subtitle")
    button = context.get("button")
    __path__ = context.get("__path__")

    item = ""
    for i in range(4):

        with open(__path__) as f:
            data = json.load(f)

        for char in data.get(page_name, []):
            type_ = char.get("type", None)
            if type_ == "img_title_3": 

                image = char.get(f"image-{i}", None)        
                item += f"""<img src="{image}" class="box-shadow">"""

    module = f"""
    <section class="img-title-3">
        <div class="textframe">
            <h1 class="title-design text-shadow">{title}</h1>
            <label class="subtitle-design">{subtitle}</label>
            <a href="#"><input type="button" value="{button}" class="blue-button-design box-shadow button-hover"></a>  
        </div>
        <div class="imgframe">
            {item}
        </div>
    </section>
    """
    return module

def img_title_4(**context):
    page_name = context.get("page_name")
    title = context.get("title")
    subtitle = context.get("subtitle")
    button = context.get("button")
    __path__ = context.get("__path__")

    item = ""
    for i in range(3):

        with open(__path__) as f:
            data = json.load(f)

        for char in data.get(page_name, []):
            type_ = char.get("type", None)
            if type_ == "img_title_4": 

                image = char.get(f"image-{i}", None)        
                item += f"""<img src="{image}" class="box-shadow">"""

    module = f"""
    <section class="img-title-4">
        <div class="imgframe">
            {item}
        </div>
        <div class="textframe">
            <h1 class="title-design text-shadow">{title}</h1>
            <label class="subtitle-design">{subtitle}</label>
        </div>
    </section>
    """
    return module

# -------------------------------------------------------------------------------------------------
# Image text
def image_text(**context):
    page_name = context.get("page_name")
    title = context.get("title")
    text1 = context.get("text")
    text2 = context.get("text2")
    __path__ = context.get("__path__")

    item = ""
    for i in range(5):

        with open(__path__) as f:
            data = json.load(f)

        for char in data.get(page_name, []):
            type_ = char.get("type", None)
            if type_ == "image_text": 

                image = char.get(f"image-{i}", None)        
                item += f"""<img src="{image}" class="box-shadow">"""
                    
    module = f"""
    <section class="image-text">
        <div class="imgframe">
            {item}
        </div>
        <div class="textframe1">
            <label class="text-design">{text1}</label>
        </div>
        <div class="textframe2">
            <h1 class="title-design text-shadow">{title}</h1>
            <label class="text-design">{text2}</label>
        </div>
    </section>
    """
    return module

def destination_spotlight(**context):
    page_name = context.get("page_name")
    title = context.get("title")
    subtitle = context.get("subtitle")
    text = context.get("text")
    button = context.get("button")
    img = context.get("img")
    __path__ = context.get("__path__")
    
    
    rank0 = context.get("rank0")
    rank1 = context.get("rank1")
    rank2 = context.get("rank2")
    
    # item = ""
    # with open(__path__) as f:
    #     data = json.load(f)

    # for char in data.get(page_name, []):
    #     type_ = char.get("type", None)
    #     if type_ == "destination_spotlight": 

    #         for i in range(5): 
    #             rank = char.get(f"rank-{i}", "")   
    #             item += f"""<label>{rank}</label>"""
    #         break
        

    module = f"""
    <section class="destination-spotlight-frame">
        <div class="destination-spotlight">
            <div class="imgframe">
                <img src="{img}" class="box-shadow">
            </div>
            <div class="textframe">
                <code class="number-design">Best places to visit.</code>
                <h1 class="title-design text-shadow">{title}</h1>
                <label class="subtitle-design">{subtitle}</label>
                <br>
                <label class="text-design">{text}</label>
                <a href="#"><input type="button" value="{button}" class="blue-button-design box-shadow button-hover"></a>  

                <div class="ranks-frame">
                    <label>{rank0}</label>
                    <label>{rank1}</label>
                    <label>{rank2}</label>
                </div>
            </div>
        </div>
    </section>
    """
    return module

def left_image_text_2(**context):
    page_name = context.get("page_name")
    title = context.get("title")
    subtitle = context.get("subtitle")
    button = context.get("button")
    __path__ = context.get("__path__")

    item = ""
    for i in range(3):

        with open(__path__) as f:
            data = json.load(f)

        for char in data.get(page_name, []):
            type_ = char.get("type", None)
            if type_ == "left_image_text_2": 

                image = char.get(f"image-{i}", None)        
                item += f"""<img src="{image}" class="box-shadow">"""
                    
    module = f"""
    <section class="left-image-text-2">
        <div class="imgframe">
            {item}
        </div>
        <div class="textframe">
            <h1 class="title-design text-shadow">{title}</h1>
            <label class="subtitle-design">{subtitle}</label>
            <a href="#"><input type="button" value="{button}" class="blue-button-design box-shadow button-hover"></a>  
        </div>
    </section>
    """
    return module

def right_image_text_1(**context):
    page_name = context.get("page_name")
    title = context.get("title")
    subtitle = context.get("subtitle")
    button = context.get("button")
    __path__ = context.get("__path__")

    item = ""
    for i in range(3):

        with open(__path__) as f:
            data = json.load(f)

        for char in data.get(page_name, []):
            type_ = char.get("type", None)
            if type_ == "right_image_text_1": 

                image = char.get(f"image-{i}", None)        
                item += f"""<img src="{image}" class="box-shadow">"""
                    
    module = f"""
    <section class="right-image-text-1">
        <div class="textframe">
            <h1 class="title-design text-shadow">{title}</h1>
            <label class="subtitle-design">{subtitle}</label>
            <a href="#"><input type="button" value="{button}" class="blue-button-design box-shadow button-hover"></a>  
        </div>
        <div class="imgframe">
            {item}
        </div>
    </section>
    """
    return module

# -------------------------------------------------------------------------------------------------
# Recomended trip
def recomended(**context):
    page_name = context.get("page_name")
    title = context.get("title")
    subtitle = context.get("subtitle")
    __path__ = context.get("__path__")

    item = ""
    for i in range(3):

        with open(__path__) as f:
            data = json.load(f)

        for char in data.get(page_name, []):
            type_ = char.get("type", None)
            if type_ == "recomended": 

                image = char.get(f"image-{i}", None)                    
                subtitle_card = char.get(f"subtitle-{i}", None)   

                item += f"""
                <div class="card">
                    <img src="{image}" class="box-shadow" style="width: 100%;">
                    <div class="textframe">
                        <lable class="subtitle-design text-shadow">{subtitle_card}</lable>
                    </div>
                </div>
                """


    module = f"""
    <section id="card-module" class="recomended">
        <div class="titleframe">
            <h1 class="title-design text-shadow">{title}</h1>
            <label class="subtitle-design">{subtitle}</label>
        </div>
        <div class="cards">
            {item}
        </div>
    </section>
    """
    return module