import streamlit as st
from transformers import MarianMTModel, MarianTokenizer, MBartForConditionalGeneration, MBart50TokenizerFast

@st.cache_resource
def load_model(target_lang_code):
    if target_lang_code == "ja":
        model_name = "facebook/mbart-large-50-many-to-many-mmt"
        tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
        model = MBartForConditionalGeneration.from_pretrained(model_name)
    else:
        model_name = f"Helsinki-NLP/opus-mt-en-{target_lang_code}"
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

def translate_text(text, target_lang_code):
    tokenizer, model = load_model(target_lang_code)
    
    if target_lang_code == "ja":
        tokenizer.src_lang = "en_XX"
        tokens = tokenizer(text, return_tensors="pt", padding=True)
        translated = model.generate(
            **tokens,
            forced_bos_token_id=tokenizer.lang_code_to_id["ja_XX"]
        )
    else:
        tokens = tokenizer([text], return_tensors="pt", padding=True)
        translated = model.generate(**tokens)
    
    return tokenizer.decode(translated[0], skip_special_tokens=True)