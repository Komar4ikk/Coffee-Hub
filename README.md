# Coffee-Hub
Console multi-AI chat hub powered by Gemini, Mistral, and Groq

# ☕ Coffee Hub

A Console-based multi-AI chat hub powered by Python, featuring support for three popular AI providers: Google Gemini, Mistral AI, and Groq Cloud.

## 🚀 Key Features

- **Google Gemini** (`gemini-2.5-flash`) via `google-genai` SDK.
- **Mistral AI** (`mistral-large-latest`) via `mistralai` SDK.
- **Groq Cloud** (`llama-3.3-70b-versatile`) via `groq` SDK, optimized for speed.
- Interactive and stylized CLI menu using the `rich` library.
- Built-in cooldown timers using `tqdm` tailored for free tier API rate limits.
- Persistent conversation history for each provider within the session.

## 🛠️ Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/Komar4ikk/Coffee-Hub.git
cd Coffee-Hub
```

2. **Install the required Python libraries:**
```bash
pip install python-dotenv rich tqdm google-genai mistralai groq
```

3. **Configure your API keys:**
   - Rename the `env.example.txt` file to `env.txt`.
   - Open `env.txt` and paste your actual API keys from the respective provider dashboards:

```env
GEMINI_API_KEY=your_actual_gemini_key
MISTRAL_API_KEY=your_actual_mistral_key
GROQ_API_KEY=your_actual_groq_key
```


   *(Note: The actual `env.txt` file is protected by `.gitignore` and will not be published to GitHub).*

4. **Run the program:**
```bash
python main.py
```

P.S. Sorry, I didn't just make the file .env, but env.txt. I'm too lazy to change the code now, but maybe everything will be fine in the next updates ;)
