import streamlit as st
import pandas as pd
from pandasai import Agent
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the Streamlit page
st.set_page_config(page_title="CSV Analyzer with PandasAI", page_icon="📊", layout="centered")

# Header Section
st.markdown("""
    <style>
    .main-title {
        font-size: 42px;
        font-weight: bold;
        color: #4B8BBE;
    }
    .subheader {
        font-size: 22px;
        color: #5A5A5A;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">CSV Analyzer with PandasAI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subheader">Upload your CSV and ask questions about your data using natural language. Generate visual insights instantly!</p>', unsafe_allow_html=True)

# API Key Input
st.markdown("#### Enter your PandasAI API key:")
st.markdown(
    "Don't have an API key? Get your free API key [here](https://pandabi.ai)"
)
api_key = st.text_input("Enter your PandasAI API key:", type="password")

if api_key:
    # File Uploader for CSV Input
    st.markdown("### Upload a CSV file")
    uploaded_file = st.file_uploader("Choose a CSV file to start analysis", type="csv")

    if api_key:
    # File Uploader for CSV Input
    st.markdown("### Upload a CSV file")
    uploaded_file = st.file_uploader("Choose a CSV file to start analysis", type="csv")

    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
        
        # Check if dataframe is loaded properly
        st.write("CSV loaded successfully:")
        st.write(df.head())  # Display the first few rows of the dataframe
        
        # Initialize PandasAI Agent
        agent = Agent(df, config={"api_key": api_key})
        st.write("Agent created successfully")  # Check if agent is created

        if agent is None:
            st.error("Agent initialization failed. Please check the API key or data format.")


        # User query input
        st.markdown("### Enter your query:")
        user_query = st.text_input("Ask a question about your data")

        if user_query:
            if st.button("Analyze"):
                with st.spinner("Analyzing your data..."):
                    try:
                        # Get response from PandasAI
                        response = agent.chat(user_query)
                        st.markdown("### Analysis Result:")
                        st.success(response)

                        # Generate additional visualizations
                        if "Plot" in user_query or "plot" in user_query:
                            st.markdown("### Visualization")
                            fig, ax = plt.subplots(figsize=(10, 6))

                            # Assuming user asks for a bar plot (you can extend this based on needs)
                            if "histogram" in user_query or "bar" in user_query:
                                sns.barplot(x=df.iloc[:, 0], y=df.iloc[:, 1], ax=ax, palette="Set3")
                                ax.set_title(f"Bar Plot for {df.columns[0]} vs {df.columns[1]}")
                                ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")

                            # Show the plot
                            st.pyplot(fig)

                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")
else:
    st.info("Please enter your API key to begin.")

# Footer Section
st.markdown("---")
st.markdown("""
    <div style='text-align: center;'>
        💻 by <b>Om Wakale</b>
    </div>
""", unsafe_allow_html=True)
