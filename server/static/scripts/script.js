// ================================================================
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

// ================================================================
// Map texts
const country_info_list = {
    italy: {
        subtitle: "A Timeless Journey Through Art, Culture, and Cuisine",
        text: "Italy is a captivating country where ancient history meets modern vibrancy. Explore Rome’s Colosseum, Florence’s Renaissance art, and Venice’s romantic canals. From the sunlit Amalfi Coast to Tuscany’s rolling hills, Italy’s landscapes are stunning. Enjoy regional culinary delights like Neapolitan pizza, handmade pasta, and creamy gelato. Italian festivals celebrate food, music, and tradition, reflecting the passion of its people. Whether wandering Milan’s fashion streets or tasting wine in Sicily, Italy offers unforgettable experiences rooted in culture and community. Embrace the spirit of La Dolce Vita and Italy’s timeless charm.",
        img1: "../static/img/country/Italy/AmalfiCoast.png",
        img2: "../static/img/country/Italy/Florence.png",
        img3: "../static/img/country/Italy/Naples.png",
        img4: "../static/img/country/Italy/Milan.png",
        count: 0
    },
    slovenia: {
        subtitle: "A Hidden Gem of Natural Wonders and Rich Traditions",
        text: "Slovenia, a small European gem, captivates with its natural beauty and cultural charm. Discover Lake Bled’s emerald waters, the Julian Alps’ peaks, and Ljubljana’s vibrant energy. Famous for its wines from Maribor and Vipava Valley, Slovenia blends tradition with eco-friendly practices. Visit Postojna Cave, hike in Triglav National Park, and savor dishes like potica. The capital’s Baroque architecture and riverside cafes offer a relaxed vibe. Slovenia’s festivals and love for nature make it a welcoming destination where heritage and modernity coexist harmoniously.",
        img1: "../static/img/country/Slovenia/LakeBohinj.png",
        img2: "../static/img/country/Slovenia/Piran.png",
        img3: "../static/img/country/Slovenia/LjubljanaMarshes.png",
        img4: "../static/img/country/Slovenia/PostojnaCave.png",
        count: 0
    },
    belgium: {
        subtitle: "A Blend of Medieval Charm, Modern Creativity, and Culinary Excellence",
        text: "Belgium, in the heart of Europe, is rich in history and culture. Explore medieval towns, grand squares, and artistic heritage in cities like Brussels and Bruges. The Grand Place and Atomium reflect the country’s diversity. Belgium’s culinary scene is world-famous, offering chocolates, beers, waffles, and fries. Festivals celebrate art, music, and gastronomy. Whether exploring Antwerp’s vibrant art scene or savoring fries in Ghent, Belgium blends old-world charm with modern creativity. Discover a nation where culture, tradition, and innovation meet.",
        img1: "../static/img/country/Belgium/Ardennes.png",
        img2: "../static/img/country/Belgium/Belgian Coast.png",
        img3: "../static/img/country/Belgium/Flanders.png",
        img4: "../static/img/country/Belgium/Wallonia.png",
        count: 0
    },
    france: {
        subtitle: "A Symphony of Art, History, and Gastronomy",
        text: "France, a timeless symbol of culture and elegance, is a country that captivates with its blend of history, art, and culinary delights. From the romantic streets of Paris to the sun-drenched vineyards of Bordeaux, France offers a diverse landscape of experiences. Iconic landmarks like the Eiffel Tower, the Louvre, and Notre-Dame embody centuries of history and art. The French Riviera and Provence showcase the country’s natural beauty, while regions like Normandy and Loire Valley are steeped in medieval charm. Known for its exquisite cuisine and wine, France is a paradise for food lovers.",
        img1: "../static/img/country/France/bordeaux.png",
        img2: "../static/img/country/France/lyon.png",
        img3: "../static/img/country/France/marseille.png",
        img4: "../static/img/country/France/paris.png",
        count: 0
    },
    austria: {
        subtitle: "A Tapestry of Music, Alps, and Imperial Grandeur",
        text: "Austria, a country where the beauty of the Alps meets a rich history of music and imperial grandeur, offers a mesmerizing mix of culture and natural beauty. Vienna, the city of music, is home to timeless architecture, grand palaces, and world-renowned opera houses. Salzburg, the birthplace of Mozart, echoes with classical harmony, while Innsbruck's alpine landscapes offer outdoor adventure year-round. Hallstatt, a fairy-tale village, is a UNESCO World Heritage site surrounded by stunning mountains and serene lakes, while Graz boasts a vibrant arts scene and medieval charm.",
        img1: "../static/img/country/Austria/graz.png",
        img2: "../static/img/country/Austria/hallstatt.png",
        img3: "../static/img/country/Austria/innsbruck.png",
        img4: "../static/img/country/Austria/salzburg.png",
        count: 0
    },
    bulgaria: {
        subtitle: "A Land of Ancient History, Rose Valleys, and Mountain Majesty",
        text: "Bulgaria, a country where centuries-old history meets natural splendor, offers a rich mosaic of cultures, traditions, and breathtaking landscapes. Sofia, the vibrant capital, blends Roman ruins with dynamic modern life. Plovdiv, one of the oldest cities in Europe, charms with its cobbled streets and Roman amphitheater. The Rila Monastery, nestled in majestic mountains, stands as a spiritual and architectural gem. The Valley of the Roses blooms with beauty and tradition, while the Black Sea coast—from Sunny Beach to Sozopol—offers golden sands and seaside charm. Bansko and the Pirin Mountains call to adventurers year-round with skiing, hiking, and folklore.",
        img1: "../static/img/country/Bulgaria/burgas.png",
        img2: "../static/img/country/Bulgaria/plovdiv.png",
        img3: "../static/img/country/Bulgaria/sofija.png",
        img4: "../static/img/country/Bulgaria/varna.png",
        count: 0
    },
    croatia: {
        subtitle: "A Land of Medieval Charm, Island Escapes, and Adriatic Allure",
        text: "Croatia, a coastal treasure along the Adriatic Sea, captivates with its blend of historic cities, sun-drenched islands, and crystal-clear waters. Dubrovnik, the 'Pearl of the Adriatic', enchants with its ancient city walls and baroque beauty. Zagreb, the capital, pulses with cultural energy and architectural elegance. Split, home to Diocletian’s Palace, combines Roman heritage with vibrant seaside life. Hvar Island tempts travelers with lavender fields, nightlife, and Venetian charm, while Pula reveals a Roman amphitheater and coastal serenity. From national parks like Plitvice Lakes to its dazzling coastline, Croatia invites you to explore its timeless wonders.",
        img1: "../static/img/country/Croatia/dubrovnik.png",
        img2: "../static/img/country/Croatia/zagreb.png",
        img3: "../static/img/country/Croatia/split.png",
        img4: "../static/img/country/Croatia/otokhvar.png",
        count: 0
    },
    czechia: {
        subtitle: "A Land of Castles, Cobblestones, and Bohemian Beauty",
        text: "The Czech Republic, nestled in the heart of Europe, is a captivating blend of medieval towns, ornate castles, and timeless charm. Prague, the 'City of a Hundred Spires', amazes with its Gothic cathedrals, baroque architecture, and vibrant cultural scene. Český Krumlov enchants with fairy-tale streets and a majestic castle overlooking the Vltava River. Brno offers a youthful energy, modernist landmarks, and rich Moravian traditions. Kutná Hora reveals its historic wealth through dramatic cathedrals and the eerie Sedlec Ossuary. From spa towns like Karlovy Vary to tranquil countryside landscapes, the Czech Republic invites you to step into history and beauty.",
        img1: "../static/img/country/Czech_Republic/brno.png",
        img2: "../static/img/country/Czech_Republic/ceskykrumlov.png",
        img3: "../static/img/country/Czech_Republic/praga.png",
        img4: "../static/img/country/Czech_Republic/kutnahora.png",
        count: 0
    },
    greece: {
        subtitle: "A Land of Ancient Wonders and Mediterranean Beauty",
        text: "Greece is a country rich in history and natural beauty, offering a unique blend of ancient ruins, sun-kissed islands, and vibrant culture. Explore the ancient Acropolis in Athens, stroll along the beautiful beaches of the Greek Islands, and immerse yourself in the Mediterranean lifestyle. Greece is known for its delicious cuisine, including souvlaki, tzatziki, and baklava. From the white-washed buildings of Santorini to the rich history of Crete, Greece is a timeless destination for history buffs, nature lovers, and beachgoers alike.",
        img1: "../static/img/country/Greece/athens.png",
        img2: "../static/img/country/Greece/corfu.png",
        img3: "../static/img/country/Greece/thessaloniki.png",
        img4: "../static/img/country/Greece/kalambaka.png",
        count: 0
    },
    germany: {
        subtitle: "A Land of Castles, Culture, and Engineering Excellence",
        text: "Germany is a country rich in history, culture, and natural beauty. Explore the vibrant capital, Berlin, with its blend of modernity and historic sites like the Brandenburg Gate and the Berlin Wall. Visit Bavaria’s fairytale castles, such as Neuschwanstein, or enjoy the charm of medieval towns like Rothenburg ob der Tauber. Germany is also known for its contributions to music, philosophy, and engineering, from the classical sounds of Bach to the precision of German engineering. With stunning landscapes from the Black Forest to the Rhine Valley, Germany offers a perfect mix of history, culture, and outdoor adventures.",
        img1: "../static/img/country/Germany/berlin.png",
        img2: "../static/img/country/Germany/frankfurt.png",
        img3: "../static/img/country/Germany/munchen.png",
        img4: "../static/img/country/Germany/dresden.png",
        count: 0
    },
    denmark: {
        subtitle: "A Land of Royalty, Modern Design, and Scenic Coastlines",
        text: "Denmark, known for its rich history, modern design, and beautiful landscapes, offers a mix of old-world charm and contemporary innovation. The capital, Copenhagen, is famous for its iconic landmarks like the Little Mermaid statue, Tivoli Gardens, and the Nyhavn waterfront. Denmark’s coastal beauty, from the sandy beaches of Jutland to the islands of Funen and Zealand, provides countless outdoor activities. The country is a leader in sustainable living, and its design scene is world-renowned. Denmark is also home to a vibrant culinary scene, including New Nordic cuisine and delicious pastries like Danish pastries.",
        img1: "../static/img/country/Denmark/Aarhus.png",
        img2: "../static/img/country/Denmark/Kolding.png",
        img3: "../static/img/country/Denmark/roskildecathedral.png",
        img4: "../static/img/country/Denmark/helsingor.png",
        count: 0
    },    
    // ========================================================================
    // IMAGES NEEDED
    romania: {
        subtitle: "A Land of Castles, Carpathian Mountains, and Rich Folklore",
        text: "Romania is a captivating country full of medieval castles, mystical landscapes, and a rich cultural heritage. The medieval town of Brasov is a charming gateway to the Carpathian Mountains, home to the famous Bran Castle (Dracula's Castle). Bucharest, the capital, mixes history and modernity, while Transylvania offers picturesque villages, fortified churches, and breathtaking natural beauty. Romania’s diverse landscapes, from mountains to beaches, make it a perfect destination for adventure seekers and history lovers alike.",
        img1: "../static/img/country/Romania/brasov.png",
        img2: "../static/img/country/Romania/bucharest.png",
        img3: "../static/img/country/Romania/transylvania.png",
        img4: "../static/img/country/Romania/varna.png",
        count: 0
    },
    poland: {
        subtitle: "A Land of History, Heritage, and Natural Beauty",
        text: "Poland, a country of profound history and stunning landscapes, invites travelers to explore medieval castles, UNESCO World Heritage sites, and vibrant cities. Warsaw, the capital, has a blend of modern and historical landmarks, while Kraków’s Old Town, with its charming streets and Rynek Square, offers a glimpse into the past. The Białowieża Forest, a UNESCO site, is home to Europe's last wild bison. Poland's rich culture, historical landmarks, and natural beauty make it a unique destination.",
        img1: "../static/img/country/Poland/krakow.png",
        img2: "../static/img/country/Poland/warsaw.png",
        img3: "../static/img/country/Poland/bialowieza.png",
        img4: "../static/img/country/Poland/varna.png",
        count: 0
    },
    spain: {
        subtitle: "A Fiesta of Culture, History, and Passion",
        text: "Spain is a vibrant country known for its lively culture, rich history, and stunning landscapes. From the bustling streets of Madrid and Barcelona to the tranquil beaches of Costa Brava and the Balearic Islands, Spain offers something for everyone. Enjoy traditional dishes like paella, tapas, and churros, and experience flamenco dancing, bullfighting, and colorful festivals. Spain’s architecture, including Gaudí’s Sagrada Familia and the Alhambra, reflects its deep cultural heritage.",
        img1: "../static/img/country/Spain/barcelona.png",
        img2: "../static/img/country/Spain/madrid.png",
        img3: "../static/img/country/Spain/costa_brava.png",
        img4: "../static/img/country/Spain/varna.png",
        count: 0
    },
    portugal: {
        subtitle: "A Rich Tapestry of History, Coastline, and Culinary Delights",
        text: "Portugal, with its stunning coastlines, rich history, and vibrant culture, is an enchanting destination. The capital, Lisbon, is known for its charming neighborhoods, colorful streets, and historic landmarks. Porto, famous for its port wine, offers cobblestone streets and beautiful riverside views. The Algarve’s golden beaches attract sun-seekers, while Portugal’s interior boasts charming towns like Sintra, with its fairy-tale palaces. Enjoy Portuguese cuisine, including seafood dishes, pastel de nata, and world-class wines.",
        img1: "../static/img/country/Portugal/lisbon.png",
        img2: "../static/img/country/Portugal/porto.png",
        img3: "../static/img/country/Portugal/algarve.png",
        img4: "../static/img/country/Portugal/varna.png",
        count: 0
    },
    ireland: {
        subtitle: "A Land of Rolling Green Hills, Ancient Ruins, and Rich Traditions",
        text: "Ireland, known for its lush green landscapes, ancient castles, and vibrant culture, offers a truly magical experience. Explore Dublin’s lively streets, visit the Cliffs of Moher for breathtaking views, and immerse yourself in the country’s rich literary heritage. Discover medieval castles, such as Blarney Castle, and enjoy a pint of Guinness in a traditional pub. Ireland’s music, folklore, and festive spirit make it an unforgettable destination.",
        img1: "../static/img/country/Ireland/dublin.png",
        img2: "../static/img/country/Ireland/cliffs.png",
        img3: "../static/img/country/Ireland/blarney.png",
        img4: "../static/img/country/Ireland/varna.png",
        count: 0
    },
    sweden: {
        subtitle: "A Land of Modern Design, Nature, and Vibrant Cities",
        text: "Sweden is a country that effortlessly blends modern design, natural beauty, and a rich cultural heritage. Stockholm, the capital, is spread across 14 islands and offers a stunning combination of historical sites and contemporary attractions. From the serene landscapes of Swedish Lapland to the bustling streets of Gothenburg, Sweden’s variety of experiences is unmatched. Explore the country’s love for design, innovation, and sustainability, and enjoy a range of outdoor activities from hiking and skiing to ice fishing.",
        img1: "../static/img/country/Sweden/stockholm.png",
        img2: "../static/img/country/Sweden/gothenburg.png",
        img3: "../static/img/country/Sweden/lapland.png",
        img4: "../static/img/country/Sweden/varna.png",
        count: 0
    },
    // ========================================================================
    estonia: {
        subtitle: "A Land of Medieval Castles, Coastal Beauty, and Digital Innovation",
        text: "Estonia, a country where medieval charm meets modern technology, offers a unique blend of history, nature, and innovation. The capital, Tallinn, is renowned for its beautifully preserved Old Town, a UNESCO World Heritage site, with cobblestone streets and medieval architecture. Estonia’s natural landscapes include pristine beaches, dense forests, and serene lakes. Known for its digital advancements, Estonia is one of the most digitally advanced countries in the world. Explore the vibrant culture, cutting-edge technology, and peaceful natural beauty that make Estonia an intriguing destination.",
        img1: "../static/img/country/Estonia/tartu.png",
        img2: "../static/img/country/Estonia/rakvere.png",
        img3: "../static/img/country/Estonia/narva.png",
        img4: "../static/img/country/Estonia/kuressaare.png",
        count: 0
    },
    finland: {
        subtitle: "A Land of Saunas, Northern Lights, and Natural Wonders",
        text: "Finland, known for its pristine nature, is a country where tranquility and adventure coexist. Explore the vibrant capital, Helsinki, with its unique blend of modern architecture and natural beauty. Venture to Lapland to experience the magical Northern Lights and visit Santa Claus Village. Finland’s thousands of lakes, forests, and islands offer countless outdoor activities, from hiking and skiing to ice fishing. Enjoy the Finnish tradition of sauna and savor Finnish cuisine, including salmon, berries, and rye bread. Finland is a perfect destination for those seeking both relaxation and adventure.",
        img1: "../static/img/country/Finland/helsinki.png",
        img2: "../static/img/country/Finland/porvoo.png",
        img3: "../static/img/country/Finland/turku.png",
        img4: "../static/img/country/Finland/rovaniemi.png",
        count: 0
    }    
}


