import streamlit as st
import requests
import os

st.set_page_config(page_title="Startup Idea Generator", page_icon="💡")

st.title("💡 Startup Idea Generator")
st.write("Input a problem, theme, or keywords to generate a startup plan.")

# User input
user_input = st.text_input("What Can I help With?")

# Generate by clicking the button
if st.button("Generate Startup Idea"):
    if user_input.strip() == "":
        st.warning("Please enter a problem or theme to proceed.")
    else:
        master_prompt = f"""
        Act as a startup mentor. A user is trying to build a startup around the following theme/problem:
        "{user_input}"
        Provide a complete startup plan including:
        1. Startup Name
        2. One-liner Pitch
        3. Problem Statement
        4. Proposed Solution
        5. Target Audience
        6. Business Model
        7. Revenue Streams
        8. Go-to-Market Strategy
        9. Technology Stack
        10. Competitor Analysis
        11. Long-Term Vision
        """

        # Sending request to Gemini API
        api_key = st.secrets["GEMINI_API_KEY"]
        endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

        headers = {"Content-Type": "application/json"}
        params = {"key": api_key}
        body = {"contents": [
            {"parts": [{"text": master_prompt}]}
             ]
        }

        response = requests.post(endpoint, headers=headers, params=params, json=body)

        if response.status_code == 200:
            result = response.json()
            content = result["candidates"][0]["content"]["parts"][0]["text"]
            st.markdown("### 🎉 Your Startup Plan")
            st.markdown(content)
        else:
            st.error("API Error. Please check your key or input.")

# Footer
st.markdown("---")
st.markdown("Created by **Rabeel Sohail**")