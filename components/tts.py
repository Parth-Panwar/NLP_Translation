from gtts import gTTS
import streamlit as st
import io

def render_tts(text, lang_code):
    if st.button("🔊 Listen"):
        with st.spinner("Generating audio..."):
            tts = gTTS(text=text, lang=lang_code)
            audio_bytes = io.BytesIO()
            tts.write_to_fp(audio_bytes)
            audio_bytes.seek(0)
            st.audio(audio_bytes, format="audio/mp3")