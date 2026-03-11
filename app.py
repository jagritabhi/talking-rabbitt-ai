import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Talking Rabbitt 🐰")
st.write("Upload your sales data and ask questions!")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.dataframe(df)

    question = st.text_input("Ask a question about your data")

    if question:

        if "highest revenue" in question.lower():

            row = df.loc[df["Revenue"].idxmax()]

            st.success(f"Region with highest revenue: {row['Region']}")

            fig, ax = plt.subplots()
            ax.bar(df["Region"], df["Revenue"])
            ax.set_title("Revenue by Region")

            st.pyplot(fig)

        else:
            st.info("Try asking: Which region has highest revenue?")