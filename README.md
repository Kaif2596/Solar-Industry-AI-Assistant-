
## 🌞 Solar Industry AI Assistant 

This project is an AI-powered rooftop solar analysis assistant that evaluates the solar installation potential of rooftops using satellite imagery. Designed for both solar professionals and homeowners, the app uses advanced vision models to assess rooftop suitability and calculate installation recommendations and financial returns.

---
## 📌 Features

**1.)  🔍 Image-Based Analysis:** 

  - Upload or link to a rooftop image and analyze its solar potential using OpenRouter's LLaMA 3.2 Vision model.

**2.)  🤖 AI-Powered Output:** 

 -  Structured insights including:

 - Suitability for solar installation

  - Estimated usable rooftop area

  - Shading issues

  - Model confidence score

  - Summary of rooftop's solar viability

**3.) ⚙️ Installation Planning:**

  - Suggested panel type and count

  - Estimated system capacity

  - Government subsidy estimation

  - Cost breakdown and payback period

**4.) 📏 Efficiency Metric:** 

  - Coverage efficiency (how much area is used for panels)

**5.) 🖥️ Simple Web App Interface:** 

  - Built with Streamlit for easy usage.

  ---
## 🛠️ Tech Stack

**Component**     &nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   **Technology** 

AI Vision Model &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     LLaMA 3.2 Vision via OpenRouter API

Web App  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  Streamlit

Language &nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python

Image Handling &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;base64 + tempfile

Financial Modeling &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Custom cost + ROI logic

---
## 📁 Project Structure

```
├── app.py                # Streamlit UI
├── vision_analyzer.py    # Vision API integration
├── solar_calculator.py   # ROI and solar estimation logic
├── requirements.txt      # Dependencies
├── .env                  # API key (not uploaded)
└── .env.example          # Template for environment variables
```

---
## ⚙️ Setup Instructions (Local)

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
## 📸 Example Usage

-  Open the app

- Choose between uploading an image or pasting an image URL

- Click "Analyze Rooftop"

- View:

  - Structured rooftop analysis

  - Panel recommendation

  - Cost breakdown and ROI insights


  ---
## 📈 Result

Here is a sample result from the Solar Industry AI Assistant Streamlit app after analyzing a rooftop image:

**User Interface:**
![image alt](https://github.com/Kaif2596/Solar-Industry-AI-Assistant-/blob/main/example_images/image%2001.png)

![image alt](https://github.com/Kaif2596/Solar-Industry-AI-Assistant-/blob/main/example_images/image%2002.png)

**Image 1:**
![image alt](https://github.com/Kaif2596/Solar-Industry-AI-Assistant-/blob/main/example_images/Trail%20A.png)

**Result of Image 1:**
![image alt](https://github.com/Kaif2596/Solar-Industry-AI-Assistant-/blob/main/example_images/Trail%20A%20(part%202).png)

**Image 2:**
![image alt](https://github.com/Kaif2596/Solar-Industry-AI-Assistant-/blob/main/example_images/Trail%20B.png)

**Result of Image 2:**
![image alt](https://github.com/Kaif2596/Solar-Industry-AI-Assistant-/blob/main/example_images/Trail%20B%20(part%202).png)


## 🧪 Performance Metrics

Metric  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Description

Panel Coverage Efficiency &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; % of rooftop area used for solar panels

Model Confidence Score &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  LLaMA output confidence (0.0 to 1.0)

Payback Period  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Time to recover investment in years


---
## 🔮 Future Improvements

- We can add support for drawing rooftop area manually

- Use GIS data to auto-estimate azimuth/tilt angles

- Improve ROI model with local electricity rates and weather data

- Add downloadable PDF reports


---
## 👨‍💻 Author

- Name: Mohd Kaif Ansari

- Contact : 9354578826

- Email : kaifansari1808@gmail.com

- LinkedIn : https://www.linkedin.com/in/mohd-kaif-ansari-4a93aa31b/


---
## 📄 Licensing & Credits

- LLaMA 3.2 model via OpenRouter

- UI with Streamlit
