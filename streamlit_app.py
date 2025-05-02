import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="SHL Assessment Recommender", layout="wide")
st.title("SHL Assessment Recommender")
st.markdown("Enter a job description or paste a URL to get SHL assessment recommendations.")

query_input = st.text_area("Job Description or URL:", height=200)

if st.button("Get Recommendations"):
    if not query_input.strip():
        st.error("Please enter a query.")
    else:
        try:
            response = requests.post("http://localhost:8000/recommend", json={"query": query_input})
            data = response.json()
            recs = data.get("recommendations", [])
            if not recs:
                st.warning("No recommendations found.")
            else:
                df = pd.DataFrame(recs)
                st.dataframe(df)
        except Exception as e:
            st.error(f"API request failed: {e}")