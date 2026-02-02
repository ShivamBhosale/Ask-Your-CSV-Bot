import streamlit as st
import pandas as pd
from data_engine import analyze_data
from llm_explainer import explain_result

st.set_page_config(page_title="Ask Your CSV")
st.title("Ask Your CSV")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview Data")
    st.dataframe(df.head())

    question = st.text_input("Ask a question about the data")

    if st.button("Ask"):
        try:
            result = analyze_data(df, question)
            explanation = explain_result(result, question)

            st.subheader("Answer")
            st.write(explanation)

        except Exception as e:
            st.error(str(e))
