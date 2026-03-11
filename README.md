# 🌐 NLP Translation App

A sleek, offline-capable language translation app built with **Streamlit** and **Hugging Face Transformers**, featuring text-to-speech playback for translated content.

---

## 🚀 Features

- Translate English text into multiple languages
- Offline translation using Hugging Face models
- 🔊 Text-to-speech playback of translations via gTTS
- Clean, modern dark UI
- Component-based project structure

---

## 🌍 Supported Languages

| Language | Translation Model | TTS Support |
|---|---|---|
| Hindi | Helsinki-NLP/opus-mt-en-hi | ✅ |
| Spanish | Helsinki-NLP/opus-mt-en-es | ✅ |
| French | Helsinki-NLP/opus-mt-en-fr | ✅ |
| German | Helsinki-NLP/opus-mt-en-de | ✅ |
| Japanese | facebook/mbart-large-50-many-to-many-mmt | ✅ |

---

## 🛠️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/NLP_Translation.git
cd NLP_Translation
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`.

---

## 📁 Project Structure

```
NLP_Translation/
├── app.py                  # Main Streamlit app
├── components/
│   ├── __init__.py         # Makes components a Python package
│   ├── languages.py        # Language config and code mapping
│   ├── translator.py       # Model loading and translation logic
│   ├── tts.py              # Text-to-speech component
│   └── ui.py               # UI rendering components
├── requirements.txt
└── README.md
```

---

## 📦 Requirements

```
streamlit
transformers
sentencepiece
sacremoses
fugashi
ipadic
torch
gTTS
```

---

## 🤖 Models Used

Models are downloaded automatically from Hugging Face on first use and cached locally at `C:\Users\<you>\.cache\huggingface\hub\`.

| Language | Model | Size |
|---|---|---|
| Hindi, Spanish, French, German | Helsinki-NLP/opus-mt-en-* | ~300MB each |
| Japanese | facebook/mbart-large-50-many-to-many-mmt | ~2.4GB |

> **Note:** The Japanese model is large (~2.4GB). First load will take a few minutes but subsequent loads are instant from cache.

---

## ⚠️ Important Notes

- All translation happens **offline** after models are downloaded
- Internet is only needed for the first model download
- gTTS requires an internet connection for text-to-speech audio generation
- Japanese translation uses `mbart-large-50` for best accuracy

---

## 📄 License

MIT
