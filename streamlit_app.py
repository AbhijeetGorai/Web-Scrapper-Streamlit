import streamlit as st
import requests
import time

def fetch_information(urls):
    """
    Function to call an external API with given URLs.
    Modify `API_ENDPOINT` with your actual API URL.
    """
    API_ENDPOINT = "https://your-api-endpoint.com/fetch"  # Replace with your actual API URL
    
    try:
        response = requests.post(API_ENDPOINT, json={"urls": urls})
        response.raise_for_status()  # Raise an error for bad responses
        return response.text  # Assuming API returns plain text; adjust as needed
    except requests.exceptions.RequestException as e:
        return f"API request failed: {str(e)}"

st.title("File Information Fetcher")

# Dropdown to select number of input boxes
num_inputs = st.sidebar.selectbox("Select number of URLs", list(range(1, 11)), index=0)

# Dynamic input fields based on dropdown selection
urls = []
for i in range(num_inputs):
    url = st.sidebar.text_input(f"Enter URL {i+1}", "")
    urls.append(url)

# Button to fetch information
if st.button("Fetch Information"):
    if all(urls):  # Ensure all fields are filled
        st.write("Fetching data, please wait...")
        time.sleep(2)  # Simulating delay
        fetched_data = fetch_information(urls)
        
        # Save to a text file
        file_name = "fetched_info.txt"
        with open(file_name, "w") as f:
            f.write(fetched_data)
        
        # Provide a download button
        with open(file_name, "rb") as f:
            st.download_button(label="Download Results", data=f, file_name=file_name, mime="text/plain")
    else:
        st.error("Please enter all URLs before fetching information.")
