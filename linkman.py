import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import streamlit as st
from io import BytesIO

# File URL for the Excel file on GitHub
file_url = 'https://raw.githubusercontent.com/your_username/your_repository/main/link_data.xlsx'

# Function to load the Excel file
def load_excel(file_url):
    response = requests.get(file_url)
    with open('link_data.xlsx', 'wb') as f:
        f.write(response.content)
    df = pd.read_excel('link_data.xlsx')
    return df

# Function to save the DataFrame to the Excel file
def save_excel(df):
    df.to_excel('link_data.xlsx', index=False)

# Function to extract the base domain from a URL
def get_base_domain(url):
    parsed_url = urlparse(url)
    return f"{parsed_url.scheme}://{parsed_url.netloc}"

# Function to fetch and parse the webpage description
def fetch_description(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else 'No title found'
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        description = meta_desc['content'] if meta_desc else 'No description found'
        return f"Title: {title}\nDescription: {description}"
    except Exception as e:
        return f"Error fetching description: {e}"

# Function to convert DataFrame to Excel bytes
def to_excel_bytes(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    processed_data = output.getvalue()
    return processed_data

# Streamlit app setup
st.title("Link Management App")

# Load the Excel data
df = load_excel(file_url)

# Main Page
st.write("Link Management")
st.markdown("---")

link = st.text_input("Enter the link:")

if link:
    base_domain = get_base_domain(link)
    existing_domains = df['Links'].apply(get_base_domain)
    
    if base_domain in existing_domains.values:
        st.warning("Link is from the same website as an existing one. Please check it and try again.")
    else:
        description = fetch_description(link)
        new_row = pd.DataFrame({'Links': [link], 'Description': [description]})
        df = pd.concat([df, new_row], ignore_index=True)
        save_excel(df)
        st.success("Link and description have been added successfully.")

st.markdown("---")

st.write("### Current Links and Descriptions")
st.dataframe(df)

st.markdown("---")

# Download button for the updated spreadsheet
def download_excel():
    with open('link_data.xlsx', 'rb') as f:
        excel_bytes = f.read()
    return excel_bytes

excel_bytes = download_excel()
st.download_button(label="Download Excel", data=excel_bytes, file_name='links.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

st.markdown("---")

# Logout button (optional, can be removed if not needed)
#if st.button("Logout"):
#    st.success("You have been logged out.")
