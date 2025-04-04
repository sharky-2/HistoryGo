// Accordion script
let accordion_list = document.querySelectorAll("#accordion-list .item")
accordion_list.forEach(item => {
    item.addEventListener("click", function() {
        if (item.classList.contains("active")) {
            item.classList.remove("active")
        } else {
            accordion_list.forEach(el => el.classList.remove("active"))
            item.classList.add("active")
        } 
    })
})

// Map texts
const country_info_list = {
    italy: {
        subtitle: "A Timeless Journey Through Art, Culture, and Cuisine",
        text: "Italy is a captivating country where ancient history meets modern vibrancy. Explore Rome’s Colosseum, Florence’s Renaissance art, and Venice’s romantic canals. From the sunlit Amalfi Coast to Tuscany’s rolling hills, Italy’s landscapes are stunning. Enjoy regional culinary delights like Neapolitan pizza, handmade pasta, and creamy gelato. Italian festivals celebrate food, music, and tradition, reflecting the passion of its people. Whether wandering Milan’s fashion streets or tasting wine in Sicily, Italy offers unforgettable experiences rooted in culture and community. Embrace the spirit of La Dolce Vita and Italy’s timeless charm.",
        img1: "../static/img/country/Italy/AmalfiCoast.png",
        img2: "../static/img/country/Italy/Florence.png",
        img3: "../static/img/country/Italy/Naples.png",
        img4: "../static/img/country/Italy/Milan.png"
    },
    slovenia: {
        subtitle: "A Hidden Gem of Natural Wonders and Rich Traditions",
        text: "Slovenia, a small European gem, captivates with its natural beauty and cultural charm. Discover Lake Bled’s emerald waters, the Julian Alps’ peaks, and Ljubljana’s vibrant energy. Famous for its wines from Maribor and Vipava Valley, Slovenia blends tradition with eco-friendly practices. Visit Postojna Cave, hike in Triglav National Park, and savor dishes like potica. The capital’s Baroque architecture and riverside cafes offer a relaxed vibe. Slovenia’s festivals and love for nature make it a welcoming destination where heritage and modernity coexist harmoniously.",
        img1: "../static/img/country/Slovenia/LakeBohinj.png",
        img2: "../static/img/country/Slovenia/Piran.png",
        img3: "../static/img/country/Slovenia/LjubljanaMarshes.png",
        img4: "../static/img/country/Slovenia/PostojnaCave.png"
    },
    belgium: {
        subtitle: "A Blend of Medieval Charm, Modern Creativity, and Culinary Excellence",
        text: "Belgium, in the heart of Europe, is rich in history and culture. Explore medieval towns, grand squares, and artistic heritage in cities like Brussels and Bruges. The Grand Place and Atomium reflect the country’s diversity. Belgium’s culinary scene is world-famous, offering chocolates, beers, waffles, and fries. Festivals celebrate art, music, and gastronomy. Whether exploring Antwerp’s vibrant art scene or savoring fries in Ghent, Belgium blends old-world charm with modern creativity. Discover a nation where culture, tradition, and innovation meet.",
        img1: "../static/img/country/Belgium/Ardennes.png",
        img2: "../static/img/country/Belgium/Belgian Coast.png",
        img3: "../static/img/country/Belgium/Flanders.png",
        img4: "../static/img/country/Belgium/Wallonia.png"
    },
    france: {
        subtitle: "A Symphony of Art, History, and Gastronomy",
        text: "France, a timeless symbol of culture and elegance, is a country that captivates with its blend of history, art, and culinary delights. From the romantic streets of Paris to the sun-drenched vineyards of Bordeaux, France offers a diverse landscape of experiences. Iconic landmarks like the Eiffel Tower, the Louvre, and Notre-Dame embody centuries of history and art. The French Riviera and Provence showcase the country’s natural beauty, while regions like Normandy and Loire Valley are steeped in medieval charm. Known for its exquisite cuisine and wine, France is a paradise for food lovers.",
        img1: "../static/img/country/France/bordeaux.png",
        img2: "../static/img/country/France/lyon.png",
        img3: "../static/img/country/France/marseille.png",
        img4: "../static/img/country/France/paris.png"
    }
    
}

function displayCountry(country) {
    const title = document.getElementById("country-title")
    const subtitle = document.getElementById("country-subtitle")
    const text = document.getElementById("country-text")
    const countryButton = document.getElementById("__country__")

    const img1 = document.getElementById("img1")
    const img2 = document.getElementById("img2")
    const img3 = document.getElementById("img3")
    const img4 = document.getElementById("img4")


    if (countryButton) {
        countryButton.setAttribute("name", country.toLowerCase())
        countryButton.setAttribute("value", "Explore " + country + " more") 
    }

    if (country_info_list[country]) {
        title.innerText = country.charAt(0).toUpperCase() + country.slice(1)
        subtitle.innerText = country_info_list[country].subtitle
        text.innerText = country_info_list[country].text
        img1.setAttribute("src", country_info_list[country].img1)
        img2.setAttribute("src", country_info_list[country].img2)
        img3.setAttribute("src", country_info_list[country].img3)
        img4.setAttribute("src", country_info_list[country].img4)
    } else {
        title.innerText = "Country not found"
        subtitle.innerText = ""
        text.innerText = ""
    }

    const images = document.querySelectorAll(".country-map")
    images.forEach(img => {
        img.classList.remove("active")
        img.style.opacity = 0.3 
    })

    const clickedImage = document.getElementById(country)
    clickedImage.classList.add("active") 
    clickedImage.style.opacity = 1

}

// Recomended countries
function display_recomended_countrys() {
    const frame = document.getElementById("recomended-cards-frame")
    const countries = [
        {
            "name": "Slovenia",
            "subtitle": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
            "img": "../static/img/country/Slovenia/Piran.png",
        },
        {
            "name": "Italy",
            "subtitle": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
            "img": "../static/img/country/Italy/Rome.png",
        },
        {
            "name": "Belgium",
            "subtitle": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
            "img": "../static/img/country/Belgium/Brussels.png",
        }
    ]
    countries.forEach(country => {
        const card = `
        <form method="POST" action="/get_country_name">
            <div class="card">
                <img src="${country.img}" class="box-shadow" style="width: 100%;">
                <div class="textframe">
                    <lable class="subtitle-design text-shadow">${country.subtitle}/lable>
                </div>
                <input class="button-design" type="submit" name="${country.name.toLowerCase()}" value="${country.name.toLowerCase()}">    
            </div>
        </form>
        `
        frame.innerHTML += card
    });
}
display_recomended_countrys()