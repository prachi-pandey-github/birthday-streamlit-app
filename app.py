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
                terms = ["cute birthday", "happy birthday", "birthday cake", "birthday celebration", "mickey mouse"]
                random.shuffle(terms)
                for term in terms[:3]:
                    st.session_state['gif_urls'].extend(search_giphy(term, GIPHY_API_KEY))
                display_random_gif()
            else:
                st.warning("Giphy API key not provided. GIFs won't be shown.")

# --- WHAT IF SECTION ---
st.markdown("---")
st.subheader("What If? Fun")

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
    with cols[i]:
        if st.button(f"What if Adii were a {key}?"):
            st.image(path, caption=image_labels[key], use_container_width=True)

# --- POEM SECTION ---
st.markdown("---")
st.subheader("A Little Poem for You")

poem = """
I found a friend, and what joy it did bring!
A quiet spark, a gentle start,
Who slowly made home in my heart.
I used to call you a "stranger" once,
But now you’re my bestie, no need to run.
From tiny jokes to talks so deep,
We talk for hours, never bored, we leap.
Our records of calls and chats so long,
We never run out of topics, we just go on!
It all began on August 30th, you texted me,
In the evening, so casually,
A simple ping, and here we are,
Best friends, connected, no distance too far.
You listen, care, and never rush,
Even silence with you feels lush.
You're cute, you're sweet, a little strange,
But perfect — no need to change.
Cute in ways you’ll never know,
You make my quiet moments glow.
So here's my wish, from me to you,
For skies to clear and dreams come true.
May your days be bright, your nights less loud,
And may your code forever make you proud.
I thank you, Tom, for finding me,
For texting me.
For being my friend,
And making sure the laughs don’t end.
You're the best, and here's the thing,
You're my favorite person to annoy and ping!
So, on your birthday, I want to say,
You’re the best in every single way.
I wish all your dreams come true,
May happiness follow all you do.
On your special day, I hope you see,
How much you mean to me.💛
"""

if st.button("Read My Special Poem"):
    st.markdown(f"<div class='poem-text'>{poem}</div>", unsafe_allow_html=True)
    st.image("images/friends.gif", use_container_width=True)

st.markdown("---")
st.write("A little digital birthday surprise for Adii!🧡")
