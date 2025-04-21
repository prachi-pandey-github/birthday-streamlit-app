import streamlit as st

import google.generativeai as genai

import requests

import random



# --- CONFIGURATION ---

GEMINI_API_KEY = st.secrets["YOUR_GEMINI_API_KEY"]

GIPHY_API_KEY = st.secrets["YOUR_GIPHY_API_KEY"]



genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-2.0-flash-thinking-exp-01-21')



# --- HELPER FUNCTIONS ---



def generate_personalized_wish(prompt):

    try:

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"Error generating birthday wish: {e}"



def search_giphy(search_term, api_key):

    url = f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={search_term}&limit=5&rating=g"

    response = requests.get(url)

    data = response.json()

    return [gif['images']['fixed_width']['url'] for gif in data.get('data', [])] if data else []



def display_random_gif():

    if st.session_state.get('gif_urls'):

        st.image(random.choice(st.session_state['gif_urls']), use_container_width=True)



# --- SESSION STATE INIT ---

if 'gif_urls' not in st.session_state:

    st.session_state['gif_urls'] = []



# --- CUSTOM CSS ---

st.markdown(

    """

    <style>

        body {

            background-color: #f7f7f7;

            color: #333;

            font-family: sans-serif;

        }

        h1 {

            color: #FF69B4;

            text-align: center;

        }

        p {

            text-align: center;

            font-size: 18px;

        }

        .stButton > button {

            background-color: #7A4988 !important;

            color: white !important;

            font-size: 16px !important;

            border-radius: 8px !important;

            border: none !important;

            padding: 10px 20px !important;

            cursor: pointer !important;

            transition: background-color 0.3s ease !important;

        }

        .stButton > button:hover {

            background-color: #633A70 !important;

        }

        .poem-text {

            font-size: 18px;

            white-space: pre-line;

            color: #555;

            line-height: 1.6;

            border: 1px solid #eee;

            padding: 15px;

            border-radius: 5px;

            background-color: #fff;

        }

    </style>

    """,

    unsafe_allow_html=True

)



# --- HEADER ---

st.markdown("<h1>🎉 Happy Birthday, Aditya! 🎂</h1>", unsafe_allow_html=True)

st.markdown("<p>A little digital surprise just for you!</p>", unsafe_allow_html=True)

st.markdown("---")



# --- BIRTHDAY WISH ---

birthday_prompt = (

    "Write a birthday wish for Adii. Start with 'Dear Adii', focusing on his qualities like listening, caring, "

    "understanding, cute, smart. Make the wish personal and emotional. End by wishing him a fantastic day! "

    "Keep it short and warm."

)



# Centering the button

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    if st.button("✨ Show My Special Wish ✨"):

        with st.spinner("Generating your birthday wish..."):

            birthday_wish = generate_personalized_wish(birthday_prompt)

            st.markdown(f"<p style='font-size: 20px;'>{birthday_wish}</p>", unsafe_allow_html=True)

            st.markdown("---")



            if GIPHY_API_KEY:

                st.session_state['gif_urls'] = []

                terms = ["cute birthday", "happy birthday", "birthday cake", "birthday celebration"]

                random.shuffle(terms)

                for term in terms[:3]:

                    st.session_state['gif_urls'].extend(search_giphy(term, GIPHY_API_KEY))

                display_random_gif()

            else:

                st.warning("Giphy API key not provided. GIFs won't be shown.")



# --- WHAT IF SECTION ---

st.markdown("---")

st.subheader("What If? 🤔")



what_if_images = {

    "animal": "images/owl.jpg",

    "flower": "images/lavender.jpeg",

    "superhero": "images/ironman.jpg",

    "place": "images/place.jpeg"

}



image_labels = {

    "animal": "Adii as an Animal",

    "flower": "Adii as a Flower",

    "superhero": "Adii as a Superhero",

    "place": "Adii as a Place"

}



cols = st.columns(len(what_if_images))

for i, (key, path) in enumerate(what_if_images.items()):

    article = "an" if key[0].lower() in "aeiou" else "a"

    with cols[i]:

        if st.button(f"What if Adii were {article} {key}?"):

            st.image(path, caption=image_labels[key], use_container_width=True)





# --- POEM SECTION ---

st.markdown("---")

st.subheader("A Little Poem for You")



poem = """

You pinged me once, and just like that,

A stranger turned into my favorite chat!

From silly jokes to secrets we share,

You're oddly perfect—beyond compare.

Happy Birthday to you, my dear,

So glad you texted, so glad you're here! 💛

"""



if st.button("Read My Special Poem"):

    st.markdown(f"<div class='poem-text'>{poem}</div>", unsafe_allow_html=True)

    st.image("images/friends.gif", use_container_width=True)



st.markdown("---")

st.markdown("<p style='text-align: center; font-size: 18px;'>A little digital birthday surprise for Adii!🧡</p>", unsafe_allow_html=True)
