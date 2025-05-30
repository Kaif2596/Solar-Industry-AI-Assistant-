import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()


# Replace these with your actual credentials
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
YOUR_SITE_URL = "your-site-url.com"      # Optional
YOUR_SITE_NAME = "Solar Rooftop AI"      # Optional

def analyze_rooftop_image(image_url):
    """
    Sends a rooftop image to OpenRouter's LLaMA 3.2 Vision model and gets solar analysis.
    Returns a structured JSON with:
    - suitable (bool)
    - estimated_area_sq_m (float)
    - shading_issues (bool)
    - confidence (0.0–1.0)
    - summary (str)
    """
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": YOUR_SITE_URL,
        "X-Title": YOUR_SITE_NAME
    }

    prompt = """
You are a rooftop solar analysis expert.

Given a rooftop satellite image, analyze it and return ONLY this valid JSON:

{
  "suitable": true or false,
  "estimated_area_sq_m": float (e.g. 42.5),
  "shading_issues": true or false,
  "confidence": float between 0 and 1,
  "summary": "One-line summary of rooftop's solar suitability"
}

⚠️ Strictly return ONLY valid JSON. No extra text, markdown, or explanation.
"""

    payload = {
        "model": "meta-llama/llama-3.2-11b-vision-instruct:free",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": image_url}}
                ]
            }
        ]
    }

    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            data=json.dumps(payload)
        )

        result = response.json()
        content = result["choices"][0]["message"]["content"]

        # Attempt to extract just the JSON object from response text
        start = content.find("{")
        end = content.rfind("}") + 1
        json_text = content[start:end]

        data = json.loads(json_text)
        return data

    except Exception as e:
        return {
            "error": str(e),
            "raw_response": response.text if 'response' in locals() else 'No response object'
        }
