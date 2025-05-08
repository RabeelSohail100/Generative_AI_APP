import requests

# Define your API key
api_key = "AIzaSyBNpgay3V0QRLyQ_V2-hDyw9BzfM7PNYN8"  # Replace with your actual API key

# Set the endpoint for listing available models
endpoint = "https://generativelanguage.googleapis.com/v1beta/models"

# Set up the parameters for the request
params = {"key": api_key}

# Make the request to the API
response = requests.get(endpoint, params=params)

# Check the response status and print the available models or error message
if response.status_code == 200:
    print(response.json())  # Print out the available models
else:
    print(f"Error: {response.status_code}")
