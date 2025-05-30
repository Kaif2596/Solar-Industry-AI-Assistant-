
# 🔆 Solar Industry AI Assistant

An AI-powered tool that analyzes satellite rooftop images and provides detailed insights into solar panel installation suitability, recommendations, and ROI estimates.

---

## 🚀 Project Overview

This project is part of an internship assignment that demonstrates AI integration in the solar industry. The assistant uses OpenRouter’s Vision LLM (LLaMA 3.2) to extract structured data from rooftop images and provide actionable solar recommendations.

---

## 🧠 Features

- 🌐 Accepts both **image URL** and **file upload**
- 🧠 Uses **LLaMA 3.2 Vision Model** from OpenRouter for rooftop analysis
- 📊 Calculates **panel count**, **area**, **cost**, **savings**, and **ROI**
- 💸 Government subsidy estimates
- 🛡️ Shading issues & suitability confidence score
- 📉 Payback period and yearly savings
- 📈 Panel coverage efficiency metric

---

## 🖼️ Example Output

```json
{
  "suitable": true,
  "estimated_area_sq_m": 38.2,
  "shading_issues": false,
  "confidence": 0.92,
  "summary": "Rooftop is suitable with minimal shading."
}
```

---

## 🧰 Technologies Used

- 🧠 LLaMA 3.2 Vision (OpenRouter API)
- 🧮 Python
- 🎛️ Streamlit (UI)
- 📡 REST API (`requests`)
- 🔐 dotenv (.env for API security)

---

## 📂 Project Structure

```
├── app.py                # Streamlit UI
├── vision_analyzer.py    # Vision API integration
├── solar_calculator.py   # ROI and solar estimation logic
├── requirements.txt      # Dependencies
├── .env                  # API key (not uploaded)
└── .env.example          # Template for environment variables
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/solar-ai-assistant.git
cd solar-ai-assistant
```

### 2. Create `.env` File

Create a `.env` file and add your API key:

```env
OPENROUTER_API_KEY=your-api-key-here
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 🧪 Example Use Case

- Upload or enter URL of a rooftop image.
- App analyzes and determines if the rooftop is suitable.
- If suitable, app recommends number of panels, total capacity, cost breakdown, and ROI.

---

## 📈 Performance Metrics

- ✅ Valid JSON structure from LLM
- ✅ Response confidence score (0.0–1.0)
- ✅ Accuracy of panel coverage estimates
- ✅ Payback period computed using dynamic solar generation data

---

## 🔐 Security

- API key is stored in `.env` and never exposed publicly.
- `.env` is excluded using `.gitignore`.

---

## 🔮 Future Improvements

- ✅ Add shade heatmaps
- 🔄 Handle low-confidence responses with retries
- 🌍 Support for multiple languages
- 📦 Deploy to Hugging Face or Render

---

## 👨‍💻 Author

**Mohd Kaif Ansari** – AI Enthusiast & Intern  
[LinkedIn](https://linkedin.com) | [GitHub](https://github.com)

---

## 📜 License

This project is for academic & demo purposes.
