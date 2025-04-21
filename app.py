import streamlit as st
import random

# --- HELPER FUNCTIONS ---

def display_static_gif(gif_path):
    st.image(gif_path, use_container_width=True)

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
st.markdown("---")

# --- BIRTHDAY WISH ---
personalized_wish = "Dear Adii, Happy Birthday! You're such a wonderful listener, always understanding and caring whenever I need you. Your smartness shines through, and let's be honest, you're also incredibly cute! Thank you for being such a special friend. Wish you a fantastic day!"

# Centering the button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("✨ Show Special Wish ✨"):
        with st.spinner("...."):
            st.image("images/us.png", use_container_width=True)
            st.markdown(f"<p style='font-size: 20px;'>{personalized_wish}</p>", unsafe_allow_html=True)
            st.markdown("---")
            display_static_gif("images/birthdaygif.gif") # Replace with your GIF path


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
From a LinkedIn ping to endless talks,
You walked into my life and rewrote the blocks.
Once a stranger, now my closest one,
With you, even silence feels like fun.

We chat for hours, never run dry,
You get me in ways I can't deny.
Sweet, mature, and oddly cute,
A bond like ours? Nothing can mute.

Thank you for finding me that day, Tom
Stay forever, please, okay? 💛
"""

if st.button("Read a Special Poem"):
    st.markdown(f"<div class='poem-text'>{poem}</div>", unsafe_allow_html=True)
    st.image("images/friends.gif", use_container_width=True)

st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 18px;'>A little digital birthday surprise for Adii!🧡</p>", unsafe_allow_html=True)
