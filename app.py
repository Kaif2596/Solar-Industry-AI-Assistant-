import streamlit as st
from vision_analyzer import analyze_rooftop_image
from solar_calculator import analyze_solar_potential
import time

# Set page config
st.set_page_config(page_title="Solar Industry AI Assistant  ☀️", layout="centered")

# --- Title and Instructions ---
st.title("🔆 Solar Industry AI Assistant")
st.markdown("Analyze rooftop solar potential using satellite imagery + AI.")
st.info("Upload a rooftop image or paste an image URL to get started.")

# --- Image Input Section ---
input_mode = st.radio("Select Input Method:", ["Image URL", "Upload Image"], horizontal=True)

image_url = None

if input_mode == "Image URL":
    image_url = st.text_input("🌐 Paste Image URL:")
else:
    uploaded_file = st.file_uploader("📤 Upload a Rooftop Image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        # Save temporarily to display & convert
        import tempfile
        import base64
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
            tmp.write(uploaded_file.read())
            image_url = f"data:image/png;base64,{base64.b64encode(open(tmp.name, 'rb').read()).decode()}"
            st.image(tmp.name, caption="Uploaded Rooftop", use_column_width=True)

# --- Analyze Button ---
if image_url and st.button("🔍 Analyze Rooftop"):
    with st.spinner("Analyzing image with AI..."):
        start_time = time.time()
        vision_result = analyze_rooftop_image(image_url)
        api_duration = round(time.time() - start_time, 2)  # in seconds

    required_keys = {"suitable", "estimated_area_sq_m", "shading_issues", "confidence", "summary"}

    if "error" in vision_result:
        st.error("⚠️ Vision API Error: " + vision_result["error"])
        st.code(vision_result.get("raw_response", ""), language="json")

    elif not required_keys.issubset(vision_result.keys()):
        st.error("⚠️ Incomplete JSON received from Vision API.")
        st.json(vision_result)

    else:
        st.success(f"✅ Rooftop Analyzed Successfully! (API time: {api_duration} sec)")


        st.subheader("🏠 Rooftop Summary")
        st.metric("🤖 AI Confidence", f"{vision_result['confidence']*100:.1f} %")
        st.progress(int(vision_result['confidence'] * 100))


        if vision_result.get("suitable", False):
            solar_stats = analyze_solar_potential(vision_result["estimated_area_sq_m"])

            with st.expander("📈 Solar Installation Recommendation"):
                st.markdown(f"""
                - **Panel Type:** {solar_stats['panel_type']}
                - **Panel Count:** {solar_stats['panel_count']}
                - **Total Capacity:** {solar_stats['total_capacity_kw']} kW
                """)
                st.metric("📏 Panel Coverage Efficiency", f"{solar_stats['panel_coverage_percent']} %")

            with st.expander("💰 ROI & Financials"):
                st.markdown(f"""
                - **Estimated Cost:** ₹{solar_stats['estimated_cost_inr']}
                - **Government Subsidy:** ₹{solar_stats['gov_subsidy_inr']}
                - **Final Cost After Subsidy:** ₹{solar_stats['final_cost_inr']}
                - **Estimated Yearly Savings:** ₹{solar_stats['estimated_yearly_savings_inr']}
                - **Payback Period:** {solar_stats['payback_period_years']} years
                """)

        else:
            st.warning("❌ This rooftop may not be suitable for solar installation.")

# --- Footer ---
st.markdown("---")
st.caption("Built with ❤️ using LLaMA Vision AI, Streamlit and Python.")
