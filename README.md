# 📈 AI Stock Trading Advisor

An interactive **AI-powered stock analysis and trading advisor** built with **Streamlit**, **CrewAI**, and **Groq Llama 3.3**. This application combines real-time market data from **Yahoo Finance (yfinance)** with intelligent multi-agent reasoning to produce concise market insights and actionable trade recommendations.

---

## 🚀 Features

### 💡 Smart Market Analysis

* Fetches live stock data (price, high/low, volume, and change %) using **Yahoo Finance API**.
* Displays clean, human-readable insights formatted for clarity.

### 🤖 AI Trader Recommendation

* Uses **CrewAI multi-agent orchestration** to coordinate:

  * **Financial Market Analyst Agent** → interprets live data.
  * **Strategic Trader Agent** → issues a BUY, SELL, or HOLD recommendation with reasoning.

### 🧩 Groq Llama 3.3 Integration

* Leverages **Groq's ultra-fast inference engine** with **Llama 3.3 70B** for high-accuracy trading recommendations.

### 🖥️ Streamlit Frontend

* Beautiful and minimal web UI.
* Includes sidebar with tech stack, author info, and disclaimer.
* Provides instant feedback and colored decision highlighting (green = BUY, red = SELL, gold = HOLD).

### ⚡ Graceful Fallbacks

* Displays clear messages if the LLM rate-limit is reached.
* Shows Yahoo Finance summary even when AI analysis is temporarily unavailable.

---

## 🧠 Architecture Overview

```
User Input (Stock Symbol)
       │
       ▼
[Yahoo Finance Tool] ───▶  Live Market Summary (Analyst Insights)
       │
       ▼
[CrewAI Orchestrator] ───▶  Trader Reasoning via Groq Llama 3.3
       │
       ▼
Streamlit Frontend ─────▶  Interactive Output (BUY / SELL / HOLD)
```

---

## 🛠️ Tech Stack

| Layer                  | Technology                     |
| ---------------------- | ------------------------------ |
| **Frontend**           | Streamlit                      |
| **LLM Orchestration**  | CrewAI                         |
| **LLM Backend**        | Groq Llama 3.3 70B via LiteLLM |
| **Market Data Source** | Yahoo Finance (yfinance)       |
| **Environment Config** | python-dotenv                  |

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/ai-stock-trading-advisor.git
cd ai-stock-trading-advisor
```

### 2️⃣ Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Then open your browser at:
👉 **[http://localhost:8501](http://localhost:8501)**

---

## 🧾 Example Output

**Analyst Insights:**

```
Stock: AAPL
Current price: 182.01 USD
Daily change: +0.44%
Day high / low: 183.20 / 181.50
Volume: 51,853,339
Momentum: Slight upward bias
```

**Trader Recommendation:**

```
Recommendation: BUY
Reason: The current price of AAPL shows a stable upward trend and strong trading volume, indicating positive momentum.
```

---

## ⚠️ Disclaimer

This application is developed **solely for educational and entertainment purposes**. It does **not constitute financial advice**. Please perform your own due diligence and consult a licensed financial advisor before making investment decisions.

---

## 👨‍💻 Author

**Alhad Bhadekar**
Software Development Engineer

---

## 🧰 Requirements

See [requirements.txt](./requirements.txt)

---

## 🏗️ Future Enhancements

* 🧮 Sentiment analysis on financial news.
* 📊 Historical trend visualization.
* 🔔 Real-time alerts for threshold movements.
* 🧠 Model fine-tuning with reinforcement feedback.

---

## 🌟 License

MIT License © 2025 Alhad Bhadekar
