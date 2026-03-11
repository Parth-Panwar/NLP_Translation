import streamlit as st
from components.languages import LANGUAGES
from components.translator import translate_text
from components.tts import render_tts

def render_header():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@300;400;500&display=swap');

        html, body, [class*="css"] {
            font-family: 'DM Sans', sans-serif;
            background-color: #0d0d0d;
            color: #f0ece4;
        }

        .stApp {
            background: #0d0d0d;
        }

        .hero {
            text-align: center;
            padding: 3rem 1rem 1.5rem;
        }

        .hero h1 {
            font-family: 'Syne', sans-serif;
            font-size: 3.5rem;
            font-weight: 800;
            letter-spacing: -2px;
            background: linear-gradient(135deg, #f0ece4 30%, #c8f560 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.3rem;
        }

        .hero p {
            color: #888;
            font-size: 1rem;
            font-weight: 300;
            letter-spacing: 0.5px;
        }

        .card {
            background: #1a1a1a;
            border: 1px solid #2a2a2a;
            border-radius: 16px;
            padding: 2rem;
            margin-bottom: 1.5rem;
        }

        .result-card {
            background: #141a0e;
            border: 1px solid #c8f560;
            border-radius: 16px;
            padding: 1.5rem 2rem;
            margin-top: 1.5rem;
        }

        .result-label {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #c8f560;
            margin-bottom: 0.5rem;
            font-weight: 500;
        }

        .result-text {
            font-size: 1.4rem;
            font-weight: 300;
            color: #f0ece4;
            line-height: 1.6;
        }

        div[data-testid="stSelectbox"] label,
        div[data-testid="stTextArea"] label {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #888;
            font-weight: 500;
        }

        div[data-testid="stSelectbox"] > div,
        div[data-testid="stTextArea"] textarea {
            background: #111 !important;
            border: 1px solid #2a2a2a !important;
            border-radius: 10px !important;
            color: #f0ece4 !important;
        }

        div[data-testid="stTextArea"] textarea:focus {
            border-color: #c8f560 !important;
            box-shadow: 0 0 0 2px rgba(200, 245, 96, 0.15) !important;
        }

        .stButton > button {
            background: #c8f560;
            color: #0d0d0d;
            font-family: 'Syne', sans-serif;
            font-weight: 700;
            font-size: 0.9rem;
            letter-spacing: 1px;
            border: none;
            border-radius: 10px;
            padding: 0.65rem 2rem;
            width: 100%;
            transition: all 0.2s ease;
        }

        .stButton > button:hover {
            background: #d9ff70;
            transform: translateY(-1px);
            box-shadow: 0 8px 24px rgba(200, 245, 96, 0.25);
        }

        .stSpinner > div {
            border-top-color: #c8f560 !important;
        }

        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        </style>

        <div class="hero">
            <h1>🌐 Translator</h1>
            <p>Offline translation powered by Hugging Face</p>
        </div>
    """, unsafe_allow_html=True)


def render_translator():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2 = st.columns([3, 1])
    with col1:
        input_text = st.text_area(
            "Your Text",
            placeholder="Type something in English...",
            height=150
        )
    with col2:
        target_language = st.selectbox("Translate To", list(LANGUAGES.keys()))

    if st.button("✦ Translate"):
        if input_text.strip():
            with st.spinner(f"Translating to {target_language}..."):
                result = translate_text(input_text, LANGUAGES[target_language]["translate"])
                st.session_state.translated_text = result
                st.session_state.target_lang_code = LANGUAGES[target_language]["tts"]
        else:
            st.warning("Please enter some text to translate.")

    st.markdown('</div>', unsafe_allow_html=True)

    if "translated_text" in st.session_state and st.session_state.translated_text:
        st.markdown(f"""
            <div class="result-card">
                <div class="result-label">Translation → {target_language}</div>
                <div class="result-text">{st.session_state.translated_text}</div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        render_tts(st.session_state.translated_text, st.session_state.target_lang_code)