var count_clicks = 0
function displayCountry(country) {

    // ==========================================================
    // Easter egg - Rominski šefe
    const img = "../static/img/image.webp"
    if (country == "romania") {
        const countryImg = document.getElementById(country);
        count_clicks += 1

        if (count_clicks == 5) {
            countryImg.src = "../static/img/image.webp";
            countryImg.style.width = "100px"
        }
    }
    // ==========================================================

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

// ================================================================
// Recomended countries
function display_recomended_countrys() {
    const frame = document.getElementById("recomended-cards-frame");
    if (!frame) return;

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
        },
        {
            "name": "Austria",
            "subtitle": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
            "img": "../static/img/country/Austria/vienne.png"
        },
        {
            "name": "France",
            "subtitle": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
            "img": "../static/img/country/France/Paris.png"
        },
        {
            "name": "Bulgaria",
            "subtitle": "A land of ancient history, scenic beauty, and vibrant traditions in the heart of the Balkans.",
            "img": "../static/img/country/Bulgaria/sofija.png"
        },
        {
            "name": "Croatia",
            "subtitle": "A coastal paradise of medieval cities, turquoise waters, and rich cultural heritage along the Adriatic Sea.",
            "img": "../static/img/country/Croatia/dubrovnik.png"
        }
        
    ];

    function shuffleArray(arr) {
        for (let i = arr.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [arr[i], arr[j]] = [arr[j], arr[i]]; 
        }
    }

    shuffleArray(countries);
    const randomCountries = countries.slice(0, 3);

    frame.innerHTML = '';

    randomCountries.forEach(country => {
        const card = `
        <form method="POST" action="/get_country_name">
            <div class="card">
                <img src="${country.img}" class="box-shadow" style="width: 100%;">
                <div class="textframe">
                    <label class="subtitle-design text-shadow">${country.subtitle}</label>
                    <input class="button-design" type="submit" name="${country.name.toLowerCase()}" value="${country.name.toLowerCase()}">    
                </div>
            </div>
        </form>
        `;
        frame.innerHTML += card;
    });
}

// ================================================================
// Sign In
var step = 0
function displayInputs() {

    const label = document.getElementById("label")
    const button = document.getElementById("submit-button")

    const client_name = document.getElementById("name")
    const client_surname = document.getElementById("surname")
    
    const client_email = document.getElementById("email")
    const client_password = document.getElementById("password")

    step += 1
    label.style.color = ""
    if (step == 1) {

        if (!client_name.value.trim() || !client_surname.value.trim()) {
            label.innerText = "You forgot to input name or surname!"
            label.style.color = "red"
            step = 0
            return
        }

        label.innerText = "Email"
        client_name.style.display = "none"
        client_surname.style.display = "none"
        client_email.style.display = "flex"
    } else if (step == 2) {

        if (!client_email.value.trim()) {
            label.innerText = "You forgot to input email!"
            label.style.color = "red"
            step = 1
            return
        }

        label.innerText = "Password"
        client_email.style.display = "none"
        client_password.style.display = "flex"

        button.value = "Create"
        button.onclick = function() {

            if (!client_password.value.trim()) {
                label.innerText = "You forgot to input password!"
                label.style.color = "red"
                step = 2
                return
            }

            register()
        }
    }
}
display_recomended_countrys()