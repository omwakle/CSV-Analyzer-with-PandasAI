# 📊 CSV Analyzer with PandasAI

This is a simple web application built with Streamlit that allows users to upload a CSV file, ask questions about the data using natural language, and generate visual insights instantly. The app uses [PandasAI](https://pandabi.ai) for natural language analysis of data, enabling a conversational interface to interact with data.

## Demo

https://csv-analyzer-with-pandasai.streamlit.app/


## Features

- Upload any CSV file for analysis.
- Ask natural language questions about the data (e.g., "What are the top 5 countries by sales?").
- View and interact with visualizations, such as bar charts and histograms, generated from your data.
- Supports customizable visual analysis based on user queries.


## Requirements

- Python 3.7+
- Streamlit
- Pandas
- PandasAI
- Matplotlib
- Seaborn

## Installation

1. Clone the repository or download the source code:

   ```bash
   git clone https://github.com/yourusername/csv-analyzer-pandasai.git
   cd csv-analyzer-pandasai
2. pip install -r requirements.txt
3. streamlit run app.py


## Usage
Get a PandasAI API key:
Sign up at PandasAI to get your free API key.

Run the application:
Use the command mentioned in the installation step to start the app.

Enter your API key:
On the app page, enter your PandasAI API key in the input field provided. If you don’t have an API key, you can get one here.

Upload a CSV file:
Click the "Choose a CSV file" button to upload your data.

Ask questions:
Type natural language questions in the query input box. For example:

"Which are the top 5 countries by revenue?"
"Show me a bar plot of sales data by country."
View results and visualizations:
The app will display the answer and any relevant visualizations based on your query.

## Example Queries
"Which are the top 5 countries by sales?"
"Show a histogram of revenue."
"Calculate the total revenue of European countries."
"Plot a bar graph of revenue for each country."
Customization
You can customize the app by editing the app.py file:

Modify the query logic or add new types of visualizations.
Adjust the layout and design using Streamlit features.

## Screenshot
![image](https://github.com/user-attachments/assets/4240430f-23bb-4659-9eee-ec9b22e07bb0)


Contributing
Feel free to submit issues or pull requests for new features, bug fixes, or improvements. Contributions are welcome!
