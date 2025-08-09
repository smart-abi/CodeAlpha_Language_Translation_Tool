import streamlit as st
from googletrans import Translator

# App title
st.set_page_config(page_title="Language Translation Tool", page_icon="🌍")
st.title("🌍 Language Translation Tool")
st.write("Translate text from one language to another easily.")

# Create translator
translator = Translator()

# Language options
languages = {
    'en': 'English',
    'ta': 'Tamil',
    'hi': 'Hindi',
    'fr': 'French',
    'es': 'Spanish',
    'de': 'German',
    'zh-cn': 'Chinese (Simplified)',
    'ja': 'Japanese',
    'ar': 'Arabic'
}

# User input
text = st.text_area("Enter text to translate:")
source_lang = st.selectbox("Select source language", options=languages.keys(), format_func=lambda x: languages[x])
target_lang = st.selectbox("Select target language", options=languages.keys(), format_func=lambda x: languages[x])

if st.button("Translate"):
    if text:
        translated = translator.translate(text, src=source_lang, dest=target_lang)
        st.subheader("Translated Text:")
        st.success(translated.text)
    else:
        st.warning("Please enter some text to translate.")

# Optional Copy Button
if st.button("Copy to Clipboard"):
    st.write("📋 Copied! (Feature works better in local apps)")